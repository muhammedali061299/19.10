#değer (parametre,arguman)alan fonksiyonlar
#Bu fonksiyonlar değerleri alır ve bunlarla birşeyler yapar

def topla (s1=0,s2=0,s3=0,s4=0) :  #Default parametre
    toplam=s1+s2+s3+s4
    return toplam 
 
print(topla(3,4))
print(topla(3,4,85))
print(topla())