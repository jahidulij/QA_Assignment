# Write a simple script which:
# 1) Accepts a Wikipedia link - return/throw an error if the link is not a valid wiki link
# 2) Accepts a valid integer between 1 to 20 - call it n
# 3) Scrape the link provided in Step 1, for all wiki links embedded in the page and store
#    them in a data structure of your choice.
# 4) Repeat Step 3 for all newly found links and store them in the same data structure.
# 5) This process should terminate after n cycles.

# Optional:
# 1) Optimize your code not to visit any links you've already visited.
# 2) Write the results ( all found links, total count, unique count ) to a CSV/JSON file.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = input("Enter wikipedia link: ")
wiki_link_contains = "https://en.wikipedia.org/"

if wiki_link_contains in url:
    pass
else:
    print("Please Enter valid wikipedia link.")

n = int(input("Enter integer between 1 and 20: "))

if (n < 1) or (n > 20):
    print("Please Enter integer between 1 and 20")
else:
    pass

driver.get(url)
driver.maximize_window()
links = []
all_links = driver.find_elements(By.XPATH, "//a[@href]")

i = 1
while i <= n:
    wiki_link = all_links[i].get_attribute("href")
    if "wiki" in wiki_link:
        links.append(wiki_link)
        # print(wiki_link)
    else:
        continue
    i += 1

print(links)

driver.quit()

