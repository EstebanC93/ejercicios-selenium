import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
	
	def setUp(self):	
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.get('https://the-internet.herokuapp.com/')
		driver.find_element_by_link_text("Disappearing Elements").click()

	def test_name_elements(self):
		driver = self.driver
		 #Lista vacia para almacenar los elementos del menu
		options = []
		#Elementos existentes
		menu = 5
		#Intentos de refrescamiento iniciara en 1 por que al ingresar se contara como un intento
		tries =+ 1

		#Bucle while para iniciar proceso
		while len(options) < 5:
			options.clear()

			for i in range(menu):
				#Uso de try y except para evitar errores
				try:
					#Agregamos la iteracion al xpath para recorrer todos los elementos
					option_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i + 1}]/a")
					#Agregar elementos a la lista
					options.append(option_name.text)
					print(options)
				except:
					#Aplicando el iterador para contar los pasos
					print(f"Option number {i + 1} is NOT FOUND")
					tries +=1
					driver.refresh()

		print(f"Finished in {tries} tries")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(verbosity = 2)