# READ FILE

#read the file on the Files Folder 
# and return the content of the file

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


file = read_file("Files/test.txt")

print(file)

# -----------------------------------------------------
# WRITE A FILE

#write a file on the Files Folder
# and return the content of the file

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


write_file("Files/newFile.txt",  "This is a new file")

