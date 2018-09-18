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
	elif type(val) == dict:
		keys = list(val.keys())
		keys.sort()
		end = b'd'
		for i in keys:
			if type(i) == str:
				end += encode(i)
			end += encode(val[i])
		end += b'e'
		return end
	elif type(val) == list:
		end = b'l'
		for i in val:
			end += encode(i)
		end += b'e'
		return end


def decode(val):
	pass

# print(decode('9:sdvsdg vs'))
# print(decode('i-0653e'))
# print(decode('l4:spami-3345e4:eggs12:papandopulosli33ei-6ei0eee'))
# print(decode('d3:cow3:moo4:spam4:eggse'))
# print(decode('d4:spaml1:a1:bee'))
# print(decode('d4:spaml4:eggs5:applee3:vool4:lark5:argsee4:wool3:cow2:xo4:tezee'))
#
#
#
# print(encode('sdvsdg vs'))
# print(encode(-3))
# print(encode(['spam', -3345, 'eggs', 'papandopulos', [33, -6, 0]]))
# print(encode({b'cow': 'moo', b'spam': 'eggs'}))
# print(encode({b'spam': ['a', 'b']}))
# print(encode({b'spam': ['eggs', 'apple'], b'voo': ['lark', 'argse'], b'wool': b'cow', b'xo': b'teze'}))
