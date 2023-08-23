#! /bin/bash

# Install nightly toolchain
# rustup toolchain install nightly-x86_64-unknown-linux-gnu
# rustup component add rust-src --toolchain nightly


# -Clink-arg=-nostartfiles
RUSTFLAGS="-Ctarget-cpu=native -Clink-arg=-nostartfiles -Ctarget-feature=+crt-static -Clink-args=-Wl,-n,-N,--no-dynamic-linker,--no-pie" cargo +nightly b --release 

# Processing

echo
echo "Final binary size:"
/bin/ls -l target/release/smallest-hello | awk '{print $5}'
file target/release/smallest-hello

./target/release/smallest-hello

