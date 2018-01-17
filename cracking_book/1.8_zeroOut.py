#given a matrix, if an element is found with a 0, zero out the row and the col


def zeroOut(mInput):
    xIndeces = []
    yIndeces = []
    
    for i in xrange(len(mInput)):
        for j in xrange(len(mInput[i])):
            if mInput[i][j] == 0:
               xIndeces.append(i)
               yIndeces.append(j)

    for i in xrange(len(mInput)):
        for j in xrange(len(mInput[i])):
            if i in xIndeces or j in yIndeces:
               mInput[i][j] = 0
    
    return mInput


def printMatrix(matrix):
    for i in xrange(len(matrix)):
        print matrix[i]
        
    print ""

def test1():
    print "Test 1"
    mInput = []
    mInput.append([1,2,3,4,5,6])
    mInput.append([1,0,3,4,5,6])
    mInput.append([1,2,3,4,0,6])
    mInput.append([1,2,3,4,5,6])
    print "Input: "
    printMatrix(mInput)
    
    mOutput = zeroOut(mInput)
    print "Output:"
    printMatrix(mOutput)

    mExpected = []
    mExpected.append([1,0,3,4,0,6])
    mExpected.append([0,0,0,0,0,0])
    mExpected.append([0,0,0,0,0,0])
    mExpected.append([1,0,3,4,0,6])
    print "Expected: "
    printMatrix(mExpected)
    
    if mOutput == mExpected:
        return True
    
    return False

assert test1()











