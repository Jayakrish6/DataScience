from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.google.com").text
soup = BeautifulSoup(html, 'html5lib')

first_paragraph = soup.find('p')

#print(soup)
print(first_paragraph)
print("=====================================")

first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

print(first_paragraph_text)


print("=====================================")
print(first_paragraph_words)


print("=====================================")

#first_paragraph_id = soup.p['id'] # raises KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id') # returns None if no 'id'
print(first_paragraph_id2)
print("=====================================")
print(first_paragraph_id2)

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
    if 'important' in p.get('class', [])]

url = "http://shop.oreilly.com/category/browse-subjects/" + \
"data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')
print(soup)

