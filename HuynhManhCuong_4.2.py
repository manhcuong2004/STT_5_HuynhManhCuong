def mod(m, e, n):
    result = 1
    while e > 0:
        if e % 2 == 1:
            result = (result * m) % n
        m = (m * m) % n
        e //= 2
    return result

p = 17
q = 23
n = p * q  
z = (p - 1) * (q - 1)  
e = 5

message = "HuynhManhCuong"
ascii = [ord(char) for char in message]

mahoa = [mod(m, e, n) for m in ascii]

print(mahoa)
