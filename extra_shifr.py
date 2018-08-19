"""Some text"""


from random import randint

def shifr_func(a, b):
	error = 0

	if a.replace(' ', '').isalpha():
		error += 0
	elif a == None:
		error += 1
	else:
		error += 1

	try:
		b = int(b)
		error += 0
	except ValueError:
		error += 2
	except TypeError:
		error += 2


	if error == 0:
		data_num_list = list(str(b))
		print('End code:', error)
		fst_ra = 0
		for i in data_num_list:
			ra_num_str = randint(fst_ra+1, len(a))
			fst_ra = ra_num_str
			a = a[:ra_num_str] + i + a[ra_num_str:]
		print(a)
		return a
	elif error == 1:
		print('End code:', error,'\nThere is not only letters in the string')
		return 1
	elif error == 2:
		print('End code:', error, '\nThe encription number should be an integer')
		return 2
	elif error == 3:
		print('End code:', error, '\nCheck the input data: string should consists of the letters only '
								  'and the encription number should be an integer')
		return 3




def deshifr_func(a):
	if a == 1 or a == 2 or a == 3:
		return
	number = ''
	new_str= ''
	for letter in a:
		if letter.isdigit():
			number += letter
		else:
			new_str += letter

	print(number)
	print(new_str)


DATA = [
	(123, 'шифрование трафика'),
	(45675679643245566787543222333255688,
	 'дело благородное'),
    (None, 'qwerty'),
    (4839, 'Боинг747 идёт на посадку'),
	('98y9', 'something got wrong!')
]

for numer, st in DATA:
	deshifr_func(shifr_func(st, numer))
	print()

