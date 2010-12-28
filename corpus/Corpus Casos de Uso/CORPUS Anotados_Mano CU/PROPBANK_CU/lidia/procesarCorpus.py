nom_fich="CU-Ing-Todo.txt"
nom_fich_frases="CU-Ing-frases.txt"
nom_fich_cat="CU-Ing-cat.txt"
nom_fich_roles="CU-Ing-rol.txt"
categorias=["OPT","MSG","STA"]
fent=open(nom_fich,"r")
ffra=open(nom_fich_frases,"w")
fcat=open(nom_fich_cat,"w")
frol=open(nom_fich_roles,"w")
linea=fent.readline()
lf=lc=lr=1
while linea:
  if 'NIL' in linea:
    ffra.write(linea)
    fcat.write(linea)
    frol.write(linea)
    #print "NIL->" + linea
  elif '[' in linea:
    frol.write(str(lr) + " " + linea)
    lr+=1
    #print "etiquetado->" + linea
  elif '\"' in linea:
    ffra.write(str(lf) + " " + linea)
    lf+=1
    #print "comillas->" + linea
  elif (categorias[0] in linea or categorias[1] in linea or categorias[2] in linea) and not ('[' in linea):
    fcat.write(str(lc) + " " + linea)
    lc+=1
    #print "categoria->" + linea
  else:
    if linea!="\n": #len(linea) > 0:
      ffra.write(str(lf) + " " + linea)
      fcat.write(str(lc) + " " + linea)
      lf+=1
      lc+=1     
  linea=fent.readline()
  print linea

fent.close()
ffra.close()
fcat.close()
frol.close()
