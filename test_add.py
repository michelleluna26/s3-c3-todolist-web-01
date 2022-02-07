from add import add, addNumberList


def test_add():
    result = add(1, 2)
    assert result == 3


"""pruebas existen para poder verificar"""


def test_addNumberList_pepito():

    result = addNumberList([1, 2])
    assert result == 3

    result = addNumberList([])
    assert result == 0

    result = addNumberList([1, 2, 3])
    assert result == 6
