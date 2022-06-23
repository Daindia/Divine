fhandle = open('Emails.txt')
for hd in fhandle:
    ind = hd.index('@')
    left = ind
    right = ind + 1
    print('Individual URL:', hd[right:])
    print('Host:', hd[:left])