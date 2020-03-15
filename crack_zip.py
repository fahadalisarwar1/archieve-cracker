import zipfile
from tqdm import tqdm

dictionary_list = "passwords.txt"

zipped_file = "image.zip"

zip_file = zipfile.ZipFile(zipped_file)
# count the number of words in this wordlist
n_words = len(list(open(dictionary_list, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)

with open(dictionary_list, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            searchterm = (word.decode('utf-8').strip('\n'))
            zip_file.extractall(pwd=bytes(searchterm, "utf-8"))
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")