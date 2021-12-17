from tkinter import*
from scr.employee import Employee
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 

def main():
    
    print("Por favo, selecione a opção desejada: \n")
    print("1) Adição de um empregado;\n2) Remoção de um empregado;\n3) Lançar um Cartão de Ponto; \n4) Lançar um Resultado Venda;5) Lançar uma taxa de serviço;\n6) Alterar detalhes de um empregado;\n7) Rodar a folha de pagamento para hoje;\n8) Undo/redo;\n9) Agenda de Pagamento;\n10) Criação de Novas Agendas de Pagamento;\n11) Sair;")
    number = int(input())
    empregados = []
    numberOfEmployees = 0
    while(number != 11):
        if(number == 1):#def __init__(self, name, adress, type, id, salary, MethodPayment,IsSidcate):
            numberOfEmployees = numberOfEmployees + 1
            name = input("Insira o nome do empregado:\n")
            adress = input("Insira aqui o endereço do empregado:\n")
            type = input("Insira aqui o tipo do empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado\n")
            salary = input("Insira aqui quanto o empregado ganha:\n")
            MethodPayment = input("Insira aqui o método de pagamento escolhido pelo empregado:\n(1)Cheque pelos correios\n(2)Cheque em mãos\n(3)Depósito em conta bancária\n")
            IsSyndicacte = input("O novo empregado pertence ao sindicato? (s \ n)\n")
            isd = 0
            while(isd == 0):
                if(IsSyndicacte == "s"):
                    isd = 1
                    gerar_sindicato = 1
                elif(IsSyndicacte == "n"):
                    isd = 1
                    continue
                else:
                    print("Opçaõ inválida")
                    IsSyndicacte = input("O novo empregado pertence ao sindicato? (s \ n)\n")

            novoEmpregado = Employee(name,adress,type,numberOfEmployees,salary, MethodPayment,IsSyndicacte)
            empregados.insert(numberOfEmployees,novoEmpregado)
            print("Novo funcionário adicionado com sucesso!")
            print(empregados)
            print(novoEmpregado)

        elif(number == 2):
            numberOfEmployees = numberOfEmployees - 1
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
            empregados.pop(id)
            print("Funcionário removido com sucesso!")
        elif(number == 3):
            #lançar cartão de ponto
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 4):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 5):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 6):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 7):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 8):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 9):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 10):
            #remover um empregado
            id = input("Insira o id do empregado que deseja retirar do sistema")
        elif(number == 11):
            return #parar
        else:
            print("Entrada inválida")
        
        number = int(input("Por favo, selecione a opção desejada: \n\n1) Adição de um empregado;\n2) Remoção de um empregado;\n3) Lançar um Cartão de Ponto; \n4) Lançar um Resultado Venda;5) Lançar uma taxa de serviço;\n6) Alterar detalhes de um empregado;\n7) Rodar a folha de pagamento para hoje;\n8) Undo/redo;\n9) Agenda de Pagamento;\n10) Criação de Novas Agendas de Pagamento;\n11) Sair\n"))


    
main()


