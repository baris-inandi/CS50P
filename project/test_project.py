import os
import shutil

import project
from project import (
    decrypt_file,
    encrypt,
    encrypt_file,
    generate_decrypt_outfile,
    zip_directory,
)

TEST_DIRECTORY = ".test_files"

td = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".test_files")
if os.path.isdir(td):
    shutil.rmtree(td)
os.mkdir(td)
os.chdir(td)


def test_generate_decrypt_outfile():
    assert generate_decrypt_outfile("test.txt.aes") == "test.dec.txt"
    assert generate_decrypt_outfile("test.tar.gz.aes") == "test.dec.tar.gz"
    assert generate_decrypt_outfile("test.x.y.z.aes") == "test.dec.x.y.z"
    assert generate_decrypt_outfile("test") == "test.dec"


def test_zip_directory():
    d = "zip_directory"
    if not os.path.isdir(d):
        os.mkdir(d)
    new_path = zip_directory(d)
    assert new_path == "zip_directory.zip"


def test_encrypt_directory():
    d = "encrypt_directory"
    if not os.path.isdir(d):
        os.mkdir(d)
    f = zip_directory(d)
    new_path = encrypt_file(f, "password")
    assert os.path.exists(new_path)


def test_encrypt_decrypt_file():
    data = "super secret data"
    fpath = "encrypt_decrypt_file.txt"
    f = open(fpath, "w")
    f.write(data)
    f.close()
    new_path = encrypt_file(fpath, "password")
    assert os.path.exists(new_path)
    dec_path = decrypt_file(new_path, "password")
    assert os.path.exists(dec_path)
    f = open(dec_path, "r")
    assert f.read() == data
    f.close()


def test_encrypt_file():
    fpath = "encrypt.txt"
    f = open(fpath, "w")
    f.close()
    new_path = encrypt_file("encrypt.txt", "password")
    assert os.path.exists(new_path)


def test_available_path():
    fpath = "available_path.txt"
    f0path = "available_path.txt.aes"
    f1path = "available_path.txt.1.aes"
    f = open(fpath, "w")
    f0 = open(f0path, "w")
    f1 = open(f1path, "w")
    new_path = encrypt_file("available_path.txt", "password")
    assert os.path.exists(new_path)
    f.close()
    f0.close()
    f1.close()
