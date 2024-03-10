import pytest
from main import get_title, check_title

def test_step1(title):
    assert title[0] in get_title(title[1])

def test_step2(new_title):
    assert new_title[0] in check_title(new_title[1])



if __name__ == '__main__':
    pytest.main(['-vv'])