alunos = []


def ler_nota(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def obter_situacao(media):
    if media >= 7:
        return "APROVADO!"
    if media >= 5:
        return "RECUPERAÇÃO!"
    return "REPROVADO!"


def cadastrar_aluno():
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if nome:
            break
        print("O nome não pode ficar vazio.")

    nota1 = ler_nota("Digite a primeira nota: ")
    nota2 = ler_nota("Digite a segunda nota: ")

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- LISTA DE ALUNOS ---")
    for aluno in alunos:
        media = calcular_media(aluno["nota1"], aluno["nota2"])
        print(f"Nome: {aluno['nome']}")
        print(f"Primeira nota: {aluno['nota1']:.2f}")
        print(f"Segunda nota: {aluno['nota2']:.2f}")
        print(f"Média: {media:.2f}")
        print("----------------------")


def verificar_situacao():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome do aluno: ").strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            media = calcular_media(aluno["nota1"], aluno["nota2"])
            situacao = obter_situacao(media)

            print(f"\nAluno: {aluno['nome']}")
            print(f"Média: {media:.2f}")
            print(f"Situação: {situacao}")
            return

    print("Aluno não encontrado.")


def menu():
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Verificar situação do aluno")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            verificar_situacao()
        elif opcao == "4":
            print("Obrigado por utilizar o sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
                        
                     

                    
                
                                            
