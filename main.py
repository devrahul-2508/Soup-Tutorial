import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

#Step 1: GET HTML

r = requests.get(url)
htmlcontent = r.content
print(htmlcontent)

#Step 2: Parse HTML
soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())
#Step 3: HTML Tree traversal


#Commonly used types of objects

#Get the title of HTML Page
title = soup.title
print(title)
print(type(title)) #1. TAG
print(type(title.string)) #2. NavigableString
print(type(soup)) #3. BeautifulSoup

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string)) #4. Comment




#Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)



print(anchors)

#Get first element in html page
print(soup.find('p'))
#Get classes of any element in the html page
print(soup.find('p')['class'])

#Find all the elements with class lead
print(soup.find_all("p",class_="mt-2"))

#Get the text from the elements tags/soup
print(soup.find('p').get_text())

#Get all anchor tags
anchors = soup.find_all('a')
#Get all the links from the page
all_links = set()
for link in anchors:
    if(link['href'] != '#'):
       linkText = "https://codewithharry.com"+link['href']
       all_links.add(link)
       print(linkText)

navbarSupportedContent = soup.find(id='search-toggle')
print(navbarSupportedContent.contents)

# .contents - A tag's children are available as a list
# .children - A tag's children are available as generator
for elem in navbarSupportedContent.contents:
    print(elem)

for item in navbarSupportedContent.strings:
    print(item)

print(navbarSupportedContent.parent.prettify())

for item in navbarSupportedContent.parents:
    print(item.name)


print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

print(soup.select('#loginModal'))
