import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url=URL).text, "html.parser")

titles = soup.select(selector=".article-title-description__text .title")
titles = [titles.text for titles in titles]
print(titles)

with open(file="movies.txt",mode="a") as file:
    for i in range (len(titles)):
        file.write(f"{titles[-(i+1)]}\n")