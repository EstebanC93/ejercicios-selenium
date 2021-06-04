'''import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		self.driver = driver
		driver.implicity_wait(30)
		driver.maximize_window()
		driver.get('http://demo-store.seleniumacademy.com/')

	def test_search_field(self):
		self.asserTrue(self.is_element_present(By.NAME, 'q'))

	def test_languaje_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-languaje'))

	def tearDown(self):
		self.driver.quit()

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by = how, value = what)
		except NosuchElementException as variable:
			return False
		return True

if __name__ == '__main__':
	unittest.main(verbosity = 2)'''

import unittest
from selenium import webdriver
#sirve como excepción para los assertions cuando queremos
#validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get('http://demo-store.seleniumacademy.com/')

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def	is_element_present(self, how, what):
		try:  #busca los elementos según el parámetro
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True

if __name__ == '__main__':
	unittest.main(verbosity = 2)