import struct

# Remove first ~100 bytes, still makes the ELF file valid
# Assumes 64 bit

# https://en.wikipedia.org/wiki/Executable_and_Linkable_Format
# Available space for writing
# 0x09 -> 7b
# If your exe is 64 bit and entry point fits in 1 byte,
# 0x18 + 1 -> 7b
# If you disrespect the elf header
# 0x1C -> 0x40
# But in my experience the empty space ends at 0xE7


# Entry point is 0x18

with open('hello', 'rb+') as file:
    data = bytearray(file.read())

    file.seek(0x09)

    file.write(b"Hello R")

    file.seek(0x80)

    file.write(b"ust! How much free space is in here? test123456\n")
