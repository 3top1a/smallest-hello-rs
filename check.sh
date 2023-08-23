#! /bin/bash

# Install nightly toolchain
# rustup toolchain install nightly-x86_64-unknown-linux-gnu
# rustup component add rust-src --toolchain nightly


RUSTFLAGS="-Ctarget-cpu=native -Clink-arg=-nostartfiles -Ctarget-feature=+crt-static -C relocation-model=static -Clink-args=-Wl,-n,-N,--no-dynamic-linker,--no-pie,-build-id=none " cargo +nightly b --release 

# Processing
# Remove unnecesary sectors
objcopy -R .shstrtab -R .comment ./target/release/smallest-hello ./target/release/smallest-hello.tmp
mv ./target/release/smallest-hello.tmp ./target/release/smallest-hello

# Remove everything after Hello Rust!\n\x00, mainly the section header
# Ideally you would use something like https://github.com/blackle/Section-Header-Stripper
python truncate.py

echo
echo "Final binary size:"
/bin/ls -l target/release/smallest-hello | awk '{print $5}'
file target/release/smallest-hello

./target/release/smallest-hello
