import requests

import send_email

topic = "business"

api_key = "43b8044658014bffa8711de2dabde18a"
url = (
    "https://newsapi.org/v2/top-headlines?"
    "country=us&"
    f"category={topic}&"
    "apiKey=43b8044658014bffa8711de2dabde18a&"
    "language=en"
)
# Make request to the API
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article titles and descriptions
# this way gets rid of any None values
body = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = (
            "Subject: Today's News"
            + "\n"
            + body
            + article["title"]
            + "\n"
            + article["description"]
            + "\n"
            + article["url"]
            + "\n\n"
        )


# Another way to do it is
# This way will keep the None values but still send
# body = ""
# for article in content["articles"]:
#     body = (
#         body + (article["title"] or "") + "\n" + (article["description"] or "") + "\n\n"
#     )

body = body.encode("utf-8")
send_email.send_email(body)
