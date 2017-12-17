import itertools

def check_no_dupes(fname):
    return check_passphrases(fname, make_equality_test())

def check_no_anagrams(fname):
    return check_passphrases(fname, make_is_anagram())
    
def check_passphrases(fname, check):
    f = open(fname)
    nvalid = 0
    for passphrase in f:
        if check_passphrase(passphrase, check):
            nvalid += 1
    f.close()
    
    return nvalid

def check_passphrase(passphrase, check):
    combs = itertools.combinations([word for word in passphrase.split()], 2)
    for t in combs:
        if check(t[0], t[1]): return False
    return True
    
def make_equality_test():
    return lambda x, y: x == y
    
def make_is_anagram():
    return lambda s, o: sorted([c for c in s]) == sorted([c for c in o])
