import random, time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

proxies = ["http://user:pass@proxy1:port", ...]
options = uc.ChromeOptions()
options.add_argument('--proxy-server=' + random.choice(proxies))
driver = uc.Chrome(options=options)

driver.get("https://exemple.com/")

time.sleep(random.uniform(3, 6))
slides = driver.find_elements(By.CSS_SELECTOR, ".slide")
for s in slides:
    print(s.text)
    time.sleep(random.uniform(2,4))

driver.quit()
