#!python3
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
  def __init__(self, driver):
    self.driver = driver
    self.orders_xpath = "//a[contains(@href, 'order-history')]"
    self.amazonpay_xpath = "//a[contains(@href, 'nav_apay')]"
    self.num_orders_css = "span.num-orders"
    self.menu_class = "nav-line-1"
    self.password_id = "ap_password"
    self.signin_id = "signInSubmit"
  
  def your_orders(self):
    try:
      self.driver.find_element_by_xpath(self.orders_xpath).click()
    except:
      menu = self.driver.find_element_by_class_name(self.menu_class)
      link = self.driver.find_element_by_xpath(self.orders_xpath)
      ActionChains(self.driver).move_to_element(menu).click(link).perform()
    time.sleep(5)
    try:
      self.driver.find_element_by_id(self.password_id).send_keys("Novak3rd")
      self.driver.find_element_by_id(self.signin_id).click()
      time.sleep(5)
    except:
      pass
    orders = self.driver.find_element_by_css_selector(self.num_orders_css)
    return orders.text
        
      
    


