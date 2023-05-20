def SumaKwCyfr(n):
    suma = 0
    while n > 0:
        cyfra = n % 10
        suma += cyfra ** 2
        n //= 10
    return suma
print(SumaKwCyfr(123))

def CzyCiekawa(n):
    while n != 1 and n != 4:
        n = SumaKwCyfr(n)
    if n == 1:
        return False
    else:
        return True

print(CzyCiekawa(82))