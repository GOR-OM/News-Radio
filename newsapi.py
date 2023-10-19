import requests
import pyttsx3


api_key = '7684b9a0b5e94656819efef1c0ed1b85'  


base_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business'

params = {
    'country': 'us', 
    'apiKey': api_key
}


response = requests.get(base_url, params=params)

if response.status_code == 200:
    news_data = response.json()
    if 'articles' in news_data:
        top_news = news_data['articles']
        if top_news:
            engine = pyttsx3.init()
            engine.say("Here are the top news headlines:")
            engine.runAndWait()
            for index, article in enumerate(top_news, start=1):
                title = article.get('title', 'Title not available')
                engine.say( f"News {index}: {title}" )
                engine.runAndWait()
                

        else:
            print("No top news found.")
    else:
        print("No articles found in the response.")
else:
    print("Failed to retrieve top news. Status code:", response.status_code)
