import requests
import json



def usajob(token, email, parameter, search, argv):
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
        url = 'https://data.usajobs.gov/api/Search?' + parameter + '=' + search.replace(' ', '%20')
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
        for d in data:
            d = d['MatchedObjectDescriptor']
            temp_dict = {}
            temp_dict['JobRole'] = d['PositionTitle']
            temp_dict['CompanyName'] = d['OrganizationName']
            temp_dict['JobType'] = d['JobCategory'][0]['Name']
            temp_dict['Pay'] = d['PositionRemuneration'][0]['MinimumRange']
            temp_dict['City'] = d['PositionLocationDisplay'][0:d['PositionLocationDisplay'].find(',')]
            temp_dict['State'] = d['PositionLocationDisplay'][d['PositionLocationDisplay'].find(',') + 1:].replace(' ', '')
            temp_dict['Experience'] = ''
            temp_dict['Skills'] = ''
            # tempDict['Qualifications'] = d['QualificationSummary']
            cleaned_data.append(temp_dict)

        outfile = open('usajob_data.json', "w")
        dict = cleaned_data
        json.dump(dict, outfile, indent=2)
        outfile.close()


def github(description):
    url = 'https://jobs.github.com/positions.json?description=' + description.replace(' ', '%20')
    r = requests.get(url)
    data = r.json()
    outfile = open("github_raw.json", "w")
    json.dump(data, outfile, indent=2)
    outfile.close()

    cleaned_data = []
    dict = {}
    for d in data:
        temp_dict = {}
        temp_dict['JobRole'] = d['title']
        temp_dict['CompanyName'] = d['company']
        temp_dict['JobType'] = description
        temp_dict['Pay'] = ''
        temp_dict['City'] = d['location'][0:d['location'].find(',')]
        temp_dict['State'] = d['location'][d['location'].find(',')+1:].replace(' ', '')
        temp_dict['Experience'] = ''
        temp_dict['Skills'] = ''
        cleaned_data.append(temp_dict)

    outfile = open("github_data.json", "w")
    dict = cleaned_data
    json.dump(dict, outfile, indent=2)
    outfile.close()

