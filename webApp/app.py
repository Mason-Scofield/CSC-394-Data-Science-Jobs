from flask import Flask, render_template, request
from .webScraper.DataBase.queryDB import query, count
import json, re
app = Flask(__name__)
app.config['DEBUG'] = True


states = {
    'Alaska'               :  'AK' ,
    'Alabama'              :  'AL' ,
    'Arkansas'             :  'AR' ,
    'Arizona'              :  'AZ' ,
    'California'           :  'CA' ,
    'Colorado'             :  'CO' ,
    'Connecticut'          :  'CT' ,
    'DistrictofColumbia'   :  'DC' ,
    'District of Columbia' :  'DC' ,
    'Delaware'             :  'DE' ,
    'Florida'              :  'FL' ,
    'Georgia'              :  'GA' ,
    'Hawaii'               :  'HI' ,
    'Iowa'                 :  'IA' ,
    'Idaho'                :  'ID' ,
    'Illinois'             :  'IL' ,
    'Indiana'              :  'IN' ,
    'Kansas'               :  'KS' ,
    'Kentucky'             :  'KY' ,
    'Louisiana'            :  'LA' ,
    'Massachusetts'        :  'MA' ,
    'Maryland'             :  'MD' ,
    'Maine'                :  'ME' ,
    'Michigan'             :  'MI' ,
    'Minnesota'            :  'MN' ,
    'Missouri'             :  'MO' ,
    'Mississippi'          :  'MS' ,
    'Montana'              :  'MT' ,
    'National'             :  'NA' ,
    'NorthCarolina'        :  'NC' ,
    'North Carolina'       :  'NC' ,
    'NorthDakota'          :  'ND' ,
    'North Dakota'         :  'ND' ,
    'Nebraska'             :  'NE' ,
    'NewHampshire'         :  'NH' ,
    'New Hampshire'        :  'NH' ,
    'NewJersey'            :  'NJ' ,
    'New Jersey'           :  'NJ' ,
    'NewMexico'            :  'NM' ,
    'New Mexico'           :  'NM' ,
    'Nevada'               :  'NV' ,
    'NewYork'              :  'NY' ,
    'New York'             :  'NY' ,
    'Ohio'                 :  'OH' ,
    'Oklahoma'             :  'OK' ,
    'Oregon'               :  'OR' ,
    'Pennsylvania'         :  'PA' ,
    'RhodeIsland'          :  'RI' ,
    'Rhode Island'         :  'RI' ,
    'SouthCarolina'        :  'SC' ,
    'South Carolina'       :  'SC' ,
    'SouthDakota'          :  'SD' ,
    'South Dakota'         :  'SD' ,
    'Tennessee'            :  'TN' ,
    'Texas'                :  'TX' ,
    'Utah'                 :  'UT' ,
    'Virginia'             :  'VA' ,
    'Vermont'              :  'VT' ,
    'Washington'           :  'WA' ,
    'Wisconsin'            :  'WI' ,
    'WestVirginia'         :  'WV' ,
    'West Virginia'        :  'WV' ,
    'Wyoming'              :  'WY' ,
    'AK'                   :  'AK' ,
    'AL'                   :  'AL' ,
    'AR'                   :  'AR' ,
    'AZ'                   :  'AZ' ,
    'CA'                   :  'CA' ,
    'CO'                   :  'CO' ,
    'CT'                   :  'CT' ,
    'DC'                   :  'DC' ,
    'DE'                   :  'DE' ,
    'FL'                   :  'FL' ,
    'GA'                   :  'GA' ,
    'HI'                   :  'HI' ,
    'IA'                   :  'IA' ,
    'ID'                   :  'ID' ,
    'IL'                   :  'IL' ,
    'IN'                   :  'IN' ,
    'KS'                   :  'KS' ,
    'KY'                   :  'KY' ,
    'LA'                   :  'LA' ,
    'MA'                   :  'MA' ,
    'MD'                   :  'MD' ,
    'ME'                   :  'ME' ,
    'MI'                   :  'MI' ,
    'MN'                   :  'MN' ,
    'MO'                   :  'MO' ,
    'MS'                   :  'MS' ,
    'MT'                   :  'MT' ,
    'NA'                   :  'NA' ,
    'NC'                   :  'NC' ,
    'ND'                   :  'ND' ,
    'NE'                   :  'NE' ,
    'NH'                   :  'NH' ,
    'NJ'                   :  'NJ' ,
    'NM'                   :  'NM' ,
    'NV'                   :  'NV' ,
    'NY'                   :  'NY' ,
    'OH'                   :  'OH' ,
    'OK'                   :  'OK' ,
    'OR'                   :  'OR' ,
    'PA'                   :  'PA' ,
    'RI'                   :  'RI' ,
    'SC'                   :  'SC' ,
    'SD'                   :  'SD' ,
    'TN'                   :  'TN' ,
    'TX'                   :  'TX' ,
    'UT'                   :  'UT' ,
    'VA'                   :  'VA' ,
    'VT'                   :  'VT' ,
    'WA'                   :  'WA' ,
    'WI'                   :  'WI' ,
    'WV'                   :  'WV' ,
    'WY'                   :  'WY'
}


