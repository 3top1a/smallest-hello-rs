#![no_std]
#![no_main]

const MSG: &'static str = "Hello, Rust!\n";

use core::arch::asm;

#[no_mangle]
pub extern "C" fn _start(_argc: isize, _argv: *const *const u8) {
    write_to_std_out(MSG.as_ptr(), MSG.len());

    exit(0);
}

fn write_to_std_out(what_pointer: *const u8, what_length: usize) {
    unsafe {
        asm!(
            "syscall",
            in("rax") 1, // write syscall number
            in("rdi") 1, // stdout file descriptor, 2 is stderr
            in("rsi") what_pointer,
            in("rdx") what_length,
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
