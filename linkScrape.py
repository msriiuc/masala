import selenium.webdriver as webdriver

def get_results(search_term):
    url = "http://www.informationcommittee.gov.mm/en/search/node?keys=" + ' '.join(search_term)
    chromedriver = r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    links = driver.find_elements_by_xpath("//h3//a")
    
    results = []

    for link in links:    
        href = link.get_attribute("href")
        results.append(str(href))
        length = len(results)
        if length > 0 :
            print(results + '\n')
        else:
            print('No links found!')
    driver.close()
    return results
    
print('Done!')
get_results("Rohingya")
