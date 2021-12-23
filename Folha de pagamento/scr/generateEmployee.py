from .employee import Employee
from .hourly import Hourly
from .commissioned import Commissioned
from .salaried import Salaried

class generateEployee():
    def generate(type, name, address, id, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day):
        if type == 1:
            num2 = str(id)
            pay_day = 1
            hourDay = int(input("Insira quanto o empregado recebe por hora: R$\n"))
            newEmployee = Hourly(name, address, "Horista", num2, MethodPayment, IsSyndicacte, day_in1,day_in2,pay_day, hourDay)
            return newEmployee
        elif type == 2:
            num2 = str(id)
            pay_day = 3
            fixedSalary = input("Insira o salário fixo mensal: R$\n")
            newEmployee = Salaried(name, address, "Assalariado", num2, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day, fixedSalary)
            return newEmployee
        elif type == 3:
            num2 = str(id)
            pay_day = 2
            fixedSalary = input("Insira o salário fixo mensal: R$\n")
            commissionPercent = float(input("Insira o percentual de comissão % : \n"))
            newEmployee = Commissioned(name, address, "Comissionado", num2, MethodPayment, IsSyndicacte,day_in1,day_in2,pay_day, fixedSalary, commissionPercent)
            return newEmployee

class list_of_employees(Employee):
    def __ini__(self,list):
        super().__init__()
        self.list = []
    
    def __str__(self):
        i = 0
        while(i < len(self.list)):
            return(self.list[i])
            i = i + 1
