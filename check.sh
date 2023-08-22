#! /bin/bash

# Install nightly toolchain
# rustup toolchain install nightly-x86_64-unknown-linux-gnu
# rustup component add rust-src --toolchain nightly


RUSTFLAGS="-Ctarget-cpu=native -Clink-args=-nostartfiles -Clink-args=-Wl,-pie,-n,-N,--no-dynamic-linker" cargo +nightly b --release 

# Processing

echo
echo "Final binary size:"
/bin/ls -l target/release/smallest-hello | awk '{print $5}'
file target/release/smallest-hello

