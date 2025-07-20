import requests
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

def cadastrar_quimioterapico():
    produto = {
        "nome": "Antibiótico Canino",
        "fabricante": "VetPharma",
        "preco": 49.90,
        "quantidade": 10,
        "principio_ativo": "Amoxicilina"
    }
    response = requests.post(f"{BASE_URL}/produtos/quimioterapico", json=produto)
    print(response.json())

def cadastrar_vacina_perecivel():
    produto = {
        "nome": "Vacina Raiva",
        "fabricante": "PetSaúde",
        "preco": 30.0,
        "quantidade": 50,
        "tipo_biologico": "vacina",
        "validade": str(date(2025, 12, 31))
    }
    response = requests.post(f"{BASE_URL}/produtos/vacina_perecivel", json=produto)
    print(response.json())

def listar_todos():
    response = requests.get(f"{BASE_URL}/produtos/")
    produtos = response.json()
    print("\n Todos os produtos")
    for p in produtos:
        print(p)

def listar_pereciveis():
    response = requests.get(f"{BASE_URL}/produtos/pereciveis")
    pereciveis = response.json()
    print("\n --- Produtos pereciveis ---")
    for p in pereciveis:
        print(p)

def quantidade_total():
    response = requests.get(f"{BASE_URL}/estoque/quantidade_total")
    print("\n--- Estoque total ---")
    print(response.json())

def menu():
    while True:
        print("\n=== CLIENTE API PRODUTOS VETERINÁRIOS ===")
        print("1 - Cadastrar Quimioterápico")
        print("2 - Cadastrar Vacina Perecível")
        print("3 - Listar todos os produtos")
        print("4 - Listar perecíveis")
        print("5 - Ver quantidade total")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_quimioterapico()
        elif opcao == "2":
            cadastrar_vacina_perecivel()
        elif opcao == "3":
            listar_todos()
        elif opcao == "4":
            listar_pereciveis()
        elif opcao == "5":
            quantidade_total()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()