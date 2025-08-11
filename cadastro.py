def formatar_nome(nome):
    return nome.strip().title()

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite e categoria do produto ")
    return (formatar_nome(nome), preco, categoria)

def salva_produto(produto):
    with open("produtos.txt", "a" , encoding="utf-8") as arquivo:
        linha =f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.wirte(linha)
def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8)as arquivo
