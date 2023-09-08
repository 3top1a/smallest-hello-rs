import struct

# Hello Rust!
# 0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x20, 0x52, 0x75, 0x73, 0x74, 0x21

with open('hello', 'rb+') as file:
    data = bytearray(file.read())

    # Calculate the entry point offset
    file.seek(0x18)
    entry_point_offset: int = struct.unpack('B', file.read1(1))[0]
    print(
        f"Entry point is at byte {entry_point_offset} ({hex(entry_point_offset)})")

    file.seek(entry_point_offset)
    bytes_after_entry_point: bytes = file.read1(len(data))

    # Clear the existing ELF header
    file.seek(0)
    file.truncate()

    data = bytes([
        0x7F, 0x45, 0x4C, 0x46, # 4b, Header
        0x02, # 1b, class, 64bit
        0x01, # 1b, endianness, LE
        0x01, # 1b, ELF Version
        0x00, # 1b, ABI type, SystemV
        0x00, # 1b, ABI version
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # 7b, e_ident
        0x02, 0x00, # 2b, e_type, executable
        0x3E, 0x00, # 2b, e_machine, AMD x86-64
        0x01, 0x00, 0x00, 0x00, # 4b, e_version
        
        # 8b, e_entry, entry point
        0xB0 - 32 - 16 - 16, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 
        
        # 8b, e_phoff, start of program header
        0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        
        # 8b, e_shoff, start of section header table
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

        # 4b, e_flags
        0x00, 0x00, 0x00, 0x00,

        # 2b, e_ehsize, Contains the size of this header, normally 64 Bytes for 64-bit and 52 Bytes for 32-bit format
        0x40, 0x00,
        
        # 2b, e_phentsize, size of program header, 54b
        0x38, 0x00,

        # 2b, e_phnum, number of entries in program header table
        0x01, 0x00,

        # 2b, e_shentsize, size of section header table entry
        0x40, 0x00,

        # 2b, e_shnum, number of section header entries
        0x00, 0x00,

        # 2b, e_shstrndx
        0x00, 0x00,
        

        ### /// PROGRAM HEADERS ///

        # 4b, p_type, 1 for loadable
        0x01, 0x00, 0x00, 0x00,

        # 4b, p_flags
        # 0x07 = +RWX
        # The rest is data
        0x07, 0x48, 0x65, 0x6C,
        
        # 8b, p_offset, offset of the segment in the file image
        0xB0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

        # 8b, p_vaddr, virtual addr of segment in memory start of this segment
        0xB0, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,

        # 8b, p_paddr, same as vaddr except on physical systems
        #0xB0, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00,
        # Seems it's fine replacing it with data?
        0x6C, 0x6F, 0x20, 0x52, 0x75, 0x73, 0x74, 0x21,

        # 8b, p_filesz
        # The first byte was 0x25 but I overwrote it into a newline (0A)
        0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        
        # 8b, p_memsz
        0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,

        # 8b, p_align
        # it doesn't segfault when I comment it out so f it
        #0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ])

    file.write(data)
    file.write(bytes_after_entry_point)
