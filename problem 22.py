f = open('p022_names.txt','r')
L=[]
for ligne in f:
    L+=(ligne.split(','))
J=sorted(L)
print(J)

c = ['A','B','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


s=0

for k in range(len(c)):
    for g in J:
        for h in g:
            if h==c[k]:
                s+=k
    


