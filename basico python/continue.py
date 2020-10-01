
texto= "buenas tardes compañeros"

contador = 0

for i in texto:
    
    if i==" ":
        continue
    contador+=1

print("caracteres sin espacio: "+ str(contador))

print("caracteres con espacio:" + str(len(texto)))