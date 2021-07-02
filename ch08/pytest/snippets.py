
from employee import Employee
import pytest

@pytest.fixture
def emp_info():
    emp_1 = Employee('Jensen', 'Yap', 50000)
    emp_2 = Employee('Taeil', 'Kim', 60000)
    return emp_1, emp_2

def test_email(emp_info):
    emp_1, emp_2 = emp_info
    assert emp_1.email == 'Jensen.Yap@email.com'
    assert emp_2.email == 'Taeil.Kim@email.com'

    emp_1.first = 'John'
    emp_2.first = 'Jane'

    assert emp_1.email == 'John.Yap@email.com'
    assert emp_2.email == 'Jane.Kim@email.com'

def test_fullname(emp_info):
    emp_1, emp_2 = emp_info
    assert emp_1.fullname == 'Jensen Yap'
    assert emp_2.fullname == 'Taeil Kim'

    emp_1.first = 'John'
    emp_2.first = 'Jane'

    assert emp_1.fullname == 'John Yap'
    assert emp_2.fullname == 'Jane Kim'

def test_apply_raise(emp_info):
    emp_1, emp_2 = emp_info

    emp_1.apply_raise()
    emp_2.apply_raise()

    assert emp_1.pay == 52500
    assert emp_2.pay == 63000

# def test_month_schedule(monkeypatch):
#     monkeypatch.setattr(requests, 'get', mock_get)
# def test_month_schedule():
#     with patch('employee.requests.get') as mocked_get:
#         mocked_get.return_value.ok = True
#         mocked_get.return_value.text = 'Success'

#         schedule = emp_1.monthly_schedule('May')
#         mocked_get.assert_called_with('http://company.com/Yap/May')
#         .assertEqual(schedule, 'Success')
