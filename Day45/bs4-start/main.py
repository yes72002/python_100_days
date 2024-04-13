from bs4 import BeautifulSoup

# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name) # title
# print(soup.title.string) # Angela's Personal Site
# # print(soup.prettify()) # indent your soup
# # print(soup.a) # the first a tag
# # print(soup.li)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # 直接用class會跟key word衝突
# print(section_heading)
# # print(section_heading.name)
# # print(section_heading.get_text())
# # print(section_heading.get("class"))

# # first matching item
# company_url = soup.select_one(selector="p a") # <p>裡面的<a>
# print(company_url)
# print(company_url.get("href"))

# name = soup.select_one(selector="#name") # CSS selector
# print(name)

# headings = soup.select(".heading") # day 43, class selector
# print(headings)

import requests

response = requests.get("https://news.ycombinator.com/show")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)


# all_anchor_tags = soup.find_all(name="td", class_="title")
# # print(all_anchor_tags)

aritcles = soup.find_all(name="span", class_="titleline")
# print(aritcles)
# aritcle_text
# aritcle_text = aritcle_tag.get_text()
# print(aritcle_text)
# # aritcle_link
# aritcle_link = soup.find(name="span", class_="titleline").find(name="a").get("href")
# print(aritcle_link)
# # aritcle_upvote
# aritcle_upvote = soup.find(name="span", class_="score").get_text()
# print(aritcle_upvote)

aritcle_texts = []
aritcle_links = []
for aritcle_tag in aritcles:
    text = aritcle_tag.get_text()
    aritcle_texts.append(text)
    link = aritcle_tag.find(name="a").get("href")
    aritcle_links.append(link)

aritcle_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(aritcle_texts)
print(aritcle_links)
print(aritcle_upvotes)

max_index = aritcle_upvotes.index(max(aritcle_upvotes))

print(aritcle_texts[max_index])
print(aritcle_links[max_index])


