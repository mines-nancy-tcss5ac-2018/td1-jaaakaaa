f = open('p022_names.txt','r')
L=[]
for ligne in f:
    L+=(ligne.split(','))
J=sorted(L)
print(J)


def Somme_des_lettres_du_prenom(L):
    s=0
    c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for g in range(len(L)):         #On somme sur le nombre de lettre dans le mot
        for k in range(len(c)):     #On parcourt l'alphabet
            if L[g]==c[k]:          #On compare
                s+=k+1              #Si les lettres sont égales alors l'indices k correspond à la position dans l'alphabet
            else :                  #Cette ligne sert à éviter les problèmes avec les " contenue dans le fichier
                pass
    return s

    
assert Somme_des_lettres_du_prenom("COLIN")==53

def solve():
    p=0
    for m in range(len(J)):
        p+=(m+1)*Somme_des_lettres_du_prenom(J[m])
    return p

print(solve())
