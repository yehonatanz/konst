import pytest

from konst._common import _verify_attr


@pytest.mark.parametrize('name', ['lower', 'UPPER', 'PascalCase', 'camelCase'])
def test_regular_name(name):
    _verify_attr(name)


@pytest.mark.parametrize('name', ['_single', '__double', '__dunder__'])
def test_bad_name(name):
    with pytest.raises(AttributeError):
        _verify_attr(name)
