import pytest

@pytest.fixture
def coll():
    return [1, 2, 3]

def test_stack(coll):
    coll.append('one')
    coll.append('two')

    assert coll.pop() == 'two'
    assert coll.pop() == 'one'


def test_emptiness(coll):
    coll.clear()
    assert not coll
    coll.append('one')
    assert bool(coll)

    coll.pop()
    assert not coll



def test_pop_with_empty_stack(coll):
    coll.clear()
    with pytest.raises(IndexError):
        coll.pop()