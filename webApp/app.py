from flask import Flask, render_template, request
import json
import random # JUST FOR TESTING

app = Flask(__name__)
app.config['DEBUG'] = True

# /jobs?Web=1&Python=1&R=1&SQL=1
@app.route('/jobs')
def jobs():
    # extracting query string arguments
    js_rating     = request.args.get('Web') # HTML, CSS, & Javascript
    python_rating = request.args.get('Python')
    r_rating      = request.args.get('R')
    sql_rating    = request.args.get('SQL')

    # use these ratings and their expected role: entry-level, junior-level, or senior-level
    # to find a given number (say 5) of job recommendations

    # dummy object
    # postings = [
    #     {
    #         'position': 'Data Scientist',
    #         'company': 'Google',
    #         'location': 'Chicago, IL',
    #         'url': 'https://www.google.com/'
    #     },
    #     {
    #         'position': 'Data Scientist',
    #         'company': 'Microsoft',
    #         'location': 'Chicago, IL',
    #         'url': 'https://www.microsoft.com/'
    #     },
    #     {
    #         'position': 'Data Scientist',
    #         'company': 'Amazon',
    #         'location': 'Chicago, IL',
    #         'url': 'https://www.amazon.com/'
    #     },
    #     {
    #         'position': 'Data Scientist',
    #         'company': 'Facebook',
    #         'location': 'Chicago, IL',
    #         'url': 'https://www.facebook.com/'
    #     },
    #     {
    #         'position': 'Data Scientist',
    #         'company': 'Apple',
    #         'location': 'Chicago, IL',
    #         'url': 'https://www.apple.com/'
    #     }
    # ]

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
    # skills    = calculate_skills()
    # pays      = calculate_pays()
    # locations = calculate_locations()

    # also dummy objects, will need to be calculated above
    keywords = {
        'labels'  : ['HTML, CSS, & JavaScript', 'Python', 'R', 'SQL', 'C++'],
        'dataset' : [
            {'source': 'GitHub Jobs', 'data': [10, 20, 30, 40, 50] },
            {'source': 'USA Jobs',    'data': [10, 20, 30, 40, 50] }
        ]
    }

    pays = {
        'labels' : ['< $50,000', '$50,000 – 75,000', '$75,001 – 100,000', '> $100,000'],
        'dataset' : [
            {'source': 'GitHub Jobs', 'data': [30, 40, 50, 60] },
            {'source': 'USA Jobs',    'data': [30, 40, 50, 60] }
        ]
    }

    locations = {
        'labels' : ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'dataset' : [
            {'source': 'GitHub Jobs', 'data': [70, 80, 90, 100, 110] },
            {'source': 'USA Jobs',    'data': [70, 80, 90, 100, 110] }
        ]
    }

    return render_template('index.html', keywords=keywords,
                                         pays=pays,
                                         locations=locations)
