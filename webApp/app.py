from flask import Flask, render_template, request
from .webScraper.DataBase.PopulateDB import query_github, query_usa
import json, random, os
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/<state>/jobs')
def jobs(state):
    # URI-encoded; e.g., /jobs?HTML,CSS,JavaScript=1&Python=1&R=1&SQL=1
    max_value        = 0
    max_search_terms = ""

    total = 0

    for arg in request.args:
        value = int(request.args[arg])
        total += value

        if value >= max_value:
            max_value = value
            max_search_terms += arg if max_search_terms == "" else ("," + arg)

    role = 'Entry-level'
    if   total >= 16: role = 'Senior-level'
    elif total >= 10: role = 'Junior-level'

    # e.g., state = 'IL'; max_search_terms = 'HTML,CSS,Javascript'
    postings = query_usa(state, role, max_search_terms)
    '''
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
    '''
    return json.dumps(postings)


def get_num_jobs():
    # just a dummy value at this point
    return 120


def get_json_by_source(json, datatype, labels, skills=("Artificial Intelligence", "Deep Learning", "Machine Learning", "Computer Engineering")):
  zipped = zip(json[skills[0]][datatype]["datasets"],
               json[skills[1]][datatype]["datasets"],
               json[skills[2]][datatype]["datasets"],
               json[skills[3]][datatype]["datasets"])
  zipped = list(zipped)

  template = {
    'labels' : labels,
    'datasets': [
      {"label": "GitHub Jobs", "data": [0, 0, 0, 0, 0]},
      {"label": "USA Jobs",    "data": [0, 0, 0, 0, 0]}
    ]
  }

  for i, data in enumerate(template['datasets']):
    """
    zipped[i] has this form:
    (
      {'label': 'GitHub Jobs', 'data': [10, 20, 30, 40, 50]},
      {'label': 'GitHub Jobs', 'data': [10, 20, 30, 40, 50]},
      ...
    )
    """
    new_data = [0] * len(labels)

    for source_data in zipped[i]:
      for i, datapoint in enumerate(source_data['data']):
        new_data[i] += datapoint

    data['data'] = new_data

  return template


def get_json_by_skill(json, datatype, labels, skills=("Artificial Intelligence", "Deep Learning", "Machine Learning", "Computer Engineering")):
    template = {
        'labels': labels,
        'datasets': [
            {"label": skills[0], "data": [0, 0, 0, 0, 0]},
            {"label": skills[1], "data": [0, 0, 0, 0, 0]},
            {"label": skills[2], "data": [0, 0, 0, 0, 0]},
            {"label": skills[3], "data": [0, 0, 0, 0, 0]},
        ]
    }

    for i, data in enumerate(template['datasets']):
        new_data = [0] * len(labels)

        for source_data in json[skills[i]][datatype]["datasets"]:
            for j, elem in enumerate(source_data['data']):
                new_data[j] += elem

        data['data'] = new_data

    return template


@app.route('/')
def index():
    data = json.loads(open("webApp/static/data.json").read())
    num_jobs = get_num_jobs()

    keywords_source  = get_json_by_source(data, "keywords", ["HTML, CSS, & JavaScript", "Python", "R", "SQL", "C++"])
    pays_source      = get_json_by_source(data, "pays", ["< $50,000", "$50,000 - $75,000", "$75,001 - $100,000", "> $100,000"])
    locations_source = get_json_by_source(data, "locations", ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"])

    keywords_skill  = get_json_by_skill(data, "keywords", ["HTML, CSS, & JavaScript", "Python", "R", "SQL", "C++"])
    pays_skill      = get_json_by_skill(data, "pays", ["< $50,000", "$50,000 - $75,000", "$75,001 - $100,000", "> $100,000"])
    locations_skill = get_json_by_skill(data, "locations", ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"])

    return render_template('index.html', num_jobs         = num_jobs,
                                         keywords_source  = keywords_source,
                                         pays_source      = pays_source,
                                         locations_source = locations_source,
                                         keywords_skill   = keywords_skill,
                                         pays_skill       = pays_skill,
                                         locations_skill  = locations_skill)
