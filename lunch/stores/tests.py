from django.test import TestCase
from .models import Store, MenuItem

# Create your tests here.
class HomeViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'home.html')

class StoreViewTests(TestCase):

    def setUp(self):
        Store.objects.create(name='AC', notes='就是爽')
        AC = Store.objects.create(name='AC')
        MenuItem.objects.create(store=AC, name='001', price=100)

    def tearDown(self):
        Store.objects.all().delete()
        
    def test_list_view(self):
        r = self.client.get('/store/')
        self.assertContains(
            r, '<a class="navbar-brand" href="/">午餐系統</a>',
            html=True,
        )
        self.assertContains(r, '<a href="/store/1/">AC</a>', html=True)
        self.assertContains(r, '就是爽')
    
    # def test_detail_view(self):
    #     response = self.client.get('/store/1/')
    #     self.assertContains(
    #         response, '<tr><td>001</td><td>100</td></tr>',
    #         html=True,
    #     )