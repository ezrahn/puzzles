

def oneAway(src, dest):
    print "Comparing %s, %s" %(src, dest)
    if src == dest:
        return True
  
    if abs(len(src) - len(dest)) > 1:
        return False
        
    diffCount = 0
    
    ptS = ptD = 0
    while True:
        #the chars are the same, just move on
        if src[ptS] == dest[ptD]:
            print "the chars are the same, just move on"
            ptS += 1
            ptD += 1
        #the current chars differ
        else:
            if diffCount == 1:
                print "We had a diff before, and now another one... False!"
                return False
            #the rest are the same, it's a replacement.
            if src[ptS+1:] == dest[ptD+1:]:
                print "the rest are the same, it's a replacement."
                diffCount += 1
                ptS += 1
                ptD += 1
            elif len(dest) < len(src) and src[ptS+2:] == dest[ptD+1:]:
                print "src[ptS+2:] == dest[ptD+1:], addition"
                diffCount += 1
                ptS += 2
                ptD += 1
            else:
                print "Diff char, and diff tail... False!"
                return False
                
        #source reaches the end
        if len(src) - ptS == 1:
            #dest reaches the end, we are done
            if len(dest) - ptD == 1:
                print "dest reaches the end, we are done"
                break
            #dest hasn't reach the end, it's an addition
            else:
                print "dest hasn't reach the end, it's an addition"
                diffCount += 1
        
        #dest reaches the end
        if len(dest) - ptD == 1:
            return True
                
        if diffCount > 1:
            return False
        
                
    return True
  
  
assert oneAway('pale', 'pale')

assert oneAway('pale', 'ple')

assert oneAway('pales','pale')

assert oneAway('pale', 'bale')

assert oneAway('paale', 'pale')

assert oneAway('paaaaale', 'paaale') == False

assert oneAway('pale', 'bake') == False