exceptions = set()
exceptions.add('IT')
exceptions.add('.NET')


def normalize_state(state):
    return states.get(state, 'Other')


def title_case(match):
  return match.group(0).replace(match.group(1), match.group(1).upper())


def make_exceptions(role):
    return " ".join([word if word in exceptions else word.lower() for word in role.split()])

to_title_case = re.compile('[^a-zA-Z]([a-z])')
def normalize_role(role):
    normalized = to_title_case.sub(title_case, make_exceptions(role))
    return normalized[0].upper() + normalized[1:]


@app.route('/<state>/jobs')
def jobs(state):
    # URI-encoded; e.g., /jobs?HTML,CSS,JavaScript=1&Python=1&R=1&SQL=1
    max_value        = 0
    search_terms = ""

    total = 0
    for arg in request.args:
        value = int(request.args[arg])
        total += value

        if value > max_value:
            max_value = value
            search_terms = arg
        elif value == max_value:
            search_terms += ("," + arg)

    # not currently used, would eliminate too many entries
    # role = 'Entry'
    # if   total >= 16: role = 'Senior'
    # elif total >= 10: role = 'Junior'

    # e.g., state = 'IL'; search_terms = 'HTML,CSS,Javascript'
    # print(search_terms)

    usa_jobs    = query('USAJobs',    state, search_terms)
    github_jobs = query('GitHubJobs', state, search_terms)

    jobs = []
    for source in [usa_jobs, github_jobs]:
        for job in source:
            state = normalize_state(job['State'])
            location = (job['City'] + ', ' + state) if state != 'Other' else state
            jobs.append([normalize_role(job['JobRole']), job['CompanyName'], location, job['URL']])

    """
    jobs = [
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
        ],
        [
            'Data Scientist',
            'Twitter',
            'Chicago, IL',
            'https://twitter.com/'
        ]
    ]
    random.shuffle(jobs)
    """
    return json.dumps(jobs)


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
    num_jobs = count()

    keywords_source  = get_json_by_source(data, "keywords", ["AWS", "C++", "CSS", "Excel", "Git", "HTML", "Java", "JavaScript", "NoSQL", "Python", "Scala", "SQL"])
    pays_source      = get_json_by_source(data, "pays", ["< $50,000", "$50,000 - $75,000", "$75,001 - $100,000", "> $100,000"])
    locations_source = get_json_by_source(data, "locations", ["Midwest", "Northeast", "South", "West"])

    keywords_skill  = get_json_by_skill(data, "keywords", ["AWS", "C++", "CSS", "Excel", "Git", "HTML", "Java", "JavaScript", "NoSQL", "Python", "Scala", "SQL"])
    pays_skill      = get_json_by_skill(data, "pays", ["< $50,000", "$50,000 - $75,000", "$75,001 - $100,000", "> $100,000"])
    locations_skill = get_json_by_skill(data, "locations", ["Midwest", "Northeast", "South", "West"])

    return render_template('index.html', num_jobs         = num_jobs,
                                         keywords_source  = keywords_source,
                                         pays_source      = pays_source,
                                         locations_source = locations_source,
                                         keywords_skill   = keywords_skill,
                                         pays_skill       = pays_skill,
                                         locations_skill  = locations_skill)
