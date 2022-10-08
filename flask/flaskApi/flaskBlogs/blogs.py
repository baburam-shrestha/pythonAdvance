from flask import Flask, render_template

app = Flask(__name__)
# export FLASK_DEBU=1 on command line provide the easyness to runa nd debug the program

posts=[
    {
        "author":"Baburam Shrestha",
        "title": "Moving toward the himalaya",
        "content":"it is about the himalaya and is about the life of himalayan",
        "posted_at":"February 12 2020"
    },
    {
        "author":"Babu silwal",
        "title": "Moving toward the hill",
        "content":"it is about the himalayan",
        "posted_at":"March 12 2020"
    },
    {
        "author":"raam Shrestha",
        "title": "toward the himalaya",
        "content":"it is about the himalayan",
        "posted_at":"january 12 2020"
    }
]
@app.route("/")
@app.route("/home/")
def home_page():
    return render_template('home.html',title="Home")

@app.route("/blog/")
def blog_page():
    return render_template('blog.html',title="Blog",posts=posts)

@app.route("/contact/")
def contact_page():
    return render_template('contact.html',title="Contact")

@app.route("/about/")
def about_page():
    return render_template('about.html',title="About")

# it is for running the flask application using python  file run command i.e. python3 blogs.py
if __name__ == "__main__":
    app.run(debug=True)