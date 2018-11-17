import pytest


def test_symbol():
    from konst.symbol import RED

    assert RED.name == 'RED'


def test_equal_symbols_are_identical():
    from konst.symbol import GREEN

    g1 = GREEN
    from konst.symbol import GREEN

    g2 = GREEN
    assert g1 is g2


def test_symbol_is_immutable():
    from konst.symbol import BLUE

    with pytest.raises(TypeError):
        BLUE.name = 3
    with pytest.raises(TypeError):
        del BLUE.name
