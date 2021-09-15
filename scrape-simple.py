from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".storylink")
votes = soup.select(".score")
subtext = soup.select(".subtext")

# print(links[0])
# print(links[0].get("href"))  # value of href
# print(links[0].getText())  # text within the tags

# titles = []
# hrefs = []
# for stuff in links:
#     titles.append(stuff.getText())
#     hrefs.append((stuff.get("href")))
#
# new_stuff = list(zip(titles, hrefs))
# print(new_stuff)


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
