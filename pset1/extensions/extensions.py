# bind all defined file types
bindings = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

# split the input with delimeter "." and get the last element (index -1)
ext = input("File name: ").split(".")[-1].lower()
out = bindings.get(ext) # use .get to avoid an Exception

if out is None:
    # if the extension is not defined, apply the default output
    out = "application/octet-stream"
print(out)
