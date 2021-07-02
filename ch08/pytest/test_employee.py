# # from _pytest.monkeypatch import monkeypatch
# import requests
# from employee import Employee
# import pytest
# # import requests

# @pytest.fixture
# def emp_1():
#     emp_1 = Employee('Jensen', 'Yap', 50000)
#     return emp_1

# @pytest.fixture
# def emp_2():
#     emp_2 = Employee('Taeil', 'Kim', 60000)
#     return emp_2

# def test_email(emp_1, emp_2):
#     assert emp_1.email == 'Jensen.Yap@email.com'
#     assert emp_2.email == 'Taeil.Kim@email.com'

#     emp_1.first = 'John'
#     emp_2.first = 'Jane'

#     assert emp_1.email == 'John.Yap@email.com'
#     assert emp_2.email == 'Jane.Kim@email.com'

# def test_fullname(emp_1, emp_2):
#     assert emp_1.fullname == 'Jensen Yap'
#     assert emp_2.fullname == 'Taeil Kim'

#     emp_1.first = 'John'
#     emp_2.first = 'Jane'

#     assert emp_1.fullname == 'John Yap'
#     assert emp_2.fullname == 'Jane Kim'

# def test_apply_raise(emp_1, emp_2):

#     emp_1.apply_raise()
#     emp_2.apply_raise()

#     assert emp_1.pay == 52500
#     assert emp_2.pay == 63000

# def test_month_schedule(emp_1, monkeypatch):
#     def mock_get(url):
#         assert url == 'http://company.com/Yap/May'
#         class MockResponse:
#             ok = True
#             text = 'Success'
#         return MockResponse()

#     monkeypatch.setattr(requests, 'get', mock_get)

#     assert emp_1.monthly_schedule('May') == 'Success'

#     # emp_2.monthly_schedule('June')
#     # assert emp_2.monthly_schedule('June') == 'Success'
