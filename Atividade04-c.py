while True:
    senha = input("Digite sua senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado")
        break

    if len(senha) < 8:
        print("Senha fraca! Ela deve ter pelo menoos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca! Ela deve conter pelo menos um número.")
        continue


    print("Senha forte cadastrada com sucesso!")
    break