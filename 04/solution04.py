import itertools

def check_passphrases(fname):
    f = open(fname)
    for passphrase in f:
        
        

def check_passphrase(passphrase):
    combs = itertools.combinations([word for word in passphrase.split()], 2)
    for t in combs:
        if t[0] == t[1]: return False
    return True