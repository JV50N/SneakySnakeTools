import zipfile
from tqdm import tqdm

# TODO: Add wordlists to project path
# TODO: Add system argv for zipfile


# path to the wordlist you want to use
wordlist = "wordlist.txt"
# the zip file you want to crack
zip_file = "zip.zip"

# init the zip file object
zip_file = zipfile.ZipFile(zip_file)
# count how many words are in the wordlist
word_ammount = len(list(open(wordlist, "rb")))
# print the total number of possible passwords
print('Total passwords to test: ', word_ammount)

with open(wordlist, 'rb') as wordlist:
    for word in tqdm(wordlist, total=word_ammount, unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print('Password Found: ', word.decode().strip())
            exit(0)
print('Password not found, try another wordlist...')