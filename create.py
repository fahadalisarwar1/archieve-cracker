from zipfile import ZipFile
import zipfile


if __name__ == "__main__":

    toZip = "image.jpg"

    try:
        with ZipFile("image.zip") as file:
            print("ok")
            file.write("image.jpg")
    except zipfile.BadZipfile as err:
        print("[-] Error Bad Zip file")
        pass


    

