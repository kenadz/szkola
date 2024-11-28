mod = 1000000007

def pot(a, b):
if(b == 0):
return 1
if(b % 2 == 0):
pom = pot(a, b / 2)
return (pom * pom) % mod
else:
return a * pot(a, b - 1) % mod
