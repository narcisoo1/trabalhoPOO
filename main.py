## Main do trabalho
import pessoa
usuarios=[]
funcionarios=[]

op=int(1)

while(op!=0):
    print("Digite a opção desejada:\n1 - Cadastrar usuário\n2 - Cadastrar funcionário\n3 - Cadastrar produto\n4 - Venda de produto\n0 - Sair")
    op=int(input())
    if op == 1:
        nome=input("\nDigite o nome: ")
        cpf=input("Digite o cpf: ")
        endereco=input("Digite o endereço: ")
        telefone=input("Digite seu telefone: ")
        usuarios.append(pessoa.Pessoa(nome,cpf,endereco,telefone))

    if op == 2:
        nome=input("\nDigite o nome: ")
        cpf=input("Digite o cpf: ")
        endereco=input("Digite o endereço: ")
        telefone=input("Digite seu telefone: ")
        login=input("Digite seu login: ")
        senha=input("Digite sua senha: ")
        funcionarios.append(pessoa.Funcionario(nome,cpf,endereco,telefone,login,senha))

    if op == 0:
        print("Obrigado, tenha um bom dia!")
        