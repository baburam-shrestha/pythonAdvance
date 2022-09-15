from flask import Flask, json
app = Flask(__name__)
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
@app.route("/main/", methods='POST')
def main():
    return posts 

if __name__ == "__main__":
    app.run(debug=True)