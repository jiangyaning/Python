import os
with open('2.txt','r+',encoding='utf-8') as f:
    a=f.readline()
    b=''
    for i in range(len(a)):
        if a[i].isalpha():
            if a[i] in 'YZyz':
                b+=chr(ord(a[i])-24)
            else:
                b+=chr(ord(a[i])+2)
        else:
            b+=a[i]
    f.close()
with open('2.txt','a+',encoding='utf-8') as f:
    f.write(b)
    f.seek(0,0)
    print(f.read())
    f.close()
