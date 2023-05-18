# FileEncryptor

**Video Demo:**  youtube.com/watch?v=xyz

## Description

FileEncryptor is a command line tool that allows you to encrypt and decrypt files using a password. It uses the AES-256-CBC algorithm to encrypt files.

### Features

#### Encryption

> Use `python project.py encrypt <files>` to encrypt a file.

- Prompts user for a password.
- For each file:
  - If `file` is a directory:
    - The directory is zipped into a temporary file.
    - `file` is set to the temporary `zip` file for encryption.
  - Forms a path, `output file` with `.aes` appended to the name.
    - If the file exists, `<index>.aes` is appended to the name instead of `.aes` where index is incremented until the file path is available.
  - `pyAesCrypt` is used to encrypt the input file and write the output to the `output file`.
  - The user is notified of the encryption status.
  - if a temporary zip file was created, it is deleted.

For example:

```plaintext
python project.py encrypt file.txt
```

creates `file.txt.aes`, an encrypted file, in the same directory.

#### Decryption

- Prompts user for a password.
- Decrypts the `.aes` file using the password.
- Writes the decrypted file to `<filename>.dec.<extension>` in the same directory.

### Libraries

The project utilizes three libraries, all available through `pip` and listed in the `requirements.txt` file in the project root:

> Use `pip install -r requirements.txt` to install the libraries.

```plaintext
pyAesCrypt==6.0.0
typer==0.9.0
termcolor==1.1.0
```

- **pyAesCrypt:** It is the library used for encryption and decryption. It provides higher level functions that can be used to encrypt and decrypt files.
- **typer:** It is the library used for creating the command line interface.
- **termcolor:** It is the library used for printing colored text in the terminal.

## Demo

Let's test my CS50P final project, FileEncryptor  
Start off by printing the help message  
As you can see we have two commands: encrypt and decrypt  
```./project.py --help```

Let's create a file with some secret data that we want to encrypt  
We'll use the echo command to create a file called test.txt  
```echo "super secret data" >test.txt```

Using cat, let's print the contents of the file to make sure it's there  
cat test.txt

Now we can encrypt the file using FileEncryptor  
```./project.py encrypt test.txt```

Let's try to print the contents of the file again  
```cat test.txt.aes```
As you can see, the contents of the file are now encrypted  
...and are not human-readable  

Now we can decrypt the file using FileEncryptor  
```./project.py decrypt test.txt.aes```

Now let's try to input the wrong password  
As you can see we get an error message  
```./project.py decrypt test.txt.aes```
Let's try again with the correct password  
As you can see, the contents of the file are now decrypted  

The contents of the file are now decrypted at test.dec.txt  
Let's use cat to print the contents of the file  
```cat test.dec.txt```

Now, let's clean up the files we created  
```rm -rf test*```

FileEncryptor also supports encrypting multiple files  
Let's use a glob to encrypt all files that end in .txt  
First, let's create some files  
```touch 1.txt 2.txt 3.txt```
Now, let's encrypt all files that end in .txt  
```./project.py encrypt *.txt```
Now, FileEncryptor will prompt us for a password for each file  
Now, all files are encrypted.  

We can also decrypt multiple files at once  
Let's decrypt all files that end in .txt.aes  
```./project.py decrypt *.txt.aes```

Now, let's clean up the files we created  
```rm -rf *.txt*```

FileEncryptor also supports encrypting directories  
Let's create a directory with some files  
```mkdir test```
```touch test/1.txt test/2.txt test/3.txt```
Now, let's encrypt the directory  
```./project.py encrypt test```

```./project.py decrypt test.aes```
and when we decrypt the directory a decrypted zip file is created  
let's unzip the file and see the original content  

Now, let's clean up the files we created  
```rm -rf test*```

Now, let's explore some edge cases  
Now, let's try to encrypt a file that doesn't exist  
```./project.py encrypt no```

We can also try to encrypt a file that is already encrypted  
Let's create a file  
```echo "super secret data" >test.txt```
Now, let's encrypt the file  
```./project.py encrypt test.txt```
Now, let's try to encrypt the file again  
```./project.py encrypt test.txt```
As you can see, FileEncryptor will increment the file name to avoid overwriting  

We can also try to re-encrypt a file that is already encrypted  
```echo "super secret data" >test.txt```
```./project.py encrypt test.txt.aes```
As you can see, FileEncryptor will warn us that the file is already encrypted  

We can also try to decrypt a file that is not encrypted  
```./project.py decrypt test.txt```
As you can see, FileEncryptor will warn us that the file is not encrypted  

Let's clean up  
```rm -rf test*```
