"""
Crie um jogo em Python onde o computador vai sortear um número de 1 até 100.
Em seguida, você vai tentar adivinhar que número foi esse.

A cada tentativa, ele vai te dizer se seu palpite foi alto, baixo ou se você acertou.
Quando acertar, deve mostrar quantas tentativas você fez até acertar.
"""

from mdoules import functions


print("Py Game: What's the Number?")

functions.sortear()

functions.inputNumber()
