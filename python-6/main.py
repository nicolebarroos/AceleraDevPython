import abc
#Classe abstrata não permite instanciarmos diretamente um método
#É indispensável a implementação dos métodos

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(metaclass=abc.ABCMeta):

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abc.abstractmethod
    def calc_bonus(self):
        pass

    @abc.abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary,
            department=Department('managers', 1)):

        super().__init__(code, name, salary)
        self.__departament = department

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8

    def get_departament(self):
        #Uma forma de proteger os métodos para que não sejam instanciados diretamente
        return self.__departament.name

    def set_departament(self, departament_name):
        self.__departament.name = departament_name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.get_sales() * 0.15

    def get_hours(self):
        return 8

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale


#testes:
#employee = Employee('8166, Nicole', 1000)
#print(employee)

#


