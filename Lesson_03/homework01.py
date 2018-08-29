# Задание 1. Встроенные типы данных, операторы, функции и генераторы
#
# Напишите реализации объявленных ниже функций. Для проверки
# корректности реализации ваших функций, запустите тесты:
#
# pytest test_homework01.py
#
# Если написанный вами код не содержит синтаксических ошибок,
# вы увидите результаты тестов ваших решений.


def fac(n):
	"""
	Факториал

	Факториал числа N - произведение всех целых чисел от 1 до N
	включительно. Например, факториал числа 5 - произведение
	чисел 1, 2, 3, 4, 5.

	Функция должна вернуть факториал аргумента, числа n.
	"""
	result = int()

	for i in range(1, n+1):
		if result >= 1:
			result *= i
		else: result += i
	return result




def gcd(a, b):
	"""
	Наибольший общий делитель (НОД) для двух целых чисел.

	Предполагаем, что оба аргумента - положительные числа
	Один из самых простых способов вычесления НОД - метод Эвклида,
	согласно которому

	1. НОД(a, 0) = a
	2. НОД(a, b) = НОД(b, a mod b)

	(mod - операция взятия остатка от деления, в python - оператор '%')
	"""
	result = [max(a,b), min(a,b)]

	while result[-1] != 0:
		result.append(result[-2] % result[-1])
	return result[-2]


def fib(a = 15):
	"""
	Генератор для ряда Фибоначчи

	Вам необходимо сгенерировать бесконечный ряд чисел Фибоначчи,
	в котором каждый последующий элемент ряда является суммой двух
	предыдущих. Начало последовательности: 1, 1, 2, 3, 5, 8, 13, ..

	Подсказка по реализации: для бесконечного цикла используйте идиому

	while True:
	  ..

	"""
	fibo_list = []

	for i in range(1, a + 1):
		if len(fibo_list) < 2:
			fibo_list += [i]*2
		else:
			fibo_list += [fibo_list[-1] + fibo_list[-2]]
	return fibo_list


def flatten(seq):
	"""
	Функция, преобразующая вложенные последовательности любого уровня
	вложенности в плоские, одноуровневые.

	>>> flatten([])
	[]
	>>> flatten([1, 2])
	[1, 2]
	>>> flatten([1, [2, [3]]])
	[1, 2, 3]
	>>> flatten([(1, 2), (3, 4)])
	[1, 2, 3, 4]
	"""
	if type(seq) is list or type(seq) is tuple:
		if len(seq) > 1:
			return flatten(seq[0]) + flatten(seq[1:])
		elif seq == []:
			return seq
		else:
			return flatten(seq[0]) + []
	else:
		return [seq]




class call_count():
	def __init__(self, function):
		self.function = function
		self._call_count = 0

	def __call__(self, *args, **kwargs):
		self._call_count += 1
		return self.function(*args, **kwargs)

	@property
	def call_count(self):
		return self._call_count


@call_count
def add(a, b):
	return a + b
