# This is a sample Python script.
from aulas.funcoes import funcoes
from aulas.sequencias import sequencias


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    escolha = int(input('Informe a aula do curso: (1) funções | (2) sequências\n'))
    match(escolha):
        case 1:
            funcoes()
        case 2:
            sequencias()
        case other:
            print("Escolha inválida.")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
