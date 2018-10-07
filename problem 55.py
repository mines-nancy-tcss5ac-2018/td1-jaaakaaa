def numbre_to_list (n):
    l=[]
    k=1
    while n > 0 :
        h=n%(10**k)
        l.append(int(h/10**(k-1)))                  #on met int car sinon on recupere type floatant (question de style uniquement)
        k+=1
        n=n-h
    l.reverse()
    return l

def reverse_number (n):                             #on transforme d'abord le nombre en liste puis on le reconstruit 
    l=numbre_to_list(n)
    j=0
    s=0
    for k in l:
        s+=k*10**j
        j+=1
    return s

assert reverse_number(1234)==(4321)

def palindrome (n) :
    L=numbre_to_list(n)
    A=list(L)
    L.reverse()
    return A==L

assert palindrome(12321)==True

def solve():
    s=0
    for k in range(1,10001):
        y=0
        k=k+reverse_number(k)                       #ligne tres important pour exclure 4994 par exemple
        while y<50 and palindrome(k)==False:        #on ne veut pas que les nombres comme 4994 passent
            y+=1       
            k=k+reverse_number(k)
        if y!=50:                                   #si la boucle while est terminer avant que y=50 alors il y a un palindrome
            s+=1
    return 10000-s                                  #les nombres de lychrel sont les autres

print(solve())