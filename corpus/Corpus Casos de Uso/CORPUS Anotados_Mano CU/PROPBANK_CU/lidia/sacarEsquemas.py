nom_fich_roles="CU-Ing-rol.txt"
corchetes=['[',']']
frol=open(nom_fich_roles,"r")
linea=frol.readline()

while linea:
  res="" 
  c=0
  for i in range(len(linea)):
    if linea[i] in corchetes:
      res+=linea[i]
      c+=1
 # print res
  if c%2 != 0 :
    print linea
  linea=frol.readline()
frol.close()

