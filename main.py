#DESAFIO PWC#
#DESAFIO NÚMERO 1: Reverter as ordens das palavras nas frases mantendo a ordem das palavras.#
print("Desafio #1: Reverter a string mantendo a ordem das palavras..")
frasedesafio1 = input("Digite a frase aqui:")
reverter1 = " ".join(reversed(frasedesafio1.split()))

print("A frase reversa fica assim: ", reverter1)
#No primeiro desafio ultilizei as extensões [.join() e .split()] e a função reversed()#
#A extensão .split() divide a frase digitada em palavras individuais, o reversed() inverte a ordem das plavras#
#E o .join() une novamente as palavras deixando pronto para exibição no print()#

print(" ")

#DESAFIO NÚMERO 2: REMOVER TODOS CARACTÉRES DUPLICADOS DA STRING#
print("Desafio #2: Remover caractéres duplicados da string..")

frase2 = input("Digite aqui:")
repetidos = set()
frase_formatada = ""
#aqui começei criando a variavel "repetidos" para armazenar caracteres duplicados#
for duplicado in frase2:
  if duplicado not in repetidos:
    repetidos.add(duplicado)
    frase_formatada += duplicado
#Logo em seguida o laço de repetição para percorrer cada caracter da frase original para verificar duplicatas#
#Se o caracter não estiver em "repetidos", adicionamos ele e em seguida concatenamos para a "frase_formatada"#
print("Frase formatada:", frase_formatada)
print(" ")

