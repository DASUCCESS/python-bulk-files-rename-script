import requests
from bs4 import BeautifulSoup as bs

# user = input("Input what you want to search: ")
# url = "https://www.chegg.com/"+user

user = input("Input username to search: ")
 url = "https://github.com/"+user
            #print(url)
# use request we imported to get the url of your choice
requests_url = requests.get(url)
            #print(requests_url)
            # print(request_url.content)
soup = bs(requests_url.content, "html.parser")
# print(soup.prettify())
#soup = bs(request_url.content, "html.parser")
            # print(soup.prettify()
# use soup to find and get your content now
            # soup_get = soup.find("a", {"class": "Link--secondary no-underline no-wrap"})
            # find_all = soup.find_all('a')
            # print(find_a.get('Link--secondary no-underline no-wrap'))
profile_image =soup.find('img', {'alt': 'Avatar'})['src']
followers =soup.find('a', {'class': 'Link--secondary no-underline no-wrap'})
print(profile_image)
print(followers.prettify())

# using for loop to access multiples site title and description
#using same url as above we have

# for text in soup.find('div', {"class": "active"}):
#     Title = text.h2.a.text
#     Paragraph = text.p.text
#     print(Title)
#     print(Paragraph)
