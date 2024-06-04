import requests 
from bs4 import BeautifulSoup 
from flask import flash

def search_(search) ->str:
    return (f"https://m.manganelo.com/search/story/{search}")



def get_search_result(url):
    response = requests.get(url) # here we are making http get request
    soup = BeautifulSoup(response.content , 'html.parser') #parsing the html content
    links= soup.find_all('a',{"class" : "item-img bookmark_check"} )
    div= soup.find('div' , class_ ="panel-search-story" )
    div2= div.find_all('div' , class_ ="search-story-item")
    
    
    links2 = []
    img2 = []
    text2= []
   
   
    for link  in links:
        text2.append(link.get('title'))
        links2.append(link.get('href'))   
    for link in div2:
        x = link.find('img')
        img2.append(x.get('src'))  
        
   
    return text2,links2,img2

clicked_url = None
def get_chapters(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    chapters = soup.find_all('a', {"class": "chapter-name text-nowrap"})
    links = []
    title =[]
    for chapter in chapters:
        links.append(chapter.get('href'))
        title.append(chapter.get('title'))
    return links,title

def get_images(url) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find_all('img', class_ ="reader-content")
    pages = []
   
    for _ in img:
        pages.append(_.get('src'))

    return pages





    #extracting the url of manga pages(which are obv images) and store in pages variable
   