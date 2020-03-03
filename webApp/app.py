from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    # skills    = calculate_skills()
    # pays      = calculate_pays()
    # locations = calculate_locations()

    # dummy objects, will need to be calculated above
    keywords = {
        'labels'  : ['HTML, CSS, & JavaScript', 'Python', 'R', 'SQL', 'C++'],
        'dataset' : [
            {'source': 'GitHub Jobs', 'data': [10, 20, 30, 40, 50] },
            {'source': 'USA Jobs',    'data': [10, 20, 30, 40, 50] }
        ]
    }

    pays = {
        'labels' : ['<50,000', '50,000-75,000', '75,001-100,000', '>100,000'],
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

    return render_template('index.html', keywords=keywords, pays=pays, locations=locations)
