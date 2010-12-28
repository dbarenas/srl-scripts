import sys
import nltk
import re
#1 [NP-SUJ-A0 DT_the NNP_Administrator] [VP VBZ_selects] [NP-OBJ-A1 DT_the NN_option NN_OPT001]
# (A1* the DT B-NP
# Intro files
filef="semrol2.out"
fileSem = open(filef,"r");
frase=[]
cont=0
for linea in fileSem.readlines():
        Aux=linea.strip("\n")
        Aux2=Aux.split("|")
	cont = cont+1
	AN=Aux2[9].strip("*")
	AB=AN.strip("(")
	AC=AB.strip(")")
	
	frase.append(AC)
	frase.append(Aux2[0]+"_"+Aux2[1])
#	frase.append(Aux2[7])


#print frase

rol=[]
pos=[]
for i in range(0,len(frase),2):
	rol.append(frase[i])
	pos.append(frase[i+1])

new=[]
aux=0
for i in range(len(rol)):
	if rol[i] == '':
		rol[i]=rol[i-1]
		new.append(rol[i])
	else:
		new.append(rol[i])
stak=0
frq=0
frql=[]
final=[]
for n in range(len(new)):
	if new[n] != aux:
		aux=new[n]
		frq=new.count(new[n])
		#print frq,
		print "[",
		print new[n],
		if stak > frq:
			frq=stak+frq
		for r in range(stak,frq):
			print pos[r],
			stak=frq
		print "]",

