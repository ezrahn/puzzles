#implement an algorithm to determine if a string has all unique characters
#what if you cannot use additional data structure


def hasAllChars(st):
    chars = "abcdefghijklmnopqrstuvwxyz"
    counts = {}
    for i in xrange(len(chars)):
        counts[chars[i]] = 0
    
    for i in xrange(len(st)):
        c = st[i].lower()
        if c in chars:
            counts[c] += 1 
        
    mul = 1
    for i in xrange(len(chars)):
       mul *= counts[chars[i]]
    
    return mul > 0 

assert hasAllChars('beeskleiushdkjhf') == False

assert hasAllChars("rreawbcsdefghwerijklmnosgfpqerrgdfgshtujvwxyz")

assert hasAllChars("rreawbcsdefghwerijklmnosgfpqe 2 rrgdfgsh tujvwxyz")

assert hasAllChars("rreawbcsdefghwerijklmnosgfpqerrgANBKEdfgshtujvwxyz")
    