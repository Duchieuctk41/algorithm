def sumFraction():
    num = int(input('Nhập số muốn tính: '))
    result = 0
    for n in range(1,num+1):
        denominator = n + ((n+2)/10)
        result = result + 1/ denominator
        print(denominator)
    return result

A = sumFraction()
print(A)

# A = 1/1.3 + 1/1.4 + 1/1.5 + 1/n.(n+2)