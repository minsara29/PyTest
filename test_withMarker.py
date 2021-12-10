import pytest


@pytest.mark.smoke
def test_login():
    print("login")

@pytest.mark.regression
def test_process():
    print("process")


@pytest.mark.smoke  # own marker need to be defined in .ini file to avoid warning
def test_logout():
    print("logout")


# only run smoke functions
# pytest test_withMarker.py -m "smoke"

# run which are matching
# pytest test_withMarker.py -m "smoke regression"


# with and conditions
# pytest test_withMarker.py -m "smoke and regression"