import string


class Validador:
    # Construtor
    def __init__(self,senha):
        self.senha = senha



    def validadorDeSenha(self):

        if len(self.senha) == 0:
            return 0
        else:
            letter = self.has_letters(self.senha)
            digit = self.has_digit(self.senha)
            punctuation = self.has_punctuation(self.senha)

            if letter and digit and punctuation:
                print("Senha Valida")
            else:
                print("Senha Invalida")




    def  has_letters(self,senha: str) -> bool:
        letters = string.ascii_letters
        # Se tiver alguma letra a função retorna True
        return any([char in letters for char in senha])

    def has_digit(self,senha: str) -> bool:
        return any(char.isdigit() for char in senha)

    def has_punctuation(self,senha: str) -> bool:
        punctuation = string.punctuation
        return any(char in punctuation for char in senha)


def main():
    nome1 = Validador("!Gustta37280")
    nome2 = Validador("Gustta37280")

    nome1.validadorDeSenha()
    nome2.validadorDeSenha()


if __name__ == "__main__":
    main()