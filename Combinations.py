# gcd stands for Greatest Common Denominator
def gcd(a,b):
    if b > a:
        return 1
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def ncr(n,r):
    result = 1
    maximum = max(r,n-r)
    minimum = min(r,n-r)
    numerator = [*range(maximum + 1,n+1)]
    denominator = [*range(2,minimum+1)]
    numerator_index = 0
    while denominator:
        common_divisor = gcd(numerator[numerator_index],denominator[0])
        if  common_divisor != 1:
            numerator[numerator_index] //= common_divisor
            denominator[0] //= common_divisor
            if numerator[numerator_index] == 1:
                del numerator[numerator_index]
                numerator_index = 0
            if denominator[0] == 1:
                del denominator[0]
                numerator_index = 0
        else:
            numerator_index = (numerator_index + 1) % len(numerator)
            continue
    for i in numerator:
        result *= i
    return result


input_number_n = int(input('Please input number of distinct options (n):'))
input_number_r = int(input('Please input number of selections (r):'))
print(ncr(input_number_n,input_number_r))