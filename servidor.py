import sys
import os
import random

from funcionario import Funcionario
from cadastroFuncionario import OpcoesFuncionario

from pessoa import Pessoa
from cadastroPessoa import CadastroPessoa

from produto import Produto
from cadastroProduto import CadastroProduto

from venda import Venda

import socket

host = 'localhost'
port = 8001
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print('Aguarde a conexao...')
con, cliente = serv_socket.accept()
print('Conectado')
print('Aguardando mensagem...')
enviar = ''

funcionario = OpcoesFuncionario()
pessoa = CadastroPessoa()
produto = CadastroProduto()

while(enviar!= 'sair'):
    recebe = con.recv(1024)
    mensagem=''
    variaveis=''
    mensagem=recebe.decode('utf-8')
    variaveis=mensagem.split(";")
    if(variaveis[0]=="cf"):
        nome=variaveis[1]
        endereco=variaveis[2]
        cpf=variaveis[3]
        telefone=variaveis[4]
        senha=variaveis[5]
        login=variaveis[6]
        if not (nome == '' or endereco == '' or cpf == '' or telefone == '' or senha == '' or login == ''):
            f = Funcionario(nome, cpf, endereco, telefone, senha, login)
            if funcionario.cadastra(f):
                enviar = "true"
            else:
                enviar = "false" 
        else:
            enviar = "falsevazio" 
        
        con.send(enviar.encode())
    
    elif(variaveis[0]=="lf"):
        login=variaveis[1]
        senha=variaveis[2]
        acesso=funcionario.login(login,senha)
        if(acesso!=None):
            enviar=acesso.cpf
        else:
            enviar="None"
        con.send(enviar.encode())
    
    elif(variaveis[0]=="cc"):
        nome=variaveis[1]
        endereco=variaveis[2]
        cpf=variaveis[3]
        telefone=variaveis[4]
        if not (nome == '' or endereco == '' or cpf == '' or telefone == ''):
            p = Pessoa(nome, cpf, endereco, telefone)
            if pessoa.cadastra(p):
                enviar = "true"
            else:
                enviar = "false" 
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    
    elif(variaveis[0]=="cp"):
        nome=variaveis[1]
        preco=variaveis[2]
        quantidade=variaveis[3]
        id=variaveis[4]
        if not (id == '' or nome == '' or preco == '' or quantidade == ''):
            qtd=int(quantidade)
            pr = Produto(id, nome, preco, qtd)
            if produto.cadastra(pr):
                enviar = "true"
            else:
                enviar = "false" 
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    
    elif(variaveis[0]=="vp"):
        nome=variaveis[1]
        quantidade=variaveis[2]
        cpfcliente=variaveis[3]
        cpfvendedor=variaveis[4]
        if not (nome == '' or quantidade == '' or cpfcliente == '' or cpfvendedor == ''):
            if pessoa.vazio():
                enviar="falsepessoavazio"
            elif pessoa.busca(cpfcliente)==None:
                enviar="falsecpf"
            else:
                qtd=int(quantidade)
                v = Venda(nome, qtd, cpfcliente, cpfvendedor)
                if produto.venda(v):
                    enviar = "true"
                else:
                    enviar = "false" 
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    if(mensagem=="sair"):
        enviar="sair"
        con.send(enviar.encode())

serv_socket.close()