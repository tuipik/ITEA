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
	# return flatten(seq[0]) + (flatten(seq[1:]) if len(seq) > 1 else []) if type(seq) is list or type(seq) is tuple else [seq]

print(flatten([]))
print(flatten([1, 2, [3,4]]))
print(flatten([1, [2, [3]]]))
print(flatten([(1, 2), (3, 4, [5, 6, (7, 8)])]))