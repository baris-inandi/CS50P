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
# use .get here to avoid an Exception
out = bindings.get(ext)

if out is None:
    # if the extension is not defined, apply the default output
    out = "application/octet-stream"
print(out)
