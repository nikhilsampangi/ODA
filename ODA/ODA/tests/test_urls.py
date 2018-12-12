from django.urls import reverse,resolve
from patient_home import urls
from welcome import urls
from blog import urls

class TestUrls:

    def test_detail_url(self):
        path1=reverse('pat_home_page')
        assert resolve(path1).view_name == 'pat_home_page'

    def test_detail_url(self):
        path1=reverse('blog_home')
        assert resolve(path1).view_name == 'blog_home'

    def test_detail_url(self):
        path1=reverse('make_blog')
        assert resolve(path1).view_name == 'make_blog'

    def test_detail_url(self):
        path1=reverse('mail', kwargs={'lat':'13.82323123' ,'long':'80.5123213'})
        assert resolve(path1).view_name == 'mail'

    def test_detail_url(self):
        path1=reverse('doctor_list_page')
        assert resolve(path1).view_name == 'doctor_list_page'

    def test_detail_url(self):
        path1 = reverse('doctor_locator')
        assert resolve(path1).view_name == 'doctor_locator'

        path2 = reverse('my_appointments')
        assert resolve(path2).view_name == 'my_appointments'

        path3 = reverse('blood_banks')
        assert resolve(path3).view_name == 'blood_banks'

        path4 = reverse('pharma_loc')
        assert resolve(path4).view_name == 'pharma_loc'

        path5 = reverse('gen_meds')
        assert resolve(path5).view_name == 'gen_meds'

        path6 = reverse('bloodbank')
        assert resolve(path6).view_name == 'bloodbank'

        path7 = reverse('medicalshop')
        assert resolve(path7).view_name == 'medicalshop'

        path8 = reverse('avail', kwargs={'shop_name':'pharmacy'})
        assert resolve(path8).view_name == 'avail'

        path9 = reverse('profile-upadate')
        assert resolve(path9).view_name == 'profile-upadate'

        path10 = reverse('take_appo')
        assert resolve(path10).view_name == 'take_appo'

        path11 = reverse('book')
        assert resolve(path11).view_name == 'book'

        path12 = reverse('pharma_stock')
        assert resolve(path12).view_name == 'pharma_stock'

        path13 = reverse('about_page')
        assert resolve(path13).view_name == 'about_page'
