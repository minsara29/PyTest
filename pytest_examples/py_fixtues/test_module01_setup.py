import pytest 

@pytest.fixture()
def cities():
    print("\n in fixtures.... \n")
    city = ["New York", "London", "Riyadh", "Singapore", "Mumbai"]
    return city 


def test_fix01(cities):
    print(cities)
    assert "New York" in cities
    assert cities [0] == "New York"
    assert cities[::2] == ["New York", "Riyadh", "Mumbai"]

def test_fix02(cities):
    print(cities)
    assert cities[::-2] == ["Mumbai", "Riyadh", "New York"]


@pytest.mark.xfail(reason="Konwn issue: 'function' object is not subscriptable")
@pytest.mark.usefixtures("cities")
def test_fix03():
    assert cities[1] == "london"

