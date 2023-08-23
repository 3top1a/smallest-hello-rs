
search_string = b"Hello, Rust!\n\x00"
binary_file_path = "target/release/smallest-hello"

with open(binary_file_path, "rb+") as file:
    content = file.read()
    position = content.find(search_string)
    
    if position != -1:
        file.seek(position + len(search_string))
        file.truncate()
        print("Truncated the file after the search string.")
    else:
        print("Search string not found in the file.")
