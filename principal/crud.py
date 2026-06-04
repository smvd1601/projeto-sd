import os

dados = {}
i=0 

caminho_cadastro = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "dados",
    "cadastro.txt"
)


def carregar_dados():
    global dados

    try:
        with open(caminho_cadastro, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        pet = {}

        for linha in linhas:
            linha = linha.strip()

            if linha.startswith("ID:"):
                id_pet = int(linha.split(":")[1].strip())
                pet = {"ID do pet": id_pet}

            elif linha.startswith("Nome:"):
                pet["Nome"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("Espécie:"):
                pet["Espécie"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("Raça:"):
                pet["Raça"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("Idade:"):
                pet["Idade"] = int(linha.split(":", 1)[1].strip())

            elif linha.startswith("Estado de saúde:"):
                pet["Estado de saúde"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("Data de chegada:"):
                pet["Data de chegada"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("Comportamento:"):
                pet["Comportamento"] = linha.split(":", 1)[1].strip()

            elif linha.startswith("----------------"):
                dados[id_pet] = pet
        
        if pet and "ID do pet" in pet:
            dados[pet["ID do pet"]] = pet

    except FileNotFoundError:
        pass

def carregar_ultimo_id():
    global i
    i = max(dados.keys()) if dados else 0

carregar_dados()

carregar_ultimo_id()

def cadastro():
    global i
    i+=1
    pet = {}

    pet["ID do pet"] = i
    pet["Nome"] = input("Nome do pet: ")
    pet["Espécie"] = input("Espécie do pet: ")
    pet["Raça"] = input("Raça do pet: ")
    pet["Idade"] = int(input("Idade do pet: "))
    pet["Estado de saúde"] = input("Estado de saúde do pet: ")
    pet["Data de chegada"] = input("Data de chegada do pet: ")
    pet["Comportamento"] = input("Comportamento do pet: ")

    dados[i] = pet
    salvar_dados()

def salvar_dados():
    with open(caminho_cadastro, "w", encoding="utf-8") as arquivo:
        for id_pet, pet in dados.items():
            arquivo.write(f"ID: {id_pet}\n")
            arquivo.write(f"Nome: {pet['Nome']}\n")
            arquivo.write(f"Espécie: {pet['Espécie']}\n")
            arquivo.write(f"Raça: {pet['Raça']}\n")
            arquivo.write(f"Idade: {pet['Idade']}\n")
            arquivo.write(f"Estado de saúde: {pet['Estado de saúde']}\n")
            arquivo.write(f"Data de chegada: {pet['Data de chegada']}\n")
            arquivo.write(f"Comportamento: {pet['Comportamento']}\n")
            arquivo.write("-" * 30 + "\n")

def excluir():
    id_excluido = int(input("ID do pet que deseja excluir: "))
    
    if id_excluido not in dados:
        print("ID inválido.")
        return
    else:
        dados.pop(id_excluido)
    salvar_dados()
    print(f"Pet {id_excluido} excluído com sucesso.")

def editar():
    id_editar = int(input("ID do pet que deseja editar: "))
 
    if id_editar not in dados:
        print("ID inválido.")
        return
 
    pet = dados[id_editar]
 
    print("Campos disponíveis: Nome, Espécie, Raça, Idade, Estado de saúde, Data de chegada, Comportamento")
    editar_item = input("Qual item deseja editar? ").strip()
 
    campos = {
        "Nome": str,
        "Espécie": str,
        "Raça": str,
        "Idade": int,
        "Estado de saúde": str,
        "Data de chegada": str,
        "Comportamento": str,
    }
 
    if editar_item not in campos:
        print("Campo inválido.")
        return
 
    novo_valor = input(f"{editar_item} do pet: ").title().strip()
    pet[editar_item] = campos[editar_item](novo_valor)
 
    salvar_dados()
    print(f"Campo '{editar_item}' atualizado com sucesso.")
 
def listar():
    if not dados:
        print("Nenhum pet cadastrado.")
        return

    for id_pet, pet in dados.items():
        print(f"\nID: {id_pet}")
        print(f"Nome: {pet['Nome']}")
        print(f"Espécie: {pet['Espécie']}")
        print(f"Raça: {pet['Raça']}")
        print(f"Idade: {pet['Idade']}")
        print(f"Estado de saúde: {pet['Estado de saúde']}")
        print(f"Data de chegada: {pet['Data de chegada']}")
        print(f"Comportamento: {pet['Comportamento']}")
        print("-" * 30)

def acao():
    print("1 - Cadastrar pet\n2 - Excluir pet\n3 - Editar pet\n4 - Listar pets")
    opcao = int(input("Oque deseja realizar: "))

    if (opcao == 1):
        cadastro()
    
    elif (opcao == 2):
        excluir()
    
    elif (opcao == 3):
        editar()

    elif (opcao == 4):
        listar()
acao()

def repeticao():
     while True:
        repetir = input("Deseja realizar mais algum cadastro ou alteração? ").title()
    
        if (repetir == "Sim" or repetir == "S"):
            os.system('cls' if os.name == 'nt' else 'clear')
            acao()

        elif (repetir == "Não" or repetir == "N" or repetir == "Nao"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Obrigado!")
            break

repeticao()
