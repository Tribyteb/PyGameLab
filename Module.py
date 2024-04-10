
import math as math 

#dir(math)
#help(math)

math.factorial(7)
print(math.floor(5.5))


# from math import floor,ceil (sadece belli functionları kullanmak için)

def factorial(sayi):
    print("Our Function")

    faktoriyel = 1

    if(sayi == 0 or sayi == 1):
        return 1
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        return faktoriyel

print(factorial(3))

