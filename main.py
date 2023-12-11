import json
import requests
import asyncio
  
GENRES = "Comedy"
RSCORE = 60
STOP = 3
URL = "https://rotten-tomatoes-api.ue.r.appspot.com/search/"

def main():
    req_movie_list = []
    
    for movie in movies_name(STOP):
        
        url_search = URL + movie
        m_detail = movie_detail(url_search)
        if m_detail and check_genres_rscore(m_detail):
            req_movie_list.append((movie , m_detail[0]["weighted_score"]))
    print(req_movie_list)

async def movie_detail(url):
    response = requests.get(url=url)
    if not response.text == "Internal Server Error":
        m_detail = response.json()["movies"]
        return (m_detail)
    return None
        

def check_genres_rscore(m_detail):
    return GENRES in m_detail[0]["genres"] and RSCORE <= m_detail[0]["weighted_score"] 
   


def movies_name(stop):
    with open ("/home/piyush/expo/csvmovie.json" , mode="r") as file:
        file_content = json.load(file)
        movie_list = file_content["movies"]
        return movie_list[:stop]
    
        

main() 