import os

# Palavra secreta
palavra_secreta = "elefante"
letras_adivinhadas = []
tentativas = 6  # Número de tentativas

def mostrar_palavra():
    return ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])

while tentativas > 0:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print("Palavra:", mostrar_palavra())
    print(f"Tentativas restantes: {tentativas}")
    letra = input("Adivinhe uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra.")
    elif letra in palavra_secreta:
        letras_adivinhadas.append(letra)
        print("Boa! Você acertou uma letra.")
    else:
        letras_adivinhadas.append(letra)
        tentativas -= 1
        print("Ops! Essa letra não está na palavra.")

    # Verifica se o jogador ganhou
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
        break
else:
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
