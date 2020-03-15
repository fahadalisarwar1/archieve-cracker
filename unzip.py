import zipfile
zip_name = "image.zip"

if __name__ == "__main__":
    print("[+] Extracting ZIP: ", zip_name)

    passwd = "12345"

    with zipfile.ZipFile(zip_name) as file:
        file.extractall(pwd=bytes(passwd, "utf-8"))
        

