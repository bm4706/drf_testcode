from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User

# Create your tests here.
# class TestView(TestCase):
#     def test_two_is_three(self):
#         self.assertEqual(2,3) # 2와 3이 같은지 확인
        
#     def test_two_is_two(self):
#         self.assertEqual(2,2) 

class UserRegistrationAPIViewTestCase(APITestCase): 
    def test_registration(self):# 회원가입 기능 테스트
        url = reverse("user_view")
        user_data = {
            "username":"testuser",
            "fullname":"테스터",
            "email":"test@testuser.com",
            "password":"password"
        } # 하나라도 없으면 에러뜸
        response = self.client.post(url, user_data)
        # print(response.data) # 이걸 사용하면 에러 발생시 무슨에러인지 파악가능
        self.assertEqual(response.status_code, 200)
        
        """       
    def test_login(self): # 로그인 기능 테스트
        url = reverse("token_obtain_pair")
        user_data = {
            "username":"testuser",
            "fullname":"테스터",
            "email":"test@testuser.com",
            "password":"password"
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        """
        
class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {'username':'john','password':'johnpassword'}
        self.user = User.objects.create_user('john','johnpassword')
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        print(response.data["access"])
        self.assertEqual(response.status_code, 200)
        
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
        response = self.client.get(
            path=reverse("user_view"),
            HTTP_AUTHORIZATION=f"Bearer {access_token}"
        )
        self.assertEqual[response.status_code, 200] # 되는지 여부 확인 아래거쓸라면 주석처리해야함
        # self.assertEqual(response.data['username'], self.data['username'])
           
        