from time import sleep
import math
f = int(input())
m = int(input())
e = math.sqrt(f)
def delay(f, m, answ, *args):
  sleep(m / 1000)
  return f(*args)
print( "Square root of " + str(f) +  ' after ' +str(m) + ' miliseconds is ' +str(e)) 
