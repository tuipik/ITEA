import pytest

@pytest.parametrize('a,b', [
	('spam': bytes('4:spam')),
	('': bytes('0:')),
	(')(*&&^*(&#@^||', )
])

def test_encode_str(a,b):
	pass

@pytest.parametrize('a,b', [
	(3: 'i3e'),
	(-3: 'i-3e')
])
def test_encode_bytes(a,b):
	pass

@pytest.parametrize('a,b', [
	('spam': bytes('4:spam'))
])








if isinstance(obj, int):
        return b"i" + str(obj).encode() + b"e"
    elif isinstance(obj, bytes):
        return str(len(obj)).encode() + b":" + obj
    elif isinstance(obj, str):
        return encode(obj.encode("utf-8"))
    elif isinstance(obj, list):
        return b"l" + b"".join(map(encode, obj)) + b"e"
    elif isinstance(obj, dict):
        if all(isinstance(i, bytes) for i in obj.keys()):
            items = list(obj.items())
            items.sort()
            return b"d" + b"".join(map(encode, it.chain(*items))) + b"e"
        else:
            raise ValueError("dict keys should be bytes " + str(obj.keys()))
    raise ValueError("Allowed types: int, bytes, list, dict; not %s", type(obj))