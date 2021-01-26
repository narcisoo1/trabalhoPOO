## Main do trabalho
from pessoa import Pessoa
from funcionario import Funcionario
from trabalhoPOO.telas.cadastroProduto import CadastroProduto
from venda import Valida_Venda
from random import randint

funcionarios=[]
clientes=[]
produtos=[]
vendas=[]

op=int(1)

while(op!=0):

    print("Digite a opção desejada:")
    print("[1] - Cadastrar funcionário:")
    if len(funcionarios)>0:
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
            cpf=input("Digite o cpf(somente números): ")
            endereco=input("Digite o endereço: ")
            telefone=input("Digite seu telefone: ")
            login=input("Digite seu login: ")
            senha=input("Digite sua senha: ")
            funcionarios.append(Funcionario(nome,cpf,endereco,telefone,login,senha))
            print()
        else:
            print("Erro de login!\n")
    elif op == 2 and len(funcionarios)>0:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        situation = False

        for obj in funcionarios:
            if(login == obj.login and senha == obj.senha):
                situation = True
                cpf_vend=obj.cpf
                break

        if(situation):
            op2 = -1

            while(op2 != 0):
                print("[1] - Cadastrar produto:")
                if len(produtos)>0 and len(clientes)>0:
                    print("[2] - Venda de produto:")
                print("[3] - Cadastrar cliente")
                print("[0] - Voltar ao menu principal")
                op2 = int(input())

                if(op2 == 1):
                    controle=0
                    qtdProd = int(input("Quantidade de produto: "))
                    nomeprod = input("Nome produto: ")
                    precoprod = float(input("Preco produto: "))    
                    if len(produtos)>0:
                        for x in produtos:
                            if x.nomeProduto==nomeprod:
                                x.qtdProduto+=qtdProd
                                controle+=1
                        if controle==0:
                            idprod = randint(0, 1000000000)
                            produtos.append(CadastroProduto(idprod, nomeprod, precoprod, qtdProd))
                    else:
                        idprod = randint(0, 1000000000)
                        produtos.append(CadastroProduto(idprod, nomeprod, precoprod, qtdProd))

                elif(op2 == 2 and len(produtos)>0 and len(clientes)>0):
                    nomeprod = input("Nome produto: ")
                    qtd=int(input("Digite a quantidade: "))
                    contr=int(0)
                    while contr==0 :
                        cpf=input("Digite o cpf do cliente: ")
                        for x in clientes:
                            if cpf==x.cpf:
                                contr+=1
                        if contr==0:
                            print("CPF inválido!\n")
                            op3=int(input("[1] Cadastrar CPF\n[2] Corrigir CPF\n"))
                            if op3==1:
                                print("CADASTRO CLIENTE \n")
                                nome=input("Digite o nome: ")
                                endereco=input("Digite o endereço: ")
                                telefone=input("Digite seu telefone: ")
                                clientes.append(Pessoa(nome,cpf,endereco,telefone))
                                print()
                                contr+=1
                    
                    venda=Valida_Venda(nomeprod,qtd,produtos,cpf,cpf_vend)
                    if venda==False:
                        print("Venda cancelada!\n")
                    else:
                        vendas.append(venda)
                        print("Venda realizada!\n")
                
                elif(op2 == 3):
                    print("CADASTRO CLIENTE: \n")
                    nome=input("Digite o nome: ")
                    cpf=input("Digite o cpf(somente números): ")
                    endereco=input("Digite o endereço: ")
                    telefone=input("Digite seu telefone: ")
                    clientes.append(Pessoa(nome,cpf,endereco,telefone))
                    print()
                
                elif(op2 == 4):
                    for x in vendas:
                        print("Venda: ",x.nomeProduto,"\nQuantidade: ",x.qtdProduto,"\nVendedor: ",x.vendedor,"\nCliente: ",x.cliente,"\n\n")
        else:
            print("Erro de login!\n")


print("Obrigado, tenha um bom dia!")
        
