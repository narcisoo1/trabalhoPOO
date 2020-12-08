## Main do trabalho
from pessoa import Pessoa
from funcionario import Funcionario
from cadastroProduto import CadastroProduto
from validacpf import validaCPF

funcionarios=[]
produtos=[]

op=int(1)

while(op!=0):

    print("Digite a opção desejada:")
    print("[1] - Cadastrar funcionário:")
    print("[2] - Logar funcionário:")
    print("[0] - Sair")


    op=int(input())
    
    if op == 1:
        user = input("login: ")
        passwd = input("password: ")

        if(user == "admin" and passwd == "admin"):
            print("\nlogged on\n")

            print("CADASTRO FUNCIONÁRIO: \n")

            nome=input("Digite o nome: ")
            contr=False
            while not(contr):
                cpf=input("Digite o cpf(somente números): ")
                contr=validaCPF(cpf)
                if not(contr):
                    print("CPF Inválido!")
            endereco=input("Digite o endereço: ")
            telefone=input("Digite seu telefone: ")
            login=input("Digite seu login: ")
            senha=input("Digite sua senha: ")
            funcionarios.append(Funcionario(nome,cpf,endereco,telefone,login,senha))
            print()
    elif op == 2:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        situation = False

        for obj in funcionarios:
            if(login == obj.login and senha == obj.senha):
                situation = True
                break

        if(situation):
            print("[1] - Cadastrar produto:")
            print("[2] - Venda de produto:")
            print("[0] - Voltar ao menu principal")
            op2 = input()

            if(op2 == 1):
                idprod = input("ID produto: ")
                nomeprod = input("Nome produto: ")
                precoprod = float(input("Preco produto: "))
                produtos.append(idprod, nomeprod, precoprod)
        else:
            print("Login invalido!")


print("Obrigado, tenha um bom dia!")
        
