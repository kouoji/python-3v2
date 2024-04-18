import os

restaurantes = ["Robalo preto", "Tubarão branco"]

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def finalizar_app():
    mostrar_subtitulo("Finalizando o app\n")

def escolher_opcoes():
    print("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def chamar_nome_do_app():
    print("Restaurante Expressão\n")

def listar_restaurantes():
    print('Listando os Restaurantes')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")
    voltar_ao_menu_principal()

def main():
    escolher_opcoes()
    chamar_nome_do_app()
    try:
        opcao_digitada = int(input("Digite a opção desejada: "))
        if opcao_digitada == 1:
            print("Você escolheu cadastrar restaurante\n")
            cadastrar_novo_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            print("Você escolheu ativar restaurante\n")
        elif opcao_digitada == 4:
            print("Você escolheu sair do aplicativo\n")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

if __name__ == "__main__":
    main()
