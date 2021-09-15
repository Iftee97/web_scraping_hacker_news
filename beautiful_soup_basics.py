from bs4 import BeautifulSoup
import requests

# ---------
print("\n")
# ---------

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# returns the first instace where the tag is 'a' and has an html class of 'storylink'
article_tag = soup.find(name="a", class_="storylink")
# print(article_tag)
# print(article_tag.getText())  # text within the tags
# print(article_tag.get("href"))  # value of href


# returns all the instances where the tag is 'a' and has an html class of 'storylink'
article_tags = soup.find_all(name="a", class_="storylink")
# print(article_tags[0])
# print(article_tags[0].getText())  # text within the tags
# print(article_tags[0].get("href"))  # value of href


# returns all instances which has html class of 'storylink' in a list
# same as above with soup.find_all()
links = soup.select(".storylink")
# print(links[0])
# print(links[0].getText())  # text within the tags
# print(links[0].get("href"))  # value of href


# ---------
print("\n")
# ---------
