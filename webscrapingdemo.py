from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = "https://apbosma.github.io/officers.html"
page = urlopen(URL)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser") # Creates an object named soup

#print(soup.get_text())

officers = soup.find_all("h3")

#for officer in officers:
    #if (officer.string != "Available"):
        #print(officer.string)

positions = soup.find_all("h2")
del positions[0]
for position in positions:
    print(position.string)

for i in range(len(positions)):
    print(positions[i].string + ": " + officers[i].string)