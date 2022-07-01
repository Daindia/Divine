import random

print(input('One word answers required. Answers are case sensetive. Press Ennter to start'))
fhandle = open('HangMan Question.txt')
Lst = list()
for lst in fhandle:
    lst = lst.strip()
    Lst.append(lst)
Qn = random.choice(Lst)
print(Qn)
index = Lst.index(Qn)
Answer = ['Python', 'Byte', 'Adware', 'Latency', 'Blackhat']
Ind = Answer[index]
Length = len(Ind)
Letter = list()
Length_U = len(Letter)
x = Length
while Length >= Length_U and x > 0:
    ans = input('Enter a letter: ')
    if ans in Ind:
        print('Correct')
        Letter = Letter.append(ans)
    else:
        x -= 1
        print('Incorrect!')
if Length == Length_U:
    print(Ind, '. You survived')
else:
    print(Ind, 'was the answer')
    print('You got hanged, man!')
