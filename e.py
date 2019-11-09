i=t=s=1
while True:
    t=t*i
    i+=1
    s=s+1/t
    if t>10**6:
        break
print("e的近似值为：",s)