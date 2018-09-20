
import string
from django.conf import settings

if not settings.configured:
	settings.configure(
		# DEBUG=True,
		# ROOT_URLCONF=name,
	)


def encode(val):
	if type(val) == int:
		return b'i' + bytes(str(val), 'utf-8') + b'e'

	elif type(val) == str:
		return bytes(str(len(val)) + ':' + val, 'utf-8')

	elif type(val) == bytes:
		return bytes(str(len(val)), 'utf-8') + b':' + val

	elif type(val) == list:
		end = b'l'
		for i in val:
			end += encode(i)
		end += b'e'
		return end

	elif type(val) == dict:
		keys = []
		for k, v in val.items():
			keys.append(k)
			keys.append(v)
		end = b'd'
		for i in keys:
			end += encode(i)
		end += b'e'
		return end




def decode(val):

	def decode_b_str(val):
		if val.startswith(b"i"):
			result = int(val[1:val.find(b'e')])
			return result, val[val.find(b'e') + 1:]

		elif str(val, 'utf-8')[0] in string.digits:
			dig = True
			counter = 0
			while dig:
				if str(val, 'utf-8')[counter] in string.digits:
					counter += 1
				else:
					dig = False
			integer = int(val[0:counter])
			if counter > 1:
				return val[counter+1:integer+counter+1], val[(integer+counter+1):]
			else:
				return val[2:(int(str(val, 'utf-8')[0]) + 2)], val[(int(str(val, 'utf-8')[0]) + 2):]

		elif val.startswith(b"l"):
			decoded_list = []
			new_b_str = val[1:]
			while not new_b_str.startswith(b"e"):
				returned_str = decode_b_str(new_b_str)[0]
				new_b_str = decode_b_str(new_b_str)[1]
				decoded_list.append(returned_str)
			new_b_str = new_b_str[1:]
			return decoded_list, new_b_str

		elif val.startswith(b"d"):
			decoded_list = []
			new_b_str = val[1:]
			while not new_b_str.startswith(b"e"):
				returned_str, new_b_str = decode_b_str(new_b_str)
				decoded_list.append(returned_str)
			new_b_str = new_b_str[1:]
			result_dict = dict(zip(decoded_list[::2], decoded_list[1::2]))
			return result_dict, new_b_str

		else:
			raise ValueError("Incorect value")

	if isinstance(val, str):
		val = val.encode("utf-8")

	returned_data = decode_b_str(val)[0]
	new_b_str = decode_b_str(val)[1]

	if new_b_str:
		raise ValueError("Incorect value")
	return returned_data


print(decode(b'9:sdvsdg vs'))
print(decode(b'i-0653e'))
print(decode(b'1: '))
print(decode(b'l4:spam4:eggse'))
print(decode(b'l4:spami3345e4:eggs53:papandopusvdvsewwwwwwwwwwwwwwwwwwwscscvsvseeeeeeeelosli33ei-6ei0eee'))
print(decode(b'd3:cow3:moo4:spam4:eggse'))
print(decode(b'd4:spaml1:a1:bee'))
print(decode(b'd4:spaml4:eggs5:applee3:vool4:lark5:argsee4:wool3:cow2:xo4:tezee'))
print(decode(encode({b'spam': [b'eggs', b'apple'], b'voo': [b'lark', b'argse'], b'wool': b'cow', b'xo': b'teze'})))
print()
print()
print(encode(b'sdvsdg vs'))
print(encode(b'sdvsvvsdvdg sdvsdvvs'))
print(encode(-653))
print(encode(' '))
print(encode([b'spam', b'eggs']))
print(encode([b'spam', 3345, b'eggs', b'papandopusvdvsewwwwwwwwwwwwwwwwwwwscscvsvseeeeeeeelos', [33, -6, 0]]))
print(encode({b'cow': b'moo', b'spam': b'eggs'}))
print(encode({b'spam': [b'a', b'b']}))
print(encode({b'spam': [b'eggs', b'apple'], b'voo': [b'lark', b'argse'], b'wool': b'cow', b'xo': b'teze'}))
