import pytest

# @pytest.fixture()
# def username():
#     return 'Maria_G'
#
# @pytest.fixture()
# def password():
#     return 'b61aa5326f'

@pytest.fixture()
def title():
    return 'White cat', 'Black dooog'

@pytest.fixture()
def new_title():
    return 'my_new_post', 'no_text'