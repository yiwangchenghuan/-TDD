from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')      #解析url，映射到响应的视图函数
        self.assertEqual(found.func,home_page)