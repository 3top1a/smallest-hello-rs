#! /bin/bash

# Install nightly toolchain
# rustup toolchain install nightly-x86_64-unknown-linux-gnu
# rustup component add rust-src --toolchain nightly

RUSTFLAGS="-Ctarget-cpu=native -Clink-args=-nostartfiles -Ctarget-feature=+crt-static -C relocation-model=static -Clink-args=-Wl,-n,-N,--no-dynamic-linker,--no-pie,-build-id=none " cargo +nightly b --release 

# Processing
# Copy to root
cp ./target/release/smallest-hello hello

# Remove unnecesary sectors
objcopy -R .shstrtab -R .comment hello hello.tmp
mv hello.tmp hello

# Remove everything after Hello Rust!\n\x00, mainly the section header
# Ideally you would use something like https://github.com/blackle/Section-Header-Stripper
#python truncate.py

# Or sstrip from https://github.com/BR903/ELFkickers, highly recommend that
sstrip -z hello

python3 mod.py

echo
echo "Final binary size:"
/bin/ls -l hello | awk '{print $5}'
file hello

./hello
