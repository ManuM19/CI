#! python3

from selenium import webdriver
from PageObjects.amazonhome import HomePage
#from amazonshoe import ShoePage
#from amazonformal import FormalshoePage
import pickle, time
import pytest

@pytest.fixture(scope='class')
def set_up(request):
  driver = webdriver.Chrome()
  if request.cls is not None:
    request.cls.driver = driver
  driver.get("https://www.amazon.in/")
  driver.maximize_window()
  cookies = pickle.load(open("C:\\Users\\anshu\\AppData\\Local\\Programs\\Python\\Jenkinsjob\\cookies.pkl", "rb"))
  for cookie in cookies:
    driver.add_cookie(cookie)
  time.sleep(5)
  driver.refresh()
  yield driver
  driver.quit()
  
@pytest.mark.usefixtures("set_up")
class TestAmazon:
  def test_orders(self):
    home = HomePage(self.driver)
    orders = home.your_orders()
    assert '5' in orders
