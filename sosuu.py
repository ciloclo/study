import time
ST=time.time()
n=10000000
q=[1]
a=0
for i in range(1,n+1):
    for p in q:
        if p==q[-1]:
            if i==1:
                break#1の時
            if p==1:
                q.append(i)
                break#2の時
            if i%p==0:
                break
            q.append(i)
            break#3,5の時
        if p==1:
            continue
        if i%p==0:
            break
        #軽量化１
        a=i/p
        if p>a:
            q.append(i)
            break
del q[0]
ET=time.time()
print(ET-ST)
