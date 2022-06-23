fhandle = input('Enter fileName: ')
fh = open(fhandle)
Fh = ''.join(fh)
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Len = len(alphabets)

for key in range(Len):
    translated = ''
    for x in Fh:
        Xi = x.upper()
        if Xi in alphabets:
            n = alphabets.index(Xi)
            n -= key
            if n < 0:
                n += Len
                translated += alphabets[n]

            else:
                translated += alphabets[n]
        else:
            translated += Xi

    print('Key #', key, ': ', translated, sep='')
