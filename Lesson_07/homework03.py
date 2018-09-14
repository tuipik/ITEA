# bencoding
# http://www.bittorrent.org/beps/bep_0003.html

# Strings are length-prefixed base ten followed by a colon and the string.
# For example 4:spam corresponds to 'spam'.

# Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
# For example i3e corresponds to 3 and i-3e corresponds to -3.
# Integers have no size limitation. i-0e is invalid.
# All encodings with a leading zero, such as i03e, are invalid,
# other than i0e, which of course corresponds to 0.

# Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
# For example l4:spam4:eggse corresponds to ['spam', 'eggs'].

# Dictionaries are encoded as a 'd' followed by a list of alternating keys
# and their corresponding values followed by an 'e'.
# For example, d3:cow3:moo4:spam4:eggse corresponds to {'cow': 'moo', 'spam': 'eggs'}
# Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).

def encode(val):
	if type(val) == str:
		return str_encode(val)

	elif type(val) == int:
		return int_encode(val)

	elif type(val) == list:
		return list_encode(val)

	elif type(val) == dict:
		return dict_encode(val)

	else: raise TypeError('This type of argument can`t be encoded')

def str_encode(val):
	result = str(len(val)) + ':' + val
	return result

def int_encode(val):
	result = 'i' + str(val) + 'e'
	return result

def list_encode(val):
	result = str()
	for item in val:
		result += str_encode(item)
	final_result = 'l' + result + 'e'
	return final_result


def dict_encode(val):
	result = str()
	for key, value in val.items():
		if type(value) == str:
			result += str_encode(key)
			result += str_encode(value)
		elif type(value) == list:
			result += str_encode(key)
			result += list_encode(value)
	final_result = 'd' + result + 'e'
	return final_result



import string
def decode(val):
	if val[0] in string.digits:
		return str_decode(val)
	elif val[0] == 'i':
		return int_decode(val)
	elif val[0] == 'l':
		return list_decode(val)
	elif val[0] == 'd':
		return dict_decode(val)
	else: raise TypeError('This type of argument can`t be decoded')

def str_decode(val):
	return val[2:]

def int_decode(val):
	return int(val.lstrip('i').rstrip('e'))

def list_decode(val):
	razbor = val.split(':')
	result = []
	del razbor[0]
	for item in razbor:
		item = list(item)
		while item[-1] in string.digits:
			del item[-1]
		for_item = ''.join(item)
		result.append(for_item)
	return result

def dict_decode(val):



# print(decode('9:sdvsdg vs'))
# print(decode('i-03e'))
# print(decode('l4:spam4:eggs12:papandopulose'))




# print(encode('sdvsdg vs'))
# print(encode(-3))
# print(encode(['spam', 'eggs', 'papandopulos']))
print(encode({'cow': 'moo', 'spam': 'eggs'}))
print(encode({'spam': ['a', 'b']}))