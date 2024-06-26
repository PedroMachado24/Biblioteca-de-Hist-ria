usuarioEsenha = {}
documentos = {}
autores = {}

def carregar_dados():
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                usuario, senha = line.strip().split(":")
                usuarioEsenha[usuario] = senha
    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

    try:
        with open("documentos.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                titulo = parts[0]
                detalhes = {
                    'autor': parts[1], 'ano_producao': parts[2], 'tema': parts[3],
                    'contexto_historico': parts[4], 'descricao': parts[5],
                    'localizacao': parts[6]
                }
                documentos[titulo] = detalhes
    except FileNotFoundError:
        print("Arquivo de documentos não encontrado.")

    try:
        with open("autores.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                nome = parts[0]
                autores[nome] = {
                    'nascimento': parts[1], 'biografia': parts[2],
                    'areas_pesquisa': parts[3].split(',')
                }
    except FileNotFoundError:
        print("Arquivo de autores não encontrado.")

def gerenciar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")
    usuarioEsenha[nome_usuario] = senha
    print("Usuário", nome_usuario, "registrado com sucesso!")

def cadastrar_documento():
    titulo = input("Digite o título do documento: ")
    autor = input("Digite o nome do autor: ")
    ano = input("Digite o ano de produção: ")
    tema = input("Digite o tema: ")
    contexto_historico = input("Digite o contexto histórico: ")
    descricao = input("Digite a descrição: ")
    localizacao = input("Digite a localização na biblioteca: ")
    
    documentos[titulo] = {
        'autor': autor, 'ano_producao': ano, 'tema': tema,
        'contexto_historico': contexto_historico, 'descricao': descricao,
        'localizacao': localizacao
    }
    print("Documento registrado com sucesso!")

def cadastrar_autor():
    nome = input("Digite o nome do autor: ")
    nascimento = input("Digite a data de nascimento: ")
    biografia = input("Digite a biografia: ")
    areas_pesquisa = input("Digite as áreas de pesquisa associadas: ")
    
    autores[nome] = {
        'nascimento': nascimento, 'biografia': biografia,
        'areas_pesquisa': areas_pesquisa.split(', ')
    }
    print("Autor registrado com sucesso!")

def listar_documentos_ordenados():
    documentos_ordenados = sorted(documentos.items(), key=lambda x: x[1]['ano_producao'])
    for titulo, detalhes in documentos_ordenados:
        print(f"{titulo}: {detalhes}")

def salvar_dados():
    with open("usuarios.txt", "w") as file:
        for usuario, senha in usuarioEsenha.items():
            file.write(f"{usuario}:{senha}\n")

    with open("documentos.txt", "w") as file:
        for titulo, detalhes in documentos.items():
            file.write(f"{titulo}:{detalhes['autor']}:{detalhes['ano_producao']}:{detalhes['tema']}:{detalhes['contexto_historico']}:{detalhes['descricao']}:{detalhes['localizacao']}\n")

    with open("autores.txt", "w") as file:
        for nome, info in autores.items():
            areas = ','.join(info['areas_pesquisa'])
            file.write(f"{nome}:{info['nascimento']}:{info['biografia']}:{areas}\n")

def main():
    print("Bem-vindo ao Sistema de Gestão da Biblioteca de História!")
    print("Aqui você pode gerenciar usuários, cadastrar documentos históricos e autores,")
    print("e visualizar documentos ordenados por ano de produção.")
    print("Carregando dados...")

    carregar_dados()

    while True:
        print("\n*** Menu ***")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Cadastrar documento")
        print("4. Cadastrar autor")
        print("5. Listar documentos ordenados por ano")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerenciar_usuario()
        elif opcao == "2":
            print("Não implementado.")
        elif opcao == "3":
            cadastrar_documento()
        elif opcao == "4":
            cadastrar_autor()
        elif opcao == "5":
            listar_documentos_ordenados()
        elif opcao == "6":
            salvar_dados()
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()