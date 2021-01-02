import sys
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from telaMenu import telaMenu
from telaCadastroCliente import telaCadastroCliente
from telaCadastroProduto import telaCadastroProduto

from cadastroPessoa import CadastroPessoa
from pessoa import Pessoa
from produto import Produto
from cadastroProduto import CadastroProduto

class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.telaMenu = telaMenu()
        self.telaMenu.setupUi(self.stack0)

        self.telaCadastroCliente = telaCadastroCliente()
        self.telaCadastroCliente.setupUi(self.stack1)
        
        self.telaCadastroProduto = telaCadastroProduto()
        self.telaCadastroProduto.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow,Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.pessoa = CadastroPessoa()
        self.produto = CadastroProduto()
        self.telaMenu.pushButton.clicked.connect(self.abrirTelaCadastroCliente)
        self.telaMenu.pushButton_2.clicked.connect(self.abrirTelaCadastroProduto)

        self.telaCadastroCliente.pushButton_2.clicked.connect(self.botaoCadastraCliente)
        self.telaCadastroCliente.pushButton.clicked.connect(self.botaoVoltar)
        self.telaCadastroProduto.pushButton_2.clicked.connect(self.botaoCadastraProduto)
        self.telaCadastroProduto.pushButton.clicked.connect(self.botaoVoltar)


    def botaoCadastraCliente(self):
        nome=self.telaCadastroCliente.lineEdit.text()
        endereco=self.telaCadastroCliente.lineEdit_2.text()
        cpf=self.telaCadastroCliente.lineEdit_3.text()
        telefone=self.telaCadastroCliente.lineEdit_4.text()
        if not(nome=='' or endereco=='' or cpf=='' or telefone==''):
            p=Pessoa(nome,endereco,cpf,telefone)
            if(self.pessoa.cadastra(p)):
                QMessageBox.information(None,"Ok!","Cadastro realizado!")
                self.telaCadastroCliente.lineEdit.setText('')
                self.telaCadastroCliente.lineEdit_2.setText('')
                self.telaCadastroCliente.lineEdit_3.setText('')
                self.telaCadastroCliente.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,"Erro!","O CPF informado já está cadastrado!")
        else:
            QMessageBox.information(None,"Erro!","Todos os valores devem ser preenchidos!")
       
        self.QtStack.setCurrentIndex(0)
    
    def botaoCadastraProduto(self):
        nome=self.telaCadastroProduto.lineEdit.text()
        preco=self.telaCadastroProduto.lineEdit_2.text()
        quantidade=self.telaCadastroProduto.lineEdit_3.text()
        id=self.telaCadastroProduto.lineEdit_4.text()
        if not(nome=='' or preco=='' or quantidade=='' or id==''):
            pr=Produto(id,nome,preco,quantidade)
            if(self.produto.cadastra(pr)):
                QMessageBox.information(None,"Ok!","Cadastro realizado!")
                self.telaCadastroProduto.lineEdit.setText('')
                self.telaCadastroProduto.lineEdit_2.setText('')
                self.telaCadastroProduto.lineEdit_3.setText('')
                self.telaCadastroProduto.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,"Erro!","O CPF informado já está cadastrado!")
        else:
            QMessageBox.information(None,"Erro!","Todos os valores devem ser preenchidos!")
       
        self.QtStack.setCurrentIndex(0)

    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaCadastroCliente(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaCadastroProduto(self):
        self.QtStack.setCurrentIndex(2)
        rand=random.randint(0,1000000)
        self.telaCadastroProduto.lineEdit_4.setText(str(rand))

if __name__=='__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())