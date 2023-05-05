s = str(input("Please enter word or sentence: "))
def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "Upper case letters : %s,Lower case letters : %s" % (u,l))

up_low(s)