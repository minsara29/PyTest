from datetime import datetime

import pytest
from student import Student

@pytest.fixture
def dummy_student(request):
    return Student("kannan", datetime(2000, 1, 1), "test", request.param)



