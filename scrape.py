import requests
from bs4 import BeautifulSoup
import pprint

print("\n")


res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
# print(res.text) # prints the source page (html) for the above url
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
# print(soup) # prints cleaner source page (html) for the above url

# print(soup.select(".score")) # list of all the tags that have a class 'score'
# print(soup.select(".storylink")) # list of all the <a></a> tags that have class 'storylink'

links = soup.select(".storylink")
subtext = soup.select(".subtext")

links2 = soup2.select(".storylink")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hacker_news_list):
    return sorted(hacker_news_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news_list = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hacker_news_list.append(
                    {"title": title, "link": href, "votes": points})

    return sort_stories_by_votes(hacker_news_list)


pprint.pprint(create_custom_hacker_news(mega_links, mega_subtext))


print("\n")
