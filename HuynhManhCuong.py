name = "HuynhManhCuong"
stt = 5

result = ''

for i in range(len(name)):
    char = name[i]
    if "A" <= char <= "Z":
        result = result + chr((ord(char) + stt - 65) % 26 + 65)
    else: 
        result = result + chr((ord(char) + stt - 97) % 26 + 97)
        
print(result)