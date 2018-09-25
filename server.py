from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"



                                          ###---Variables---###

MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE
###-HOME-###

@app.route("/") #add homepage url
def display_homepage():

    if 'username' in session:          
        return redirect('/top-melons')
    else:
        return render_template('homepage.html') #this is a known user ?(session) no?(go to homepage


###-SESSIONS-###

@app.route("/get-name")
def store_username_session(): # session for cookies

    session['username'] = request.args.get('username') # add user info to session

    return redirect('/top-melons') # -->(top_melons page)
 
###-MELONS-###

@app.route("/top-melons")  # <-- (in from homepage)
def display_top_melons():
    ''' 4 top rated melons '''

    fav_melons = MOST_LOVED_MELONS #dictionary store in var

    if 'username' in session:
        return render_template('/top-melons.html', fav_melons=fav_melons) # returning user ? --> (top-melons page)

    else:
        return redirect('/')# not a known user ? --> homepage


###-THANK USER-###

@app.route("/love-melon", methods=["POST"]) 
def increase_melon_love():
   # num_loves = []

    melon_loved = request.form.get("melon_love","MELON_NOT_FOUND") # get info(melon form) set to var



    #print(melon_loved)

    MOST_LOVED_MELONS[melon_loved]['num_loves'] += 1 # add one to that var

    return render_template('thank-you.html') # --> to thank you page






    #print(MOST_LOVED_MELONS[melon_loved])



###---------------###

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
