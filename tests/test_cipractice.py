import cipractice
from hypothesis import given
from hypothesis import example
from hypothesis.strategies import text

def test_greeting():
    assert cipractice.greeting() == 'Hello world!'

@given(s=text())
@example(s='')
def test_decode_inverts_encode(string):
	assert cipractice.decode(cipractice.encode(s)) == s
