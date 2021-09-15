from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".storylink")  # selects and compiles all instances which has html class of 'storylink' in a list 
votes = soup.select(".score")  # selects and compiles all instances which has html class of 'score' in a list
subtext = soup.select(".subtext")  # same as the above two cases

# print(links[0])
# print(links[0].getText())  # text within the tags
# print(links[0].get("href"))  # value of href

# article_tag = soup.find(name="a", class_="storylink")  # return the first 'a' tag which has an html class 'storylink'
# article_text = article_tag.getText()  # text within the tags
# article_link = article_tag.get("href")  # value of href

# article_tags = soup.find_all(name="a", class_="storylink")  # returns all the instances where the tag is 'a' and has an html class of 'storylink' in a list
# links = soup.select(".storylink")  # does the same as above

def sort_stories_by_votes(hacker_news_list):
    # return sorted(hacker_news_list, key=lambda k: k["votes"]) # sorts in ascending order

    # descending order
    return sorted(hacker_news_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hacker_news.append(
                    {"title": title, "link": href, "votes": points})
    # return hacker_news
    return sort_stories_by_votes(hacker_news)


pprint.pprint(create_custom_hacker_news(links, subtext))
