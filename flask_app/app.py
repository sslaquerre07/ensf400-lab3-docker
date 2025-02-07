from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://www.progolfweekly.com/wp-content/uploads/2017/11/79531321.jpg",
    "https://www.progolfweekly.com/wp-content/uploads/2017/11/gettyimages-81685519.jpg",
    "https://www.progolfweekly.com/wp-content/uploads/2017/11/arnold-palmer-1960-us-open.jpg",
    "https://www.progolfweekly.com/wp-content/uploads/2017/11/179421592.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")