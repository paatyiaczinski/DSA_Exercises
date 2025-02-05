
import random



def game():
    
    print("Bem vindo ao jogo da forca!!")
    print("Adivinhe a palavra abaixo: /n")


    words = ["banana","laranja","cereja","melancia"]
    word = random.choice(words)

    discovered_letters = ["_"  for letter in word]
    chances = 6
    wrong_letters = []

    while chances > 0:
        print(" ".join(discovered_letters))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(wrong_letters))

        attempt = input("\nDigite uma letra: ").lower()

        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    discovered_letters[index] = letter
                index += 1
        else:
            chances -= 1
            wrong_letters.append(attempt)

        if "_" not in discovered_letters:
            print("/nVocê venceu, a palavra era:", word)
            break
    if "_" in discovered_letters:
        print("/nVocê perdeu, a palavra era:",word)

if __name__ == "__main__":
    game()
