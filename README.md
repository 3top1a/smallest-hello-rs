# smallest-hello-rs
Smallest Hello World! possible*[^1] in rust using Cargo.
Full blog post coming "soon".
The binary is called `hello` and checked into git.
Using compiler and linker flags, I managed to get the size down from `276792` bytes (270KiB) to `214` bytes.
For comparison, the smallest [Windows Hello World! in Rust](https://github.com/retep998/hello-rs/tree/master) is `1536` bytes.

[^1]: Not really, apparently someone got a [151 byte](https://mainisusuallyafunction.blogspot.com/2015/01/151-byte-static-linux-binary-in-rust.html) executable, but that's using raw rustc and not Cargo.

Some very helpful resources:
- https://mainisusuallyafunction.blogspot.com/2015/01/151-byte-static-linux-binary-in-rust.html
- https://dev.to/szymongib/single-syscall-hello-world-in-rust-part-2-4jj4
- https://os.phil-opp.com/freestanding-rust-binary/
- https://darkcoding.net/software/a-very-small-rust-binary-indeed/
- https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html
- https://gcc.gnu.org/onlinedocs/gcc/Link-Options.html
- http://timelessname.com/elfbin/
- https://in4k.github.io/wiki/linux
