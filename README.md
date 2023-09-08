# smallest-hello-rs
Smallest Hello World! in rust using Cargo.
Full blog post coming "soon".
The binary is called `hello` and checked into git.
Using compiler and linker flags, I managed to get the size down from `276792` bytes (270KiB) to `149` bytes.
For comparison, the smallest [Windows Hello World! in Rust](https://github.com/retep998/hello-rs/tree/master) is `1536` bytes.


Some very helpful resources:
- https://mainisusuallyafunction.blogspot.com/2015/01/151-byte-static-linux-binary-in-rust.html
- https://dev.to/szymongib/single-syscall-hello-world-in-rust-part-2-4jj4
- https://os.phil-opp.com/freestanding-rust-binary/
- https://darkcoding.net/software/a-very-small-rust-binary-indeed/
- https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html
- https://www.muppetlabs.com/~breadbox/software/tiny/revisit.html
- https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html
- http://timelessname.com/elfbin/
- https://in4k.github.io/wiki/linux
- https://jacobgw.com/blog/zig/low-level/2021/03/15/elf-linux.html

## Ideas

- Put the whole message into one buffer, makes one less syscall
- Go for a beer?
