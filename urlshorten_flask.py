import random # imports the random module
import string # imports the string module

from flask import Flask, render_template, redirect, request # this is a module that allows us to create a web application and handle requests, redirect, and render templates


app = Flask(__name__) # app is a variable that stores the Flask application

shortened_urls = {} # this is a dictionary to store the shortened urls

def generate_short_url(length=6): # this is a function that generates a short url, the argument length is 6 will be used to generate the short url length
    chars = string.ascii_letters + string.digits # this is a string of characters that will be used to generate the short url
    short_url = "".join(random.choice(chars) for _ in range(length)) # this is a string of characters that will be used to generate the short url
    return short_url # returns the short url as a string

@app.route('/', methods=['GET', 'POST']) # GET and POST are the methods that are used to handle the requests and @app.route is a decorator that is used to define a route for the web application
def index(): # this function is used to handle the requests
    if request.method == 'POST': # if the method is POST, the long url is stored in the request form
        long_url = request.form['long_url'] # the variable long_url is stored in the request form
        short_url = generate_short_url() # short_url is the variable that stores the generated short url
        while short_url in shortened_urls: # while the short url is in the shortened urls, the short url is generated again
            short_url = generate_short_url() # the short url is generated again until it is not in the shortened urls
        
        shortened_urls[short_url] = long_url # variable shortened_urls is a dictionary that stores the short url and the long url
        return f"Shortened URL: {request.url_root}{short_url}" # returns the shortened url as a string
    return render_template('index.html') # returns a render template of the index.html file

@app.route("/<short_url>") # @app.route is a decorator that is used to define a route for the web application
def redirect_url(short_url): # this function is used to redirect the short url to the long url
    long_url = shortened_urls.get(short_url) # the variable long_url is stored in the shortened urls dictionary
    if long_url: # if the long url is not None, the long url is returned
        return redirect(long_url) # the long url is returned
    else: # if the long url is None, the URL not found error is returned
        return "URL not found", 404 # the URL not found error is returned and 404 is the error code

if __name__ == '__main__': # if the name of the module is __main__, the app is run in debug mode
    app.run(debug=True) # the app runs in debug mode