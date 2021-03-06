from .salaried import Salaried
from datetime import*
from dateutil.relativedelta import relativedelta
from .use import*

class Commissioned(Salaried):
    def __init__(self, name, adress, type, id, MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day, Salary_M, commissionP):
        super().__init__(name, adress, type, id,  MethodPayment,IsSyndicacte,day_in1,day_in2,pay_day,Salary_M)
        self.commissionP = float(commissionP)

    def set_commssion_day(self, valor):
        ganho = (valor * self.commissionP/100)
        return ganho
    
    def get_agenda(self):
        return self.pay_day
    
    def set_agenda(self, novaAgenda):
        self.pay_day = novaAgenda

    def salary_day(self):
        if(self.pay_day == 1 ):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day + timedelta(weeks = 1) == day_today ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 2):
            day = arrumar_data.dia_semana(self.day_in1,self.day_in2)
            day_today = date.today()
            if(day + timedelta(weeks = 2) == day_today ):
                return self.Salary_M
            else:
                return 0
        elif(self.pay_day == 3):
            day_today = date.today()
            if(self.day_in1 +  relativedelta(day=31) == day_today):
                return self.Salary_M
            else:
                return 0
        else:
            print("ok")


    def payday(self):
        tipo = "Os comissionados recebem a cada 2 sextas-feira"
        
    def set_pay_day(self,newPayday):
        self.pay_day = newPayday
    
    def get_commission(self):
        return self.commissionP
    def put_commission(self):
        nemCommission = float(input('Adicione aqui o novo percentual de comissão do funcionário'))
    
    def input_informations(self,day,money):
        self.day = input("")
        self.money = input("")
    
    def reciveSalary(self):
        newSalary = self.Salary_M /2 + (self.money * self.commissionP)
        return newSalary
    def __str__(self):
        return( " | "+ self.id +" | " + self.name +" | " + self.type +" | " +self.adress + " | " + self.IsSyndicacte + " | ")
    
    def get_id(self):
        return self.id
    
    def get_Salary_M(self):
        return self.Salary_M

    def set_name(self):
        newName = input("Insira o novo nome do empregado no sistema:\n")
        self.name = newName
    def get_name(self):
        return self.name

    def get_time1(self):
        return self.day_in1

    def get_time2(self):
        return self.day_in2

    def set_adress(self):
        newAdress = input("Insira o novo endereço do empregado no sistema: \n")
        self.adress = newAdress
    def get_adress(self):
        return self.adress

    def set_type(self): #criar aqui uma pasta externa com os três tipos associados á números para serem salvos no sistema
        newType = input("Insira o novo tipo de empregado:\n(1) Horista\n(2) Assalariado\n(3) Comissionado")
        
    def get_type(self):
        return self.type  

    def set_IsSyndicacte(self, newIsSyndicacte):
        self.IsSyndicacte = newIsSyndicacte
    def get_IsSyndicacte(self):
        return self.IsSyndicacte
    
    def set_MethodPayment(self):#realizar aqui o mesmo menu de tipo de empregadp
        newMethodPayment = input("Insira o novo método de pagamento do empregado:\n(1)Cheque pelos correios\n(2)Cheque em mãos\n(3)Depósito em conta bancária\n")
        self.MethodPayment = newMethodPayment
    def get_MethodPayment(self):
        return self.MethodPayment
#aqui recebe a cada duas semanas


    