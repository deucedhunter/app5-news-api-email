import requests
from send_email import send_email

topic = "tesla"

api_key = '5eaf36213f174ed0bed88f2ba2924977'
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-11-18&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for article in content['articles'][:20]:
    body = (f"Subject: Today's News\n"
            f"{body}{article['title']}\n"
            f"{article['description']}+|\n"
            f"{article['url']}\n\n")

print("Trying to send email...")
send_email(body)