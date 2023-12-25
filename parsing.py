# TODO line up and parse data for price, image and title 

from bs4 import BeautifulSoup   

with open('output.html', 'r', encoding='utf-8') as f:
    page_html = f.read()

soup = BeautifulSoup(page_html, 'html.parser')
img_url = soup.find_all('img', class_='img')
title = soup.find_all('div', class_='native-text')
price = soup.find_all('span', class_='f2')
#print(img_url)

#Save text only from tile into a list

for t in title:
    title_text = t.get_text().strip()
    print(f"Title: {title_text}")
    
for p in price:    
    price_text = p.get_text().strip()
    print(f"Price: {price_text}")

for i in img_url:
    img_url = i['src']
    print(f"Image URL: {img_url}")