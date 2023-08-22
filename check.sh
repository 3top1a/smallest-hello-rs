#! /bin/bash

# Install nightly toolchain
# rustup toolchain install nightly-x86_64-unknown-linux-gnu
# rustup component add rust-src --toolchain nightly


# TODO nightly
cargo b --release

# Processing

echo
echo "Final binary size:"
/bin/ls -l target/release/smallest-hello | awk '{print $5}'

