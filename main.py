import sys
from design import *
from PyQt5.QtWidgets import QApplication, QDialogButtonBox, QLabel
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QVBoxLayout


class Agenda(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnRegistra.clicked.connect(self.inserir)
        self.btnRegistra.clicked.connect(self.limpa_line)

    def inserir(self):
        nome = self.inputNome.text()
        telefone = self.inputTelefone.text()
        idade = self.inputIdade.text()
        rowPosition = self.table.rowCount()

        if not '' in (nome, telefone, idade):
            self.table.insertRow(rowPosition)
            self.table.setItem(rowPosition, 0, QTableWidgetItem(nome))
            self.table.setItem(rowPosition, 1, QTableWidgetItem(idade))
            self.table.setItem(rowPosition, 2, QTableWidgetItem(telefone))
        else:
            warningDialog = CustomDialog(self)
            warningDialog.exec_()
    
    def limpa_line(self):
        self.inputNome.setText('')
        self.inputTelefone.setText('')
        self.inputIdade.setText('')


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Erro!')

        QBtn = QDialogButtonBox.Ok

        self.btnBox = QDialogButtonBox(QBtn)
        self.btnBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        mensagem = QLabel('Preencha todos os campos para registrar um contato.')
        self.layout.addWidget(mensagem)
        self.layout.addWidget(self.btnBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    agenda = Agenda()
    agenda.show()
    qt.exec_()
