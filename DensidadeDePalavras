import string

texto = input("cole aqui o texto a ser analisado: ")
palavra_chave = input("digite aqui a palavra a ser contabilizada: ")

pontuacao = string.punctuation
for n in pontuacao:
    texto = texto.replace(n, "")
    
texto_lista = texto.split()

texto_otimizado = []

for i in texto_lista:
    texto_otimizado.append(i.lower())

contador = 0

for i in texto_otimizado:
    if (i == palavra_chave):
        contador += 1
        
densidade = contador / len(texto_otimizado)
        
print("A palavra " + palavra_chave + " ocorre " + str(contador) + " vezes no texto inserido e a sua densidade é de " + str(round(densidade,2)))
