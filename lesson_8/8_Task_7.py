#TODO - 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexCount:

    def __init__(self, cmplx):
        if type(cmplx) == int or type(cmplx) == float:
            self.cmplx = cmplx
        else:
            raise Exception('Класс ComplexNumber работает только с числами')

    def __add__(self, other):
        return ComplexCount(self.cmplx + other.cmplx)

    def __mul__(self, other):
        return ComplexCount(self.cmplx * other.cmplx)

    def __str__(self):
        return f'Результат: {self.cmplx}'


a = ComplexCount(10)
a2 = ComplexCount(18)
print(a + a2)
print(a * a2)

