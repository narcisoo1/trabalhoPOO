import sys
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_inicial
from login import Login
from escolha_Cadastro import Escolha_Cadastro

from telaMenu import telaMenu
from telaCadastroCliente import telaCadastroCliente
from telaCadastroProduto import telaCadastroProduto
from subMenuFuncionario import SubMenuFuncionario
from telaCadastroFuncionario import TelaCadastroFuncionario
from funcionario import Funcionario

from cadastroPessoa import CadastroPessoa
from pessoa import Pessoa
from produto import Produto
from cadastroProduto import CadastroProduto


class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)
        self.tela_login_ADM = Login()
        self.tela_login_ADM.setupUi(self.stack1)

        self.telaMenu = telaMenu()
        self.telaMenu.setupUi(self.stack2)

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

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.pessoa = CadastroPessoa()
        self.produto = CadastroProduto()
        self.funcio =


        # tela inicial stack 0
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaSubMenuFuncionario)
        self.tela_inicial.pushButton_2.clicked.connect(self.fecharTelaInicial)

        # tela login stack 1
        self.tela_login_ADM.pushButton.clicked.connect(self.botaoLogar)
        self.tela_login_ADM.pushButton_2.clicked.connect(self.botaoVoltarTelaInicial)

        # tela submenu funcionario - stack 6
        self.subMenuFuncionario.pushButton.clicked.connect(self.abrirTelaCadastroFuncionario)
        self.subMenuFuncionario.pushButton_2.clicked.connect(self.abrirTelaLogin)
        self.subMenuFuncionario.pushButton_3.clicked.connect(self.abrirTelaInicial)

        #tela escolha
        self.telaEscolha.pushButton.clicked.connect(self.abrirTelaCadastroCliente)
        #self.telaEscolha.pushButton_2.clicked.connect(self.abrirTelaCadastroProduto)
        #self.telaEscolha.pushButton_3.clicked.connect(self.)

        #tela Cadastro Funcionario
        self.telaCadastroFuncionario.pushButton_2.clicked.connect(self.botaoCadastraFuncionario)
        self.telaCadastroFuncionario.pushButton.clicked.connect(self.abrirTelaInicial)

        self.telaMenu.pushButton.clicked.connect(self.abrirTelaCadastroCliente)
        self.telaMenu.pushButton_2.clicked.connect(self.abrirTelaCadastroProduto)

        self.telaCadastroCliente.pushButton_2.clicked.connect(self.botaoCadastraCliente)
        self.telaCadastroCliente.pushButton.clicked.connect(self.botaoVoltar)
        self.telaCadastroProduto.pushButton_2.clicked.connect(self.botaoCadastraProduto)
        self.telaCadastroProduto.pushButton.clicked.connect(self.botaoVoltar)

    def botaoCadastraFuncionario(self):
        nome = self.telaCadastroFuncionario.lineEdit.text()
        endereco = self.telaCadastroFuncionario.lineEdit_2.text()
        cpf = self.telaCadastroFuncionario.lineEdit_3.text()
        telefone = self.telaCadastroFuncionario.lineEdit_4.text()
        senha = self.telaCadastroFuncionario.lineEdit_5.text()
        login = self.telaCadastroFuncionario.lineEdit_6.text()
        if not (nome == '' or endereco == '' or cpf == '' or telefone == '' or senha == '' or login == ''):
            f = Funcionario(nome, endereco, cpf, telefone, senha, login)
            if self.Funcionario(f):
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

    def botaoVoltarTelaCadastroFuncionario(self):
        self.QtStack.setCurrentIndex(1)

    def botaoLogar(self):
        self.QtStack.setCurrentIndex(4)

    def botaoVoltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def botaoCadastraCliente(self):
        nome = self.telaCadastroCliente.lineEdit.text()
        endereco = self.telaCadastroCliente.lineEdit_2.text()
        cpf = self.telaCadastroCliente.lineEdit_3.text()
        telefone = self.telaCadastroCliente.lineEdit_4.text()
        if not (nome == '' or endereco == '' or cpf == '' or telefone == ''):
            p = Pessoa(nome, endereco, cpf, telefone)
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

        self.QtStack.setCurrentIndex(0)

    def botaoCadastraProduto(self):
        nome = self.telaCadastroProduto.lineEdit.text()
        preco = self.telaCadastroProduto.lineEdit_2.text()
        quantidade = self.telaCadastroProduto.lineEdit_3.text()
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

        self.QtStack.setCurrentIndex(0)

    ###############################################################
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

    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastroCliente(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaCadastroProduto(self):
        self.QtStack.setCurrentIndex(2)
        rand = random.randint(0, 1000000)
        self.telaCadastroProduto.lineEdit_4.setText(str(rand))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
