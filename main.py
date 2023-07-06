#DESAFIO PWC#
#DESAFIO NUÚMERO 1: Reverter as ordens das palavras nas frases mantendo a ordem das palavras.#
frasedesafio1 = input("Digite a frase aqui:")
reverter1 = " ".join(reversed(frasedesafio1.split()))

print("A frase reversa fica assim: ", reverter1)
#No primeiro desafio ultilizei as extensões [.join(), reversed() e .split()]#
#A extensão .split() divide a frase digitada em palavras individuais, o reversed() inverte a ordem das plavras#
#E o .join() une novamente as palavras deixando pronto para exibição no print()#
