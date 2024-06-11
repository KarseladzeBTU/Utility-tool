import requests

def url_shorten(inputed_url):
    url = f"https://ulvis.net/API/write/get?url={inputed_url}"
    result = requests.get(url)
    jsoned_info = result.json()
    shortened_url = jsoned_info["data"]["url"]
    return shortened_url
