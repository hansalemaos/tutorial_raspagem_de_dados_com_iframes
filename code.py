from time import sleep
import undetected_chromedriver as uc
from a_selenium_get_source_from_all_frames import get_sourcecode_from_all_frames
import bs4


if __name__ == "__main__":
    driver = uc.Chrome(
    )
    driver.get(r"https://testpages.herokuapp.com/styled/iframes-test.html")
    sleep(2)
    source = get_sourcecode_from_all_frames(
        driver,
    )
    textos = [bs4.BeautifulSoup(x).text for x in source]
    for x in textos:
        print(x)
