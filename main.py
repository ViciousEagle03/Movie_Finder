import json
import aiohttp
import asyncio

GENRES = "Horror"
RSCORE = 60
STOP = 1000
URL = "https://rotten-tomatoes-api.ue.r.appspot.com/search/"

async def main():
    url_search_list=[]
    for movie in movies_name(STOP):
        url_search = URL + movie
        url_search_list.append(url_search)
        
    await asyncio.gather(*[movie_detail(url) for url in url_search_list])

async def movie_detail(url):
    connector = aiohttp.TCPConnector(force_close=True,limit=20)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
        
            async with session.get(url=url) as response:
                response_text = await response.text()
                
                if not response_text == "Internal Server Error" and response.headers['Content-Type'] == 'application/json' and response.status == 200:
                    m_detail = await response.json()
                    
                    if m_detail and check_genres_rscore(m_detail):
                        print((m_detail["movies"][0]["name"], m_detail["movies"][0]["weighted_score"]))
    except:
        print("dikkat")
                      
def check_genres_rscore(m_detail):
    if m_detail and "movies" in m_detail and m_detail["movies"]:
        return (
            GENRES in m_detail["movies"][0]["genres"]
            and RSCORE <= m_detail["movies"][0]["weighted_score"]
        )
    else:
        return False
    #return GENRES in m_detail["movies"][0]["genres"] and RSCORE <= m_detail["movies"][0]["weighted_score"] 
def movies_name(stop):
    with open ("/home/piyush/expo/moviename.json" , mode="r") as file:
        file_content = json.load(file)
        movie_list = file_content["movies"]
        return movie_list[:stop]
    
        

asyncio.run(main())

