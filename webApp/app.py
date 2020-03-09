from flask import Flask, render_template, request
import json
import random # JUST FOR TESTING

app = Flask(__name__)
app.config['DEBUG'] = True

# e.g., /jobs?Web=1&Python=1&R=1&SQL=1
@app.route('/jobs')
def jobs():
    # extracting query string arguments
    web_rating    = request.args.get('Web')    # HTML, CSS, & Javascript
    python_rating = request.args.get('Python')
    r_rating      = request.args.get('R')
    sql_rating    = request.args.get('SQL')

    # postings = get_job_recommendations(5, web_rating, python_rating, r_rating, sql_rating)

    postings = [
        [
            'Data Scientist',
            'Google',
            'Chicago, IL',
            'https://www.google.com/'
        ],
        [
            'Data Scientist',
            'Microsoft',
            'Chicago, IL',
            'https://www.microsoft.com/'
        ],
        [
            'Data Scientist',
            'Amazon',
            'Chicago, IL',
            'https://www.amazon.com/'
        ],
        [
            'Data Scientist',
            'Facebook',
            'Chicago, IL',
            'https://www.facebook.com/'
        ],
        [
            'Data Scientist',
            'Apple',
            'Chicago, IL',
            'https://www.apple.com/'
        ]
    ]
    random.shuffle(postings)
    return json.dumps(postings)

@app.route('/')
def index():
    data = json.loads(open("webApp/static/data.json").read())
    numJobs = 120
    return render_template('index.html', numJobs=numJobs,
                                         keywords=data["keywords"],
                                         pays=data["pays"],
                                         locations=data["locations"])
