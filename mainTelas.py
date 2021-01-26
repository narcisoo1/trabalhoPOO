
__author__= 'Vitoria, Josean, Narciso'
__license__= 'GPL'
__email__= 'vitoriacrisrs@gmail.com'
__version__= '1.0.0.1'
__status__= 'desenvolvimento'

'''
    Arquivo que contem toda a logica das telas de interacao com usuario
'''

import sys
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_inicial
from login import Login
from escolha_Cadastro import Escolha_Cadastro

from menuFuncionario import MenuFuncionario
from telaCadastroCliente import telaCadastroCliente
from telaCadastroProduto import telaCadastroProduto
from subMenuFuncionario import SubMenuFuncionario
from telaCadastroFuncionario import TelaCadastroFuncionario
from funcionario import Funcionario
from venda import Venda
from telaVenda import TelaVenda

from cadastroPessoa import CadastroPessoa
from cadastroFuncionario import OpcoesFuncionario
from pessoa import Pessoa
from produto import Produto
from cadastroProduto import CadastroProduto



class Ui_main(QtWidgets.QWidget):
    sscpf=''
    sslogin=''
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        '''Criacao da pilha de interface do tipo QT para notificar ao sistema a tela que deve estar em evidencia'''

        self.QtStack = QtWidgets.QStackedLayout()

        '''Instancia das telas utilizadas o sistema'''

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

        '''Descriacao da tela que sera setada para seu respectivo stack'''
        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)
        self.tela_login_ADM = Login()
        self.tela_login_ADM.setupUi(self.stack1)

        self.menuFuncionario = MenuFuncionario()
        self.menuFuncionario.setupUi(self.stack2)

        self.telaVenda = TelaVenda()
        self.telaVenda.setupUi(self.stack8)

        self.telaCadastroCliente = telaCadastroCliente()
        self.telaCadastroCliente.setupUi(self.stack3)

        self.telaEscolha = Escolha_Cadastro()
        self.telaEscolha.setupUi(self.stack4)

        self.telaCadastroProduto = telaCadastroProduto()
        self.telaCadastroProduto.setupUi(self.stack5)

        self.subMenuFuncionario = SubMenuFuncionario()
        self.subMenuFuncionario.setupUi(self.stack6)

        self.telaCadastroFuncionario = TelaCadastroFuncionario()
        self.telaCadastroFuncionario.setupUi(self.stack7)

        '''Adicionando widget para todas as stacks criadas'''
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)

class Main(QMainWindow, Ui_main):
    sslogin=''
    sscpf=''
    def __init__(self, parent=None):

        '''Classe para criacao de logica do sistema'''

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.pessoa = CadastroPessoa()
        self.funcionario = OpcoesFuncionario()
        self.produto = CadastroProduto()

        '''Desenvolvimento dos botoes e associacao a suas respectivas telas que direcionao para os metodos '''

        # tela inicial stack 0
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaSubMenuFuncionario)
        self.tela_inicial.pushButton_2.clicked.connect(self.fecharTelaInicial)

        # tela login stack 1
        self.tela_login_ADM.pushButton.clicked.connect(self.botaoLogar)
        self.tela_login_ADM.pushButton_2.clicked.connect(self.botaoVoltarTelaSubmenu)
        

        # tela submenu funcionario - stack 6
        self.subMenuFuncionario.pushButton.clicked.connect(self.abrirTelaCadastroFuncionario)
        self.subMenuFuncionario.pushButton_2.clicked.connect(self.abrirTelaLogin)
        self.subMenuFuncionario.pushButton_3.clicked.connect(self.abrirTelaInicial)

        #tela escolha
        self.telaEscolha.pushButton.clicked.connect(self.abrirTelaCadastroCliente)
        self.telaEscolha.pushButton_2.clicked.connect(self.abrirTelaCadastroProduto)
        self.telaEscolha.pushButton_3.clicked.connect(self.abrirTelaMenuFuncionario)

        #tela Cadastro Funcionario
        self.telaCadastroFuncionario.pushButton_2.clicked.connect(self.botaoCadastraFuncionario)
        self.telaCadastroFuncionario.pushButton.clicked.connect(self.botaoVoltarTelaSubmenu)

        #tela escolha venda ou cadastro
        self.menuFuncionario.pushButton.clicked.connect(self.abrirTelaVenda)
        self.menuFuncionario.pushButton_2.clicked.connect(self.abrirTelaCadastros)
        self.menuFuncionario.pushButton_3.clicked.connect(self.botaoVoltarTelaLogin)

        #tela cadastro cliente
        self.telaCadastroCliente.pushButton.clicked.connect(self.abrirTelaCadastros)
        self.telaCadastroCliente.pushButton_2.clicked.connect(self.botaoCadastraCliente)

        #tela cadastro produto
        self.telaCadastroProduto.pushButton_2.clicked.connect(self.botaoCadastraProduto)
        self.telaCadastroProduto.pushButton.clicked.connect(self.abrirTelaCadastros)

        #tela venda
        self.telaVenda.pushButton.clicked.connect(self.abrirTelaMenuFuncionario)
        self.telaVenda.pushButton_2.clicked.connect(self.botaoVenda)

    '''Funcoes que executam a acao de cada botao'''

    def botaoCadastraFuncionario(self):
        nome = self.telaCadastroFuncionario.lineEdit.text()
        endereco = self.telaCadastroFuncionario.lineEdit_2.text()
        cpf = self.telaCadastroFuncionario.lineEdit_3.text()
        telefone = self.telaCadastroFuncionario.lineEdit_4.text()
        senha = self.telaCadastroFuncionario.lineEdit_5.text()
        login = self.telaCadastroFuncionario.lineEdit_6.text()
        if not (nome == '' or endereco == '' or cpf == '' or telefone == '' or senha == '' or login == ''):
            f = Funcionario(nome, endereco, cpf, telefone, senha, login)
            if self.funcionario.cadastra(f):
                QMessageBox.information(None, "Ok!", "Cadastro realizado!")
                self.telaCadastroFuncionario.lineEdit.setText('')
                self.telaCadastroFuncionario.lineEdit_2.setText('')
                self.telaCadastroFuncionario.lineEdit_3.setText('')
                self.telaCadastroFuncionario.lineEdit_4.setText('')
                self.telaCadastroFuncionario.lineEdit_5.setText('')
                self.telaCadastroFuncionario.lineEdit_6.setText('')
            else:
                QMessageBox.information(None, "Erro!", "O CPF informado já está cadastrado!")
        else:
            QMessageBox.information(None, "Erro!", "Todos os valores devem ser preenchidos!")

        self.QtStack.setCurrentIndex(6)

    def botaoLogar(self):
        loginfunc=self.tela_login_ADM.lineEdit.text()
        senhafunc=self.tela_login_ADM.lineEdit_2.text()
        acesso=self.funcionario.login(loginfunc,senhafunc)
        if(acesso!=None):
            global sslogin
            sslogin=loginfunc
            global sscpf
            sscpf=acesso.cpf
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.information(None, "Erro!", "Login inválido!")

    def botaoVenda(self):
        global sscpf
        nomeProduto = self.telaVenda.lineEdit_4.text()
        quantidade = int(self.telaVenda.lineEdit_6.text())
        cpfcliente = self.telaVenda.lineEdit_5.text()
        if not (nomeProduto == '' or quantidade == '' or cpfcliente == '' or sscpf == ''):
            if self.pessoa.vazio():
                QMessageBox.information(None, "Erro!", "Sem clientes cadastrados!")
                self.QtStack.setCurrentIndex(2)
            elif(self.pessoa.busca(cpfcliente)==None):
                QMessageBox.information(None, "Erro!", "Cliente com CPF não cadastrado!")
                self.QtStack.setCurrentIndex(2)
            else:
                v = Venda(nomeProduto,quantidade,cpfcliente,sscpf)
                if (self.produto.venda(v)):
                    QMessageBox.information(None, "Ok!", "Venda realizada!")
                    self.telaVenda.lineEdit_4.setText('')
                    self.telaVenda.lineEdit_6.setText('')
                    self.telaVenda.lineEdit_5.setText('')
                else:
                    QMessageBox.information(None, "Erro!", "Produto inválido ou fora de estoque!")
        else:
            QMessageBox.information(None, "Erro!", "Todos os valores devem ser preenchidos!")
            self.QtStack.setCurrentIndex(8)

    def botaoVoltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
    
    def botaoVoltarTelaLogin(self):
        global sslogin
        global sscpf
        sslogin=""
        sscpf="" 
        self.QtStack.setCurrentIndex(1)

    def botaoVoltarTelaSubmenu(self):
        self.QtStack.setCurrentIndex(6)

    def botaoCadastraCliente(self):
        nome = self.telaCadastroCliente.lineEdit.text()
        endereco = self.telaCadastroCliente.lineEdit_2.text()
        cpf = self.telaCadastroCliente.lineEdit_3.text()
        telefone = self.telaCadastroCliente.lineEdit_4.text()
        if not (nome == '' or endereco == '' or cpf == '' or telefone == ''):
            p = Pessoa(nome, cpf, endereco, telefone)
            if (self.pessoa.cadastra(p)):
                QMessageBox.information(None, "Ok!", "Cadastro realizado!")
                self.telaCadastroCliente.lineEdit.setText('')
                self.telaCadastroCliente.lineEdit_2.setText('')
                self.telaCadastroCliente.lineEdit_3.setText('')
                self.telaCadastroCliente.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, "Erro!", "O CPF informado já está cadastrado!")
        else:
            QMessageBox.information(None, "Erro!", "Todos os valores devem ser preenchidos!")

        self.QtStack.setCurrentIndex(4)

    def botaoCadastraProduto(self):
        nome = self.telaCadastroProduto.lineEdit.text()
        preco = self.telaCadastroProduto.lineEdit_2.text()
        quantidade = int(self.telaCadastroProduto.lineEdit_3.text())
        id = self.telaCadastroProduto.lineEdit_4.text()
        if not (nome == '' or preco == '' or quantidade == '' or id == ''):
            pr = Produto(id, nome, preco, quantidade)
            if (self.produto.cadastra(pr)):
                QMessageBox.information(None, "Ok!", "Cadastro realizado!")
                self.telaCadastroProduto.lineEdit.setText('')
                self.telaCadastroProduto.lineEdit_2.setText('')
                self.telaCadastroProduto.lineEdit_3.setText('')
                self.telaCadastroProduto.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, "Erro!", "O CPF informado já está cadastrado!")
        else:
            QMessageBox.information(None, "Erro!", "Todos os valores devem ser preenchidos!")

        self.QtStack.setCurrentIndex(4)

    ###############################################################
    def abrirTelaVenda(self):
        self.QtStack.setCurrentIndex(8)

    def abrirTelaCadastros(self):
        self.QtStack.setCurrentIndex(4)
    
    def abrirTelaMenuFuncionario(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaSubMenuFuncionario(self):
        self.QtStack.setCurrentIndex(6)

    def abrirTelaCadastroFuncionario(self):
        self.QtStack.setCurrentIndex(7)

    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaInicial (self):
        self.QtStack.setCurrentIndex(0)


    def fecharTelaInicial(self):
        sys.exit()

    ###############################################################

    def abrirTelaCadastroCliente(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaCadastroProduto(self):
        self.QtStack.setCurrentIndex(5)
        rand = random.randint(0, 1000000)
        self.telaCadastroProduto.lineEdit_4.setText(str(rand))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
