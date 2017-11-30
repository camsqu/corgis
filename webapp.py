from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def main():
    with open('immigration.json') as immigration_data:
        countries = json.load(immigration_data)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/about")
def render_about():
    return render_template('about.html')

@app.route("/overall")
def render_overall():
    return render_template('overall.html')

def number_of_countries():
    countryTotal = {}
    country = countries[0]['Country']
