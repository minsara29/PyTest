import pytest 


def pytest_configure():
    pytest.var1 = "Dahlia"
    pytest.var2 = "Kannan"
    pytest.weekdays = ["mon", "tue", "wed"]

@pytest.fixture()
def fn_name():
    fn = pytest.var1 
    return fn

@pytest.fixture()
def ln_name():
    ln = pytest.var2
    return ln

@pytest.fixture()
def weekdays():
    ln = pytest.weekdays.copy()
    return ln


#access the module's variable 
#with build in function 'request'
@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "months")
    print(f"\n Fixure scope : {str(request.scope)}\n")
    print(f"\n Calling function : {str(request.function.__name__)}\n")
    print(f"\n Calling module : {str(request.module.__name__)}\n")
    mon.append("Apr")
    yield mon


@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == "list":
            return [1,2,3]
        if name == "tuple":
            return (1,2,3)
    
    return get_structure


@pytest.fixture(params=[(1,2), [3,4]], ids=['tuple', 'list'])
def setup06a(request):
    return request.param 

@pytest.fixture(params=['access', 'slice', "assign", "len"])
def setup06b(request):
    return request.param 