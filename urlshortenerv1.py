'''
import hashlib

def shorten_url(url):
    hash_object = hashlib.md5(url.encode())
    short_code = hash_object.hexdigest()[:6]
    return "short.ly/" + short_code

url = "https://www.google.com"
print(shorten_url(url))'''

import pyshorteners

url = input("Enter the URL to shorten: ")

shortener = pyshorteners.Shortener()
url_short = shortener.tinyurl.short(url)

print("Original URL: ", url)
print("Shortened URL: ", url_short)