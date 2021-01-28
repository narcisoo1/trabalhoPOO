import sys
import os
import random

import mysql.connector as mysql
conexao = mysql.connect(host='localhost', db='trabalhoPOO', user='root', passwd='password')
cursor = conexao.cursor()

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

while(enviar!= 'sair'):
    recebe = con.recv(1024)
    mensagem=''
    variaveis=''
    mensagem=recebe.decode('utf-8')
    variaveis=mensagem.split(";")
    if(variaveis[0]=="cf"):
        create= """CREATE TABLE IF NOT EXISTS funcionarios(nome text NOT NULL, cpf integer PRIMARY KEY, 
        endereco text NOT NULL, telefone text NOT NULL, senha VARCHAR(32) NOT NULL, login text NOT NULL);"""
        cursor.execute(create)
        nome=variaveis[1]
        endereco=variaveis[2]
        cpf=variaveis[3]
        telefone=variaveis[4]
        senha=variaveis[5]
        login=variaveis[6]
        if not (nome == '' or endereco == '' or cpf == '' or telefone == '' or senha == '' or login == ''):
            sql='SELECT * FROM funcionarios WHERE cpf='+cpf+';'
            #print(sql)
            cursor.execute(sql)
            c=None
            for c in cursor:
                c=c
            if c==None:
                add='INSERT INTO funcionarios (nome,cpf,endereco,telefone,senha,login) VALUES ("'+nome+'",'+cpf+',"'+endereco+'","'+telefone+'",MD5("'+senha+'"),"'+login+'");'
                #print(sql)
                cursor.execute(add)
                enviar = "true"
            else:
                enviar = "false" 
        else:
            enviar = "falsevazio" 
        
        con.send(enviar.encode())
    
    elif(variaveis[0]=="lf"):
        login=variaveis[1]
        senha=variaveis[2]
        if not(login=='' or senha==''):
            sql='SELECT * FROM funcionarios WHERE login="'+login+'" AND senha=MD5("'+senha+'");'
            acesso=None
            #print(sql)
            cursor.execute(sql)
            for acesso in cursor:
                acesso=acesso
            #print(acesso[1])
            if(acesso!=None):
                enviar=str(acesso[1])
            else:
                enviar="None"
        else:
            enviar = "false"
        con.send(enviar.encode())
    elif(variaveis[0]=="cc"):
        create= """CREATE TABLE IF NOT EXISTS clientes(nome text NOT NULL, cpf integer PRIMARY KEY, 
        endereco text NOT NULL, telefone text NOT NULL);"""
        cursor.execute(create)
        nome=variaveis[1]
        endereco=variaveis[2]
        cpf=variaveis[3]
        telefone=variaveis[4]
        if not (nome == '' or endereco == '' or cpf == '' or telefone == ''):
            
            sql='SELECT * FROM clientes WHERE cpf='+cpf
            #print(sql)
            cursor.execute(sql)
            c=None
            for c in cursor:
                c=c
            if c==None:
                add='INSERT INTO clientes (nome,cpf,endereco,telefone) VALUES ("'+nome+'",'+cpf+',"'+endereco+'","'+telefone+'")'
                cursor.execute(add)
                enviar = "true"
            else:
                enviar = "false" 
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    
    elif(variaveis[0]=="cp"):
        create= """CREATE TABLE IF NOT EXISTS produtos(nome text NOT NULL, preco float NOT NULL, 
        quantidade integer NOT NULL, id integer PRIMARY KEY);"""
        cursor.execute(create)
        nome=variaveis[1]
        preco=variaveis[2]
        quantidade=variaveis[3]
        id=variaveis[4]
        if not (id == '' or nome == '' or preco == '' or quantidade == ''):
            sql='SELECT * FROM produtos WHERE id='+id
            #print(sql)
            cursor.execute(sql)
            c=None
            for c in cursor:
                c=c
            if not(c==None):
                qtd=int(quantidade)+c[2]
                upqtd='UPDATE produtos SET quantidade='+str(qtd)+' WHERE id='+id
                uppco='UPDATE produtos SET preco='+str(preco)+' WHERE id='+id
                cursor.execute(upqtd)
                cursor.execute(uppco)
                enviar = "true"
            else:
                add='INSERT INTO produtos (nome,preco,quantidade,id) VALUES ("'+nome+'",'+preco+','+quantidade+','+id+')'
                cursor.execute(add)
                enviar = "true"
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    
    elif(variaveis[0]=="vp"):
        idproduto=variaveis[1]
        quantidade=variaveis[2]
        cpfcliente=variaveis[3]
        cpfvendedor=variaveis[4]
        if not (idproduto == '' or quantidade == '' or cpfcliente == '' or cpfvendedor == ''):
            p=None
            bps='SELECT * FROM clientes'
            #print(sql)
            cursor.execute(bps)
            for p in cursor:
                p=p
            if p==None:
                enviar="falsepessoavazio"
            bcpf='SELECT * FROM clientes WHERE cpf='+cpfcliente
            cursor.execute(bcpf)
            p=None
            for p in cursor:
                p=p
            if p==None:
                enviar="falsecpf"
            else:
                bpd='SELECT * FROM produtos WHERE id='+idproduto
                cursor.execute(bpd)
                p=None
                for p in cursor:
                    p=p
                if not(p==None):
                    if (int(quantidade)<=p[2]):
                        create1= """CREATE TABLE IF NOT EXISTS vendas(idvenda integer AUTO_INCREMENT PRIMARY KEY, 
                        idproduto integer NOT NULL, qtdproduto integer NOT NULL, 
                        cpfvendedor integer NOT NULL, cpfcliente integer NOT NULL);"""
                        cursor.execute(create1)
                        qtd=int(p[2])-int(quantidade)
                        upqtd='UPDATE produtos SET quantidade='+str(qtd)+' WHERE id='+str(idproduto)
                        cursor.execute(upqtd)
                        v='INSERT INTO vendas (idproduto,qtdproduto,cpfvendedor,cpfcliente) VALUES ('+str(idproduto)+','+str(quantidade)+','+str(cpfvendedor)+','+str(cpfcliente)+')'
                        cursor.execute(v)
                        enviar = "true"
                    else:
                        enviar = "falseqtd"
                else:
                    enviar = "falsepd" 
        else:
            enviar = "falsevazio"
        con.send(enviar.encode())
    if(mensagem=="sair"):
        enviar="sair"
        conexao.commit()
        conexao.close()
        con.send(enviar.encode())


serv_socket.close()