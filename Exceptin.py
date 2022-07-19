# global n1
# try:
#     n1=int(input("N1: "))
# except:
#     n1=0
# n2=int(input("N2: "))

# print("{} + {} = {} ".format(n1,n2,n1+n2))

n1=int(input("N1: "))
n2=int(input("N2: "))
mon_fic=open("fic.txt","a")
s=n1+n2
contenu="\n"+str(n1)+"+"+str(n2)+"="+str(s)
contenu=mon_fic.write(contenu)
mon_fic.close()

mon_fic=open("fic.txt","r")
cont=mon_fic.read()
print(cont)
mon_fic.close()