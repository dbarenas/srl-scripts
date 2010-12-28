import re
nom_fich_roles="CU-Ing-rol.txt"
frol=open(nom_fich_roles,"r")
linea=frol.readline()
while linea:
  l=re.findall("VB",linea)
  l=l+re.findall("AUX",linea)
  # print l
  if len(l)>1:
    print linea,
  linea=frol.readline()
frol.close()
