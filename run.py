import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
# First, we're importing our Flask class.

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
# We're then creating an instance of this and storing it in a variable called 'app'.
# The first argument of the Flask class, is the name of the application's module - our package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates and static files.

# We're then using the app.route decorator.
# In Python, a decorator starts with the @ symbol, which is also called pie-notation.
# Effectively, a decorator is a way of wrapping functions.


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)        


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

# We can "import os" from the standard Python library, 
# and then we're going to reference this built-in variable and say that:

# if name is equal to "main" (both wrapped in double underscores), 
# then we're going to run our app with the following arguments.

# The 'host' will be set to os.environ.get("IP"), and I will set a default of "0.0.0.0".
# We're using the os module from the standard library to get the 'IP' environment variable if it exists, 
# but set a default value if it's not found.

# It will be the same with 'PORT', but this time, we're casting it as an integer,
# and I will set that default to "5000", which is a common port used by Flask.

# We also need to specify "debug=True", 
# because that will allow us to debug our code much easier during the development stage.

#The word 'main' wrapped in double-underscores (__main__) 
# is the name of the default module in Python.

# One thing I'd like you to take note of, is that we should never have "debug=True" in a production application, 
# or when we submit our projects for assessment.

# You should only have debug=True while testing your application in development mode, 
# but change it to debug=False before you submit your project.