#!/usr/bin/python3

import os
import shutil
from os import path

import pyAesCrypt as aes
import termcolor as tc
import typer

app = typer.Typer(
    name="FileEncryptor",
    short_help="FileEncryptor encrypts and decrypts files using AES-256-CBC.",
)


def zip_directory(directory: str):
    """Zips a directory and returns the path to the zip file."""
    directory = directory.rstrip("/").lstrip("/")
    shutil.make_archive(directory, "zip", directory)
    return directory + ".zip"


def encrypt_file(inpath: str, password: str, index: int = 0) -> str:
    """
    Encrypts a file using AES-256-CBC.

    If the output file already exists,
    it will be named <filename>.<index>.aes.
    The function will recursively call itself with index+1
    until it finds an available filepath.

    If the index is greater than 99, an OSError will be raised.

    returns the output aes path
    """
    outpath = inpath + ".aes"
    if index > 0:
        outpath = inpath + f".{index}.aes"
    if index > 99:
        tc.cprint(f"Could not encrypt '{inpath}': no available filepath", "red")
        raise OSError("No available filepath: too many files with the same name.")
    if not path.exists(inpath):
        tc.cprint(
            f"Skip file {'inpath'}: Could not encrypt file because it does not exist.",
            "red",
        )
        return ""
    if not path.exists(outpath):
        aes.encryptFile(inpath, outpath, password)
        if inpath.endswith(".aes"):
            tc.cprint(f"Re-Encrypted '{inpath}' to '{outpath}'.", "yellow")
        else:
            tc.cprint(f"Encrypted '{inpath}' to '{outpath}'.", "green")
        return outpath
    return encrypt_file(inpath, password, index + 1)


def password_error(password: str) -> str:
    """
    Returns an error string if the password is invalid.
    Otherwise, returns an empty string.
    """
    if len(password) < 4:
        return "Password must be at least 4 characters long."
    if len(password) > 256:
        return "Password must be less than 256 characters long."
    return ""


def input_password(validate: bool = True, prompt: str = "Enter password") -> str:
    """
    Prompts the user for a password.
    Returns the password if it is valid.
    Otherwise, prompts the user again.
    """
    password_valid = False
    while not password_valid:
        password = typer.prompt(prompt, hide_input=True)
        if validate:
            perror = password_error(password)
        else:
            perror = ""
        password_valid = perror == ""
        if not password_valid:
            tc.cprint(perror, "red")
    return password


@app.command()
def encrypt(files: list[str]):
    """
    Encrypts files using AES-256-CBC.
    If a directory is passed, it will be zipped and encrypted.
    The output file will be named <filename>.aes.
    """
    isdir = False
    for filepath in files:
        password = input_password(
            validate=True, prompt=f"Enter password for '{filepath}'"
        )
        if path.isdir(filepath):
            isdir = True
            old = filepath
            filepath = zip_directory(filepath)
            tc.cprint(f"Zipped directory '{old}' to '{filepath}'.", "yellow")
        encrypt_file(filepath, password)
        if isdir:
            os.remove(filepath)


def generate_decrypt_outfile(f: str) -> str:
    split = f.split(".", maxsplit=1)
    srcname = split[0].strip()
    ext = split[-1].strip()[:-4]
    return f"{srcname}.dec{'.' if ext != '' else ''}{ext}"


def decrypt_file(file: str, password: str) -> str:
    if not file.endswith(".aes"):
        tc.cprint(
            f"Skip file '{file}': Could not decrypt file because it is not an .aes encrypted file.",
            "red",
        )
        return ""
    outfile = generate_decrypt_outfile(file)
    aes.decryptFile(file, outfile, password)
    tc.cprint(f"Decrypted '{file}' to '{outfile}'.", "cyan")
    return outfile


@app.command()
def decrypt(files: list[str]):
    """Decrypts files using AES-256-CBC."""
    try:
        for file in files:
            password = input_password(
                validate=False, prompt=f"Enter password for '{file}'"
            )
            decrypt_file(file, password)
    except ValueError:
        tc.cprint("Incorrect password or corrupt file.", "red")


def main():
    app()


if __name__ == "__main__":
    main()
