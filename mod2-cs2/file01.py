import re

# import Fernet as Fernet
from fernet import Fernet


def encryptfp(string, key1):
    fernet = Fernet(key1)
    return fernet.encrypt(string.encode())


def decryptfp(fp, key1):
    fernet = Fernet(key1)
    return fernet.decrypt(fp).decode()


def validate_fingerprint(word):
    result = True
    if re.search(r'\s', word):
        result = False
    if result:
        if not len(word) == 12:
            result = False
        else:
            if not re.search(r'[a-z|A-Z|0-9]{12}', word):
                result = False
    return result


def validate_refId(word):
    result = True
    if re.search(r'\s', word):
        result = False
    return result


refID = input('enter Reference ID: ')           #   'dklsdi98KK'  #
fingerprint = input(' enter Finger Print: ')    #   'dkldskKKKK3K'  #

if validate_fingerprint(fingerprint) and validate_refId(refID):
    print('Reference Id:\t', refID)
    print('fingerprint:\t', fingerprint)
    key = Fernet.generate_key()
    ecmsg = encryptfp(fingerprint, key)
    print('Encripted:\t', ecmsg)
    dcmsg = decryptfp(ecmsg, key)
    print('De-cripted:\t', dcmsg)

#     / home / sasops / Documents / ops / edureka - python - scripting / python_edureka / bin / python / home / sasops / PycharmProjects / python_edureka / mod2_cs2 / file01.py
#     enter
#     Reference
#     ID: dklsdi98KK
#     enter
#     Finger
#     Print: dkldskKKKK3K
# Reference
# Id: dklsdi98KK
# fingerprint: dkldskKKKK3K
# Encripted: b'gAAAAABjMQgoOy114Iz4drypeyG-vF21035ve6Ta3-7TzkmfmOKC69ircaXYq-QSf-4-JKIK5-1TXC_vkD4MIYhAJzcr7AQy_w=='
# De - cripted: dkldskKKKK3K
#
# Process
# finished
# with exit code 0