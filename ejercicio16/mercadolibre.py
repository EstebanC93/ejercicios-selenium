import unittest
from selenium import webdriver
from time import sleep

class TestingMercadoLibre(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'C:/Users/Esteban Henao/Downloads/chromedriver.exe')
		driver = self.driver
		driver.get('https://mercadolibre.com')
		driver.maximize_window()

	def test_search_ps5(self):
		driver = self.driver

		country = driver.find_element_by_id('CO')
		country.click()
		sleep(1)

		search_field = driver.find_element_by_name('as_word')
		search_field.click()
		search_field.clear
		search_field.send_keys('Playstation 5')
		search_field.submit()
		sleep(2)

		location = driver.find_element_by_partial_link_text('Antioquia')
		#location.click()
		driver.execute_script("arguments[0].click();", location)
		sleep(1)

		condition = driver.find_element_by_partial_link_text('Nuevo')
		#condition.click()
		driver.execute_script("arguments[0].click();", condition)

		order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
		order_menu.click()
		higher_price = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
		#higher_price.click()
		driver.execute_script("arguments[0].click();", higher_price)
		sleep(1)

		articles = []
		prices = []

		for i in range(5):
			article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
			articles.append(article_name)
			article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
			prices.append(article_price)

			print(articles, prices)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()