import requests

api_key = "43b8044658014bffa8711de2dabde18a"
url = (
    "https://newsapi.org/v2/top-headlines?"
    "country=us&category=business&apiKey=43b8044658014bffa8711de2dabde18a"
)
# Make request to the API
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n")
