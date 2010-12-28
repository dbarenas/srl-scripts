import sys
import nltk
file = open(sys.argv[1],"r");

count=0
A=[]
Aux=[]


for linea in file.readlines():
	if linea.find("NIL") == -1: 
		text = nltk.word_tokenize(linea);
		A=nltk.pos_tag(text);
		indice=len(A[1:])
		print indice,A[1:]
