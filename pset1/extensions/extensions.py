bindings = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "document/pdf",
    "txt": "text/txt",
    "zip": "document/zip",
}

out = bindings[input("File name: ")]

if out == None:
    out = "application/octet-stream"
