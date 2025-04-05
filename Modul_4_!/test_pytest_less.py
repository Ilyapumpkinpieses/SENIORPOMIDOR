from pytest_less import add  # здесь мы импортируем функцию add в текущий модуль

def test_add():
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(-1, -1) == -2
def test_admin():
    assert 5==7