from unittest import TestCase
from task232 import Vacancy, Report


class SalaryTests(TestCase):
    def test_vacancy_type(self):
        self.assertEqual(type(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'})).__name__, 'Vacancy')

    def test_salary_from(self):
        self.assertEqual(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'}).salary_from, 20000)

    def test_salary_to(self):
        self.assertEqual(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'}).salary_to, 30000)

    def test_salary_currency(self):
        self.assertEqual(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'}).salary_currency, 'RUR')

    def test_avarage_salary(self):
        self.assertEqual(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'}).avarage_salary, 25000)

    def test_area_name(self):
        self.assertEqual(Vacancy({'name': 'Аналитик', 'salary_from': '20000.0', 'salary_to': '30000.0', 'salary_currency': 'RUR', 'area_name': 'Екатеринбург', 'published_at': '2022:20:14'}).area_name, 'Екатеринбург')


class DateConverterTests(TestCase):
    def test_procent_convert(self):
        self.assertDictEqual(Report('Программист', {2017: 20000}, {2017: 50}, {2017: 50000}, {2017: 5}, {'Москва': 0.56}, {'Москва': 10000}).procent_format(), {'Москва': '56%'})

    def test_procent_convert_many_symbols_after_dot(self):
        self.assertDictEqual(Report('Программист', {2017: 20000}, {2017: 50}, {2017: 50000}, {2017: 5}, {'Москва': 0.56532523}, {'Москва': 10000}).procent_format(), {'Москва': '56.53%'})
