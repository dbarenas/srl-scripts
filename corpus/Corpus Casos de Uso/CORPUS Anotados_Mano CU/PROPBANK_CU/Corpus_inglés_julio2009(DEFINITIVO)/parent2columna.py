def saca_rol(tok):
# devuelve el rol dentro del token tok
  ltok=tok.split("-")
  if len(ltok) > 2:
    return ltok[2]
  else: 
    return '*'
    

def saca_pal(tok):
# devuelve la palabra dentro del token tok
  ltok=tok.split("_")
  # print "saca_pal" + tok + "->" + ltok[1]
  return ltok[1]

def imprime(pal,nivel,rol):
# escribe la palabra en la columna 0, tantas columnas con * como nivel, rol en la columna nivel
# el rol puede ser (* (Ax * *) (Ax)
# falta tratar cuando cierran dos ]] en el mismo token

  print pal,
  while nivel>0:
    print '*',
    print ' ',
    nivel-=1
  print rol

################
def tratar_linea(l):
  l=l[0:len(l)-1] # quitar el fin de linea
  ltoken=l.split(" ")
  del ltoken[0]
  nivel=-1
  c_ab=''
  rol='*'
  c_ce=')'
  for tok in ltoken:
    # print "###   " + tok
    if '[' in tok:
      rol=saca_rol(tok)
      nivel+=1
      c_ab='('
    elif ']' in tok:
      # print "en ]" + tok + " " + tok[0:len(tok)-1]
      c=c_ab+rol
      niv_aux=nivel
      while ']' in tok:
        tok=tok[0:len(tok)-1]
        c=c+c_ce
        niv_aux-=1
      pal=saca_pal(tok)
      imprime(pal,nivel,c)
      nivel=niv_aux
    else:
      pal=saca_pal(tok)
      imprime(pal,nivel,c_ab +rol)
      nivel-=1
      c_ab=''
      rol='*'

################

frol=open("CU-Ing-rol.txt","r")

linea=frol.readline()
while linea:
  if not ('NIL' in linea):
    tratar_linea(linea)
    # pon_punto()
    print
  linea=frol.readline()

frol.close();
  
  

