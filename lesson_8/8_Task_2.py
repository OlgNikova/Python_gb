#TODO - 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой


class MyZero(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


def my_err(x, y):
    try:
        if y == 0:
            raise MyZero('Деление на ноль невозможно')
        result = x / y
    except MyZero as err:
        print(err)
    else:
        print(f'Деление выполнено: {result}')


my_err(3, 0)
