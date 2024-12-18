import requests

api_key = '5eaf36213f174ed0bed88f2ba2924977'
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-11-18&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


for article in content['articles']:
    print(article["title"])