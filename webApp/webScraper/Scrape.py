import requests
import json


def parse_usa_data(d):
    data = []
    id = d['MatchedObjectId']
    for i in range(len(d['MatchedObjectDescriptor']['PositionLocation'])):
        temp_dict = {}
        temp_dict['ID'] = id + str(i)
        temp_dict['JobRole'] = d['MatchedObjectDescriptor']['PositionTitle']
        temp_dict['CompanyName'] = d['MatchedObjectDescriptor']['OrganizationName']
        temp_dict['JobType'] = d['MatchedObjectDescriptor']['JobCategory'][0]['Name']
        temp_dict['Pay'] = str((float(d['MatchedObjectDescriptor']['PositionRemuneration'][0]['MinimumRange']) +
                                float(d['MatchedObjectDescriptor']['PositionRemuneration'][0]['MaximumRange'])) / 2)
        temp_dict['City'] = d['MatchedObjectDescriptor']['PositionLocation'][i]['LocationName'][0:d['MatchedObjectDescriptor']['PositionLocation'][i]['LocationName'].find(',')]
        temp_dict['State'] = d['MatchedObjectDescriptor']['PositionLocation'][i]['LocationName'][
                             d['MatchedObjectDescriptor']['PositionLocation'][i]['LocationName'].find(',') + 1:].replace(' ',
                                                                                              '')
        temp_dict['Skills'] = get_skills(
            (d['MatchedObjectDescriptor']['QualificationSummary'] + d['MatchedObjectDescriptor']['UserArea']['Details']['JobSummary']).lower())
        temp_dict['Technology'] = get_techs(
            (d['MatchedObjectDescriptor']['QualificationSummary'] + d['MatchedObjectDescriptor']['UserArea']['Details']['JobSummary']).lower())
        temp_dict['URL'] = d['MatchedObjectDescriptor']['ApplyURI'][0]
        data.append(temp_dict)
    return data


# This looks for keywords in the job posting summaries and returns a list of the ones it found
def get_skills(data):
    keywords = ['linux', 'mac', 'windows',
                'machine learning', 'artificial intelligence', 'algorithms',
                'analysis', 'statistic', 'computer science', 'math', 'deep learning',
                'software development', 'software engineering', 'data engineering',
                'neural networks', 'communications', 'creativity', 'resilience']
    found_keywords = []
    for word in keywords:
        if word in data:
            found_keywords.append(word)
    if len(found_keywords) == 0:
        found_keywords.append('')
    return found_keywords


# This looks for keywords in the job posting summaries and returns a list of the ones it found
def get_techs(data):
    keywords = ['python', 'sql', 'spark',
                'hadoop', 'aws', 'tensorflow',
                'scala', 'c++', 'css',
                'excel', 'azure', 'java',
                'pytorch', 'git', 'c#',
                'docker', 'nosql', 'javascript',
                'html', 'keras', 'mongodb']
    found_keywords = []
    for word in keywords:
        if word in data:
            found_keywords.append(word)
    if len(found_keywords) == 0:
        found_keywords.append('')
    return found_keywords


def usajob(token, email, parameter, search):
    '''
    For api reference: https://developer.usajobs.gov/API-Reference
    
    Url is the API endpoint that you will be using when making HTTP GET request
    /api/Search will be the most used endpoint for our purposes
    
    Visit https://developer.usajobs.gov/API-Reference/GET-api-Search for more information on search parameters
    
    Examples:
    To search for Software Engineer jobs use: 'https://data.usajobs.gov/api/Search?PositionTitle=Software%20Engineer'
    To search for all jobs with the keyword 'software' use: 'https://data.usajobs.gov/api/search?Keyword=Software'
    
    Headers is going to be the mandatory information that must be included with every API call
    
    Headers has three parameters: Host, User-Agent, and Authorization Key
    
    Host will always be 'data.usajobs.gov'
    User-Agent is your email address
    Authorization Key will be your API key
    For more information visit: https://developer.usajobs.gov/Guides/Authentication
    '''

    if usajob:
        url = 'https://data.usajobs.gov/api/Search?ResultsPerPage=500&' + parameter + '=' + search.replace(' ',
                                                                                                           '%20').lower()
        headers = {'Host': 'data.usajobs.gov', 'User-Agent': email, 'Authorization-Key': token}

        r = requests.get(url, headers=headers)

        data = r.json()
        data = data['SearchResult']['SearchResultItems']

        # Loads data.json with all the raw data collected
        outfile = open('usajob_raw.json', 'w')
        outfile.write(json.dumps(data, indent=2))
        outfile.close()

        cleaned_data = []
        dict = {}
        temp_dict = []
        for d in data:
            temp_dict.append(parse_usa_data(d))

        for i in range(len(temp_dict)):
            for j in range(len(temp_dict[i])):
                cleaned_data.append(temp_dict[i][j])

        outfile = open('usajob_data.json', "w")
        dict = cleaned_data
        json.dump(dict, outfile, indent=2)
        outfile.close()


def github(description):
    cleaned_data = []
    for i in range(9):
        url = 'https://jobs.github.com/positions.json?page=' + str(i) + '&description=' + description.replace(' ',
                                                                                                              '%20')
        r = requests.get(url)
        data = r.json()
        outfile = open("github_raw.json", "w")
        json.dump(data, outfile, indent=2)
        outfile.close()

        for d in data:
            temp_dict = {}
            temp_dict['ID'] = d['id']
            temp_dict['JobRole'] = d['title']
            temp_dict['CompanyName'] = d['company']
            temp_dict['JobType'] = description
            temp_dict['Pay'] = ''
            temp_dict['City'] = d['location'][0:d['location'].find(',')]
            temp_dict['State'] = d['location'][d['location'].find(',') + 1:].replace(' ', '')
            temp_dict['Skills'] = get_skills(d['description'].lower())
            temp_dict['Technology'] = get_techs(d['description'].lower())
            temp_dict['URL'] = d['url']
            cleaned_data.append(temp_dict)
    dict = {}
    outfile = open("github_data.json", "w")
    dict = cleaned_data
    json.dump(dict, outfile, indent=2)
    outfile.close()
