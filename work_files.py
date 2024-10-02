with open("work_files.py", mode="r") as source_file, open("file2.txt", mode="w") as dest_file:
    content = source_file.read()
    print(content)
    dest_file.write(content)
