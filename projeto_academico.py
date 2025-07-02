import json

def carregar_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_cadastro_json(lista_cadastro, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        json.dump(lista_cadastro, f, indent=4)

def titulo(texto):
    tamanho = len(texto) + 10
    print('-=' * (tamanho // 2))
    print(f'{texto:^{tamanho}}')
    print('-=' * (tamanho // 2))

def mostrar_menu_principal():
    titulo('SISTEMA DE GESTÃO ACADÊMICA')
    print("\nMenu Principal:")
    print("1 - Estudantes")
    print("2 - Disciplinas")
    print("3 - Professores")
    print("4 - Turmas")
    print("5 - Matrículas")
    print("6 - Sair")
    return int(input("\nEscolha uma opção do menu principal: "))

def mostrar_menu_operacoes():
    titulo('MENU DE OPERAÇÕES')
    print("\n1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Voltar ao menu principal")
    return int(input("\nEscolha uma operação: "))

def incluir_cadastro_turmas(lista_qualquer, nome_arquivo):
    codigo = int(input('Digite o código da turma: '))
    codigo_prof = int(input('Digite o código do professor: '))
    codigo_disc = int(input('Digite o código da disciplina: '))
    dicionario_turmas = {
        'codigo': codigo,
        'codigo_professor': codigo_prof,
        'codigo_disc': codigo_disc,
    }
    lista_qualquer.append(dicionario_turmas)
    salvar_cadastro_json(lista_qualquer, nome_arquivo)

def incluir_cadastro_disciplinas(lista_qualquer, nome_arquivo):
    codigo = int(input("Digite o código da disciplina: "))
    nome = input("Digite o nome da disciplina: ")
    dicionario_d = {
        "codigo": codigo,
        "nome": nome,
    }
    lista_qualquer.append(dicionario_d)
    salvar_cadastro_json(lista_qualquer, nome_arquivo)

def incluir_cadastro_matricula(lista_qualquer, nome_arquivo):
    codigo_turma = int(input('Digite o código de turma: '))
    codigo_estudante = int(input('Digite o código do estudante: '))

    dicionario_turmas = {
        'codigo': codigo_turma,
        'codigo_estudante': codigo_estudante,
    }
    lista_qualquer.append(dicionario_turmas)
    salvar_cadastro_json(lista_qualquer, nome_arquivo)
def incluir_cadastro_aluno_e_professor(lista_qualquer, nome_arquivo):
    print("\nVocê escolheu: Incluir")
    codigo_cadastro = int(input("Insira o código: "))
    nome_cadastro = input("Insira o nome: ")
    cpf_cadastro = input("Insira o CPF: ")

    dicionario_aluno_e_professor = {
        "codigo": codigo_cadastro,
        "nome": nome_cadastro,
        "cpf": cpf_cadastro
    }
 ##
    lista_qualquer.append(dicionario_aluno_e_professor)
    salvar_cadastro_json(lista_qualquer, nome_arquivo)
    print(f"Você incluiu {nome_cadastro} na lista!")

def listar_cadastros(lista_qualquer):
    if not lista_qualquer:
        print("Não há cadastros na lista!\n")
    else:
        print("A lista de cadastros é:\n")
        for cadastro in lista_qualquer:
            if 'nome' in cadastro:

                print(f"Código: {cadastro['codigo']}, Nome: {cadastro['nome']}", end='')
                if 'cpf' in cadastro:
                    print(f", CPF: {cadastro['cpf']}")
                else:
                    print()
            elif 'codigo_professor' in cadastro and 'codigo_disc' in cadastro:

                print(f"Código da turma: {cadastro['codigo']}, Código do professor: {cadastro['codigo_professor']}, Código da disciplina: {cadastro['codigo_disc']}")
            elif 'codigo_estudante' in cadastro:

                print(f"Código da matrícula (turma): {cadastro['codigo']}, Código do estudante: {cadastro['codigo_estudante']}")
            else:

                print(f"Cadastro inválido ou incompleto: {cadastro}")



def excluir_cadastro(lista_qualquer, nome_arquivo):
    cadastro_a_ser_excluido = int(input("Digite o código do cadastro a ser excluído: "))
    for cadastro in lista_qualquer:
        if cadastro_a_ser_excluido == cadastro["codigo"]:
            lista_qualquer.remove(cadastro)
            salvar_cadastro_json(lista_qualquer, nome_arquivo)
            print("Cadastro removido com sucesso!")
            return
    print("O código informado não corresponde a nenhum cadastro.")

def editar_cadastro(lista_qualquer, nome_arquivo):
    cadastro_a_ser_editado = int(input("Digite o código do cadastro a ser editado: "))
    for cadastro in lista_qualquer:
        if cadastro_a_ser_editado == cadastro["codigo"]:
            print("\nCadastro encontrado. Editando dados...")
            cadastro["codigo"] = int(input("Digite o novo código: "))

            if "nome" in cadastro:
                cadastro["nome"] = input("Digite o novo nome: ")
                if "cpf" in cadastro:
                    cadastro["cpf"] = input("Digite o novo CPF: ")
            elif "codigo_professor" in cadastro and "codigo_disc" in cadastro:
                cadastro["codigo_professor"] = int(input("Digite o novo código do professor: "))
                cadastro["codigo_disc"] = int(input("Digite o novo código da disciplina: "))
            elif "codigo_estudante" in cadastro:
                cadastro["codigo_estudante"] = int(input("Digite o novo código do estudante: "))

            salvar_cadastro_json(lista_qualquer, nome_arquivo)
            print("Cadastro atualizado com sucesso!\n")
            return
    print("O código informado não corresponde a nenhum cadastro.\n")

# Loop principal
while True:
    while True:
        opcao_principal = mostrar_menu_principal()
        if opcao_principal == 1:
            print("\nVocê escolheu: Estudantes")
            nome_arquivo = 'estudantes.json'
            Lista_geral = carregar_arquivo_json(nome_arquivo)
            break

        elif opcao_principal == 2:
            print("\nVocê escolheu: Disciplinas")
            nome_arquivo = 'disciplinas.json'
            Lista_geral = carregar_arquivo_json(nome_arquivo)
            break

        elif opcao_principal == 3:
            print("\nVocê escolheu: Professores")
            nome_arquivo = 'professores.json'
            Lista_geral = carregar_arquivo_json(nome_arquivo)
            break

        elif opcao_principal == 4:
            print("\nVocê escolheu: Turmas")
            nome_arquivo = 'turmas.json'
            Lista_geral = carregar_arquivo_json(nome_arquivo)
            break

        elif opcao_principal == 5:
            print("\nVocê escolheu: Matrículas")
            nome_arquivo = 'matriculas.json'
            Lista_geral = carregar_arquivo_json(nome_arquivo)
            break

        elif opcao_principal == 6:
            print("\nVocê escolheu: Sair")
            exit()

        else:
            print('Insira uma opção válida!')

    while True:
        opcao_operacao = mostrar_menu_operacoes()

        if opcao_operacao == 1:
            if opcao_principal in [1, 3]:
                incluir_cadastro_aluno_e_professor(Lista_geral, nome_arquivo)
            elif opcao_principal == 2:
                incluir_cadastro_disciplinas(Lista_geral, nome_arquivo)
            elif opcao_principal == 4:
                incluir_cadastro_turmas(Lista_geral, nome_arquivo)
            elif opcao_principal == 5:
                incluir_cadastro_matricula(Lista_geral, nome_arquivo)

        elif opcao_operacao == 2:
            listar_cadastros(Lista_geral)

        elif opcao_operacao == 3:
            listar_cadastros(Lista_geral)
            editar_cadastro(Lista_geral, nome_arquivo)

        elif opcao_operacao == 4:
            listar_cadastros(Lista_geral)
            excluir_cadastro(Lista_geral, nome_arquivo)

        elif opcao_operacao == 5:
            print("\nVoltando ao menu principal...")
            break

        else:
            print("\nOpção inválida.")
