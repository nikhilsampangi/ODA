from patient_home.forms import ProfileUpdateForm
from welcome.forms import DoctorUpdateForm
from welcome.models import Doctors,Patient_DB
from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestRegisterSubmissionPass(TestCase):

    def setUp(self):
        # self.user = User.objects.create(username="testuser02", email="testuser02@ts.com", password="Hello World")
        pass

    def test_doc_submission(self):
        self.client = Client()
        response = self.client.post('/doc_register/',
                                    {"f_name": "test",
                                     "l_name": "user",
                                     "phone_num":"9242342332",
                                     "gender": "Male",
                                     "license": "123123",
                                     "Doctor Type":"Ge",
                                     "Doctor_Deg": "nferl",
                                     "username": "testuser02",
                                     "email": "testuser02@ts.com",
                                     "password": "HelloWorld",
                                     })
        self.assertRedirects(response,expected_url="/doc_home/")

    # def test_pat_submission(self):
    #     self.client = Client()
    #     response = self.client.post('/doc_register/',
    #                                 {"phone_num":"31231223",
    #                                  "gender":"Male",
    #                                  "username": "testuser02",
    #                                  "emer_email": "testuser_emg2@ts.com",
    #                                  })
    #     self.assertEquals(response.status_code, 302)

class TestRegisterSubmissionFail(TestCase):

    def setUp(self):
        pass

    def test_submission(self):
        self.client = Client()
        response = self.client.post('/doc_register/',
                                    {"f_name": "test",
                                     "l_name": "user",
                                     "phone_num":"31231223",
                                     "gender":"Male",
                                     "license": "123123",
                                     "Doctor Type":"Ge",
                                     "Doctor_Deg": "nferl",
                                     "username": "testuser02",
                                     "email": "testuser02@ts.com",
                                     "password": "HelloWorld",
                                     })
        self.assertEquals(response.status_code, 302)


class TestLoginSubmission(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="testuser03", email="testuser03@ts.com", password="asdasd123")
        self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')


    def test_submission(self):
        self.client = Client()
        response = self.client.post('/doc_login/',
                                    {"doc_email": "testuser03@ts.com",
                                     "doc_pass": "asdasd123"}
                                    )

        self.assertRedirects(response, expected_url="/doctor/")


class TestLoginFailSubmission(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="testuser02", email="testuser02@ts.com", password="Hello World")
        # self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')


    def test_submission(self):
        self.client = Client()
        response = self.client.post('/doc_login/',
                                    {"doc_email": "testuser02@ts.com",
                                     "doc_pass": "Hello World"})

        self.assertRedirects(response,expected_url="/doctor/")


class TestLoginWrongPasswordSubmission(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser02", email="testuser02@ts.com", password="HelloWorld")
        # self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')

    def test_submission(self):
        self.client = Client()
        response = self.client.post('/doc_login/',
                                    {"doc_email": "testuser02@ts.com",
                                     "doc_pass": "Hello World"})

        self.assertRedirects(response, expected_url="/doctor/")

class TestUpdateDoctorsForm(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name="test", last_name="user", username="testuser",email="testuser002@ts.com")

    def test_all_pass(self):
        form_instance = DoctorUpdateForm(data={
            "username":"testuser",
            "first_name": "test",
            "Phone": "999999999",
            "Desc": "info",
            "doc_type" : "GEndeal",
            "Degrees" : "MBBS",
            "d_website": "test@gmail.cin",
            "About_Clinic": "kafegis",
            "Other_info": "thia is wena",

        })

        self.assertEqual(form_instance.is_valid(), True)
        register = form_instance.save(commit=False)
        register.save()

    def test_Phone_Notvalid_fail(self):
        form_instance = DoctorUpdateForm(data={
            "username": "test",
            "Phone": "99999999999",
            "Desc": "info",
            "doc_type": "GEndeal",
            "Degrees": "MBBS",
            "d_website": "test@gmail.cin",
            "About_Clinic": "kafegis",
            "Other_info": "thia is wena",

        })
        self.assertEqual(form_instance.is_valid(), False)
        self.assertEqual(form_instance.errors.get("Phone"), ['Ensure this value has at most 10 characters (it has 11).'])

    def test_User_fail(self):
        form_instance = DoctorUpdateForm(data={
            "username": "",
            "Phone": "9999999999",
            "Desc": "info",
            "doc_type": "GEndeal",
            "Degrees": "MBBS",
            "d_website": "test@gmail.cin",
            "About_Clinic": "kafegis",
            "Other_info": "thia is wena",

        })
        self.assertEqual(form_instance.is_valid(), True)
        self.assertEqual(form_instance.errors.get("username"), None)


class TestUpdatePatientForm(TestCase):

    def setUp(self):
        self.user = User.objects.create(first_name="test", last_name="user", username="testuser",email="testuser002@ts.com")

    def test_all_pass(self):
        form_instance = ProfileUpdateForm(data={
            "last_name":"user",
            "first_name": "first",
            "emerg_email": "tuea3@jda.com",
            "Phone_num": "999999999",
            "Emergency_num":"9888888888",
            "medical_con":"nthg",


        })

        self.assertEqual(form_instance.is_valid(), True)
        register = form_instance.save(commit=False)
        register.save()

    def test_Phone_Notvalid_fail(self):
        form_instance = ProfileUpdateForm(data={
            "last_name": "user",
            "first_name": "first",
            "emerg_email": "tuea3@jda.com",
            "Phone_num": "99999999993",
            "Emergency_num": "9898989898",
            "medical_con": "nthg",

        })
        self.assertEqual(form_instance.is_valid(), False)
        self.assertEqual(form_instance.errors.get("Phone_num"), ['Ensure this value has at most 10 characters (it has 11).'])


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name="test", last_name="user", username="testuser",
                                            email="testuser002@ts.com",password="helloworld12")

    def test_doc_auth_pass_pat_auth_fail(self):
        self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.post('/doctor/',
                                    {"doc_email": "testuser002@ts.com",
                                     "doc_pass": "helloworld12"})
        self.assertRedirects(response, expected_url="/doc_home/")

    def test_doc_auth_fail_pat_auth_pass(self):
        self.user2 = Patient_DB.objects.create(P_Id=self.user, user_pat='yes')
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.post('/doctor/',
                                    {"doc_email": "testuser002@ts.com",
                                     "doc_pass": "helloworld12"})
        self.assertRedirects(response, expected_url="/home/")

    def test_after_doc_log_front_page(self):
        self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.post('/',
                                    )
        self.assertRedirects(response, expected_url="/doc_home/")

    def test_after_doc_log_home(self):
        self.user2 = Doctors.objects.create(D_Id=self.user, user_pat='no')
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.post('/home/',
                                    )
        self.assertRedirects(response, expected_url="/doc_home/")








