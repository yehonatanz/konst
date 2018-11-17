def test_string():
    from konst.string import A

    assert A == 'A'


def test_string_preserve_case():
    from konst.string import mixedCase

    assert mixedCase == 'mixedCase'
