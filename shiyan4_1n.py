with open('1.txt','r+',encoding='utf-8') as f:
    a=f.read()
    w=a.upper()
    f.close()
with open('jyp.txt','w+',encoding='utf-8') as f:
    f.write(w)
    f.close()

