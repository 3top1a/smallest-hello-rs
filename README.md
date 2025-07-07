# smallest-hello-rs
Smallest 64-bit `Hello, World!` in Rust in the World[^1].
[Follow up blog post available here](https://e-topy.srht.site/small-rust.html).
Using compiler/linker flags and a simple python script, I managed to get the size down from `276792` bytes (270KiB) to a mere `149` bytes.
The binary is called `hello` and checked into git.
For comparison, the smallest [Windows Hello World! in Rust](https://github.com/retep998/hello-rs/tree/master) is `1536` bytes.
There's still a LOT more space in the ELF header, as most of it is ignored.

[^1]: Most probably, the only other one I was able to find was [151 bytes](https://mainisusuallyafunction.blogspot.com/2015/01/151-byte-static-linux-binary-in-rust.html) and only prints `Hello!`.

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
- Mark all the editable fields with a special character
- Go for a beer?
