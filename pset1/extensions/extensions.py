# bind all defined file types
bindings = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "application/txt",
    "zip": "application/zip",
}

# split the input with delimeter "." and get the last element (index -1)
ext = input("File name: ").split(".")[-1]
out = bindings[ext]

if out is None:
    # if the extension is not defined, apply the default output
    out = "application/octet-stream"
print(out)
