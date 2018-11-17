def test_symbol():
    from konst.symbol import RED

    assert RED.name == 'RED'


def test_equal_symbols_are_identical():
    from konst.symbol import GREEN

    g1 = GREEN
    from konst.symbol import GREEN

    g2 = GREEN
    assert g1 is g2
