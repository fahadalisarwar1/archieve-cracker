import optparse
import zipfile
from threading import Thread


def extract_zip(zFile, password):
    match = False
    try:
        zFile.extractall(pwd=password)
        print("[+] Password found : ", password)
        match = True
    except:
        pass
    


if __name__ == "__main__":
    print("[+] Cracking ZIP")
    parser = optparse.OptionParser("usuage %prog "+\
            "-f <zip-file> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")

    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")

    (options, args) = parser.parse_args()

    if options.zname == None or options.dname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    
    zFile = zipfile.ZipFile(zname)

    passFile = open(dname)
    for line in passFile.readlines():
        passwd = line.strip("\n")
        
        t = Thread(target=extract_zip, args=(zFile, passwd))
        t.start()