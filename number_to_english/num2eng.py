
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def n2e(num):
    if num < 100:
        return twodigit(num)
        
    if num < 1000:
        return threedigit(num)

    if num < 1000000:
        return sixdigit(num)
 
def sixdigit(num):
    v = num / 1000
    r = num % 1000
    if v > 0:
        return threedigit(v) + " thousand " + threedigit(r)
    else:
        return threedigit(r)

def threedigit(num):
    v = num / 100
    r = num % 100 
    if v > 0:
        return numbers[v] + " hundred " + twodigit(r)
    else:
        return twodigit(r)
    
def twodigit(num):
    if num < 10:
        return numbers[num]
        
    v = num / 10
    r = num % 10
    if v == 1:
        return teens[r]
    
    if v < 10:
        return tens[v] + " " + numbers[r]


assert n2e(4) == "four"

assert n2e(10) == "ten"

assert n2e(14) == "fourteen"

assert n2e(22) == "twenty two"

assert n2e(65) == "sixty five"

assert n2e(99) == "ninety nine"

assert n2e(101) == "one hundred one"

assert n2e(110) == "one hundred ten"

assert n2e(523) == "five hundred twenty three"

assert n2e(1023) == "one thousand twenty three"

assert n2e(5056) == "five thousand fifty six"

assert n2e(9199) == "nine thousand one hundred ninety nine"

assert n2e(73910) == "seventy three thousand nine hundred ten"

assert n2e(999999) == "nine hundred ninety nine thousand nine hundred ninety nine"

#inputs = map(int, raw_input().strip())
#k = inputs[0]
#print k
#print  n2e(k)
