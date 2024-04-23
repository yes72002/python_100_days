from bs4 import BeautifulSoup
import requests

URL = "https://www.audible.com/search?keywords=book&node=18573211011"
response = requests.get(URL)
yc_web_page = response.text
# print(yc_web_page)

# with open("website.html", mode="w") as file:
#     file.write(f"{yc_web_page}\n")

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

booknames = soup.select(selector=".bc-list-item .bc-heading.bc-color-link")
# print(len(booknames)) # 20
# print(booknames)

subtitles = soup.select(selector=".bc-col-6 .bc-row-responsive .bc-col-12 .bc-list-nostyle")
# print(len(subtitles)) # 20
# print(subtitles)
# for subtitle in subtitles:
#     print("----------------")
#     print(subtitle)

authorlabels = soup.find_all(name="li", class_="bc-list-item authorLabel")
# print(authorlabels)

runtimelabels = soup.find_all(name="li", class_="bc-list-item runtimeLabel")
# print(len(runtimelabels)) # 20
# print(runtimelabels)

releaselabels = soup.find_all(name="li", class_="bc-list-item releaseDateLabel")
# print(len(releaselabels)) # 20
# print(f"{releaselabels}")

languagelabels = soup.find_all(name="li", class_="bc-list-item languageLabel")
# print(len(languagelabels)) # 20
# print(f"{languagelabels}")

ratingslabels = soup.find_all(name="li", class_="bc-list-item ratingsLabel")
# print(len(ratingslabels)) # 20
# print(f"{ratingslabels}")
# for ratingslabel in ratingslabels:
#     print("----------------")
#     print(ratingslabel)

bookname_texts = []
subtitle_texts = []
authorlabel_texts = []
runtime_texts = []
release_texts = []
language_texts = []
stars_texts = []
ratings_texts = []

for bookname in booknames:
    aaa = bookname.find(name="a").get_text()
    aaa = aaa.replace("\xae","")
    bookname_texts.append(aaa)

for subtitle in subtitles:
    try:
        aaa = subtitle.select_one(selector=".bc-list-item.subtitle").find(name="span").get_text()
        aaa = aaa.replace("\xae","")
        subtitle_texts.append(aaa)
    except:
        subtitle_texts.append("-")

for authorlabel in authorlabels:
    author_element = []
    authors_list = authorlabel.find(name="span").find_all(name="a")
    for authors in authors_list:
        aaa = authors.get_text()
        author_element.append(aaa)
    authorlabel_texts.append(", ".join(author_element))

for runtime in runtimelabels:
    aaa = runtime.find(name="span").get_text()
    aaa = aaa.split("Length: ")[1].replace("\n","")
    runtime_texts.append(aaa)

for release in releaselabels:
    aaa = release.find(name="span").get_text()
    aaa = aaa.split("Release date:\n")[1].replace("\n","").replace(" ","")
    release_texts.append(aaa)

for language in languagelabels:
    aaa = language.find(name="span").get_text()
    aaa = aaa.split("Language:\n")[1].replace("\n","").replace(" ","")
    language_texts.append(aaa)

for stars in ratingslabels:
    try:
        aaa = stars.find(name="span", class_="bc-pub-offscreen").get_text()
        stars_texts.append(aaa)
    except:
        aaa = stars.find(name="span", class_="bc-color-secondary").get_text()
        stars_texts.append(aaa)

for ratings in ratingslabels:
    aaa = ratings.find(name="span", class_="bc-text bc-size-small bc-color-secondary").get_text()
    ratings_texts.append(aaa)

# print(bookname_texts)
# print(subtitle_texts)
# print(authorlabel_texts)
# print(runtime_texts)
# print(release_texts)
# print(language_texts)
# print(stars_texts)
# print(ratings_texts)

# print(len(bookname_texts))
# print(len(subtitle_texts))
# print(len(authorlabel_texts))
# print(len(runtime_texts))
# print(len(release_texts))
# print(len(language_texts))
# print(len(stars_texts))
# print(len(ratings_texts))

with open('day_93_report.csv', 'w') as file:
    file.write(f"bookname, subtitle, author, run time, release date, language, stars, ratings\n")
    for i in range(0, len(bookname_texts)):
        file.write(
            f'{bookname_texts[i]}, '
            f'"{subtitle_texts[i]}", '
            f'"{authorlabel_texts[i]}", '
            f'"{runtime_texts[i]}", '
            f'"{release_texts[i]}", '
            f'"{language_texts[i]}", '
            f'"{stars_texts[i]}", '
            f'"{ratings_texts[i]}" '
            f'\n'
        )

print(f"Write data in the report.csv")



