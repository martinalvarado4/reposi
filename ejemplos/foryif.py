
import string
key="vojgb"
encriptado="hrkgnisaxjhtqmyl"
def cuanto(key , encripted):
    largo=len(string.ascii_lowercase)
    listakey=[]
    k=list(key)
    e=list(encripted)
    i=0
    while len(listakey)<len(encripted):
        b=len(encripted)//len(k)
        if i < b:
            for m in range(0,len(k)):
                listakey.append(k[m])
            i=i+1
        else :
            c=len(encripted)%len(k)
            for j in range(0,c):
                listakey.append(k[j])
    return listakey
c=cuanto(key,encriptado)
d=str("".join(c))
def valor(lista):
    lista2=[]
    i=0
    largo=len(lista)
    while i<len(lista):
        for j in range(0,len(string.ascii_lowercase)):
            if lista[i]==string.ascii_lowercase[j]:
                lista2.append(j)
        else:
            i=i
        i=i+1
    return lista2
e=valor(d)
f=valor(encriptado)
print(e)
print(f)
def desncriptado(key,encriptado):
    listaf=[]
    for i in range(0,len(encriptado)):
        if (encriptado[i]-key[i])<0:
            listaf.append(string.ascii_lowercase[encriptado[i]-key[i]+26])
        else:
            listaf.append(string.ascii_lowercase[encriptado[i]-key[i]])
    return listaf
print("".join(desncriptado(e,f)))

