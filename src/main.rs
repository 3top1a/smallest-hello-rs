#![no_main]
#![no_std]

#![feature(rustc_private)]
extern crate libc;

#[no_mangle]
pub extern "C" fn main(_argc: isize, _argv: *const *const u8) -> isize {
    const HELLO: &'static str = "Hello, Rust!\n\0";

    unsafe {
        libc::printf(HELLO.as_ptr() as *const _);
    }

    0
}

#[panic_handler]
fn my_panic(_info: &core::panic::PanicInfo) -> ! {
    loop {}
}

