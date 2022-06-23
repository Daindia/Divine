Bits = ('')

length = 0
print(length)
while True:
    if length != 32:
        Bits = input('Enter Bits: ')
        length = len(Bits)
    else:
        break

    

Level_A = list(Bits[:8])
Level_B = list(Bits[8:16])
Level_C = list(Bits[16:24])
Level_D = list(Bits[24:])

dec_A = 128
Ip_A = 0 
for x in Level_A:
    if x == '1':
        Ip_A += dec_A
    dec_A = dec_A/2
    
dec_B = 128
Ip_B = 0 
for z in Level_B:
    if z == '1':
        Ip_B += dec_B
    dec_B = dec_B/2        

dec_C = 128
Ip_C = 0 
for i in Level_C:
    if i == '1':
        Ip_C += dec_C
    dec_C = dec_C/2

dec_D = 128
Ip_D = 0 
for a in Level_D:
    if a == '1':
        Ip_D += dec_D
    dec_D = dec_D/2
print('IPv4 Address:')
print(int(Ip_A), '.', int(Ip_B), '.', int(Ip_C), '.', int(Ip_D), sep='')