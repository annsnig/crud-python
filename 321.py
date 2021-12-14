import requests
import unittest 

class MyTest(unittest.TestCase):

	def test_create(self):
		r = requests.post("https://petstore.swagger.io/v2/user")

	def test_get(self):
		 r = requests.get("https://petstore.swagger.io/v2/user/login?username=anna&password=12345678")

	def test_update(self):
		r = requests.put("https://petstore.swagger.io/v2/user/anna")

	def test_get_user(self):
		 r = requests.get("https://petstore.swagger.io/v2/user/anya")

	def test_delete(self):
		r = requests.delete("https://petstore.swagger.io/v2/user/anya")


if __name__=='__main__':
    unittest.main()