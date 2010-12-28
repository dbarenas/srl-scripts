import sys
import nltk

# Intro files
frase="corpus/frases.txt"
tagged="corpus/sav.tagged"
parsed="corpus/sav.parsed"
semantic="corpus/sav.semantic"

fileFra = open(frase,"r");
fileTag = open(tagged,"r");
filePar = open(parsed,"r");
fileSem = open(semantic,"r");
count=0
A=[]
Aux=[]

for linea in fileFra.readlines():
        Aux=linea.strip("\n")
        Aux2=Aux.strip(" ")
        frase=Aux2.split()	
	frase.append(".")
#print frase

for linea in fileTag.readlines():
	Aux=linea.strip("\n")
	Aux2=Aux.strip(" ")
	morpho=Aux2.split()
#print morpho
#print "----"
nmorpho=[]
for i in range(0,len(morpho),2):
	nmorpho.append(morpho[i]+"_"+morpho[i-1])
#print nmorpho[1:]
pos=nmorpho[1:]
#print "----"

for linea in filePar.readlines():
	Aux=linea.strip("\n")
        Aux2=Aux.strip(",")
        Aux3=Aux2.split()

parse=[]
for i in range(2,len(Aux3)):
	parse.append(Aux3[i])
#print parse

seman=[]
for linea in fileSem.readlines():
	Aux=linea.strip("\n")
        Aux2=Aux.strip("--")
        Aux3=Aux2.split()
	seman.append(Aux3)

nseman=[]
for i in range(len(seman)):
	for j in range(len(seman[i])):
		nseman.append(seman[i][j])
#print nseman
ind=[]
roles=[]
for i in range(0,len(nseman),2):
	ind.append(nseman[i+1])	
	roles.append(nseman[i])
#print ind

#tengo frase, morpho, parse, nseman,ind

testf=frase[1:]
#print testf
#print ":.:.::.::.::.::.::.::.::.::.::.::.:"
nm=0
nmaux=0
for n in range(len(ind)): # [0,1,2]
	print "[",
	print roles[n],
	nm=int(ind[n])
	
	if nmaux > nm or nmaux == nm:
		nou=nmaux+int(ind[n])
		#nmaux=int(ind[n])
		for m in range(nmaux,nou):
			if m != 0:
				print pos[m],
			else:
				break
		nmaux=nou
	else:
		for m in range(nmaux,nm):
			nmaux=int(ind[n])
	                print pos[m],
	print "]",
