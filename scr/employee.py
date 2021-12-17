from tkinter import*
#turtle 
#importante lembrar que o tipo de salário está associado ao tipo de empregado

class Employee():

    def __init__(self, name, adress, type, id, salary, MethodPayment,IsSyndicacte):
        self.name = name
        self.adress = adress
        self.type = type
        self.id = id
        self.salary = salary
        self.MethodPayment = MethodPayment
        self.IsSyndicacte = IsSyndicacte
    
    def set_name(self):
        newName = input("Insira o novo nome")
        self.name = newName
    def get_name(self):
        return self.name

    def set_adress(self):
        newAdress = input("Insira o novo endereço")
        self.name = newAdress
    def get_adress(self):
        return self.adress

    def set_type(self): #criar aqui uma pasta externa com os três tipos associados á números para serem salvos no sistema
        newType = input("Insira o novo tipo de empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado")
        self.type = newType
    def get_type(self):
        return self.type  

    def set_salary(self):
        newSalary = input("Insira o novo valor do salário do empregado")
        self.salary = newSalary
    def get_salary(self):
        return self.salary

    def set_IsSyndicacte(self):
        newIsSyndicacte = input("Insira o a entrada ou saída de um empregado ao sindicato(Saída = s e entrada = e.)") #aqui deve conter algo para exclui o empregado do sindicato
        self.IsSyndicacte = newIsSyndicacte
    def get_IsSyndicacte(self):
        return self.IsSyndicacte
    
    def set_MethodPayment(self):#realizar aqui o mesmo menu de tipo de empregadp
        newMethodPayment = input("Insira o novo método de pagamento do empregado:\n(1)Cheque pelos correios\n(2)Cheque em mãos\n(3)Depósito em conta bancária\n")
        self.MethodPayment = newMethodPayment
    def get_MethodPayment(self):
        return self.MethodPayment

    
    

