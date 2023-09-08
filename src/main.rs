#![no_std]
#![no_main]

use core::arch::asm;

// Prefix all file pointers with 0x4000 (e.g. 0x07 -> 0x400007)

#[no_mangle]
pub extern "C" fn _start(_argc: isize, _argv: *const *const u8) {
    write_to_std_out(0x40002B as *const u8, 5);
    write_to_std_out(0x400058 as *const u8, 9);

    exit(0);
}

fn write_to_std_out(string_pointer: *const u8, string_length: usize) {
    unsafe {
        asm!(
            "syscall",
            in("rax") 1, // write syscall number
            in("rdi") 1, // stdout file descriptor, 2 is stderr
            in("rsi") string_pointer,
            in("rdx") string_length,
            out("rcx") _, // clobbered by syscalls
            out("r11") _, // clobbered by syscalls
            lateout("rax") _, // clobbered by syscalls too I think
        );
    }
}

fn exit(code: i32) {
    unsafe {
        asm!(
            "syscall",
            in("rax") 60,
            in("rdi") code,
            options(noreturn),
        );
    }
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}
