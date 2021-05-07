from bs4 import BeautifulSoup
import requests


url='https://github.com/clear-code-projects/Snake/tree/main/Graphics'

response_from_url= requests.get(url)
soup= BeautifulSoup(response_from_url.content,'html.parser')

images_location= soup.find_all('a',class_="js-navigation-open Link--primary")

for links in images_location:
    image_link=f"https://github.com{links['href']}/?raw=true"
    request_img_link=requests.get(image_link)
    title= links['title']
    with open(f'{title}','wb') as f:
        f.write(request_img_link.content)
print("Succesfully Downloaded")