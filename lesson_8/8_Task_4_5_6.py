#TODO - 4, 5, 6.Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


from abc import ABC, abstractmethod, abstractproperty


class Warehouse:
    equipment = []
    organizationDict = {}

    def receipt(self, el):
        if isinstance(el, OfficeEquipment):
            self.equipment.append(el)
        else:
            raise Exception('wrong class')

    def consumption(self, el):
        if isinstance(el, OfficeEquipment):
            self.equipment.remove(el)
        else:
            raise Exception('wrong class')

    def count(self):
        return len(self.equipment)

    def sendToOrganozation(self, orgName, el):
        if isinstance(el, OfficeEquipment):
            if self.organizationDict.get(orgName) == None:
                self.organizationDict[orgName] = [el]
            else:
                self.organizationDict.get(orgName).append(el)
        else:
            raise Exception('wrong class')


class OfficeEquipment(ABC):

    def id(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def toPrint(self):
        print('print')


class Scanner(OfficeEquipment):

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def toScan(self):
        print('scan')


class Xerox(OfficeEquipment):

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def toCopy(self):
        print('copy')


p = Printer(1)
s = Scanner(2)
x = Xerox(3)
warehouse = Warehouse()
warehouse.receipt(p)
warehouse.receipt(s)
#warehouse.receipt('3232')
warehouse.sendToOrganozation('lorus', p)
warehouse.sendToOrganozation('lorus', s)
warehouse.sendToOrganozation('gpb', x)
print(warehouse.organizationDict)
