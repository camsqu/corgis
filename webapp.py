from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def main():
    with open('static/immigration.json') as immigration_data:
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

@app.route("/databycountry")
def render_cdata():
    countryvalue = get_country_options()
    return render_template('countrydata.html', value = countryvalue)

@app.route("/admissions")
def render_admit():
    return render_template('admissions.html')

@app.route("/yeardata")
def render_ydata():
    return render_template('yeardata.html')

@app.route("/visual")
def render_visual():
    return render_template('visual.html')

def number_of_countries():
    countryTotal = []
    country = countries[0]["Country"]
    for c in countries:
        if c["Country"] in countryList:
            countryTotal.append([c["Country"]])

def get_country_options():
     with open('static/immigration.json') as immigration_data:
         countries = json.load(immigration_data)
         count = 0
         country = []
         for c in countries:
             if c["Country"] not in country:
                 country.append(c["Country"])
                 value = ""
         for c in country:
            value += Markup("<option value=\"" + c + "\">" + c + "</option>")
         return value
def country_response(country):
    with open('static/immigration.json') as immigration_data:
        countries = json.load(immigration_data)
    for z in countries:
        if z["Country"] == country:
            return "Immigration data for " + z["Country"] + " Enforcement:" + " Non-criminal:" + str(z["Data"]["Enforcement"])
            # formatting this return line requires creating a jinja variable for the seperate parts of this line and implement into the HTML code.
@app.route("/response")
def render_response():
    country = request.args['Country']
    return render_template("countrydata.html",value=get_country_options(),fact=country_response(request.args["Country"]))

if __name__ == '__main__':
    app.run(debug=True)
