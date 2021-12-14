import pytest
from student import is_eligible_for_degree


@pytest.mark.parametrize("dummy_student, expected", [(19, False), (21, True)],
                         indirect=["dummy_student"],
                         ids=["ineligible", "eligible"])
def test_is_eligible_for_degree(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) == expected

