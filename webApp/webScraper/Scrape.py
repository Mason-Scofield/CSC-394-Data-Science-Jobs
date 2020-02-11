import requests
import json


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
        url = 'https://data.usajobs.gov/api/Search?' + parameter + '=' + search
        headers = {'Host': 'data.usajobs.gov', 'User-Agent': email, 'Authorization-Key': token}

        r = requests.get(url, headers=headers)

        data = r.json()
        data = data['SearchResult']['SearchResultItems']

        # Loads data.json with all the raw data collected
        outfile = open('raw-data.json', 'w')
        json.dump(data, outfile)
        outfile.close()

        # An example of how to parse the data.
        # Eventually we want to get to the point where we can send data to populateDB.py
        outfile = open('CleanedData.txt', "w")

        # Convert CleanedData.txt to data.json
        # This means building a JSON object so that we write proper JSON
        for d in data:
            # print(d['MatchedObjectDescriptor'])
            d = d['MatchedObjectDescriptor']
            outfile.write('JobRole: ' + d['PositionTitle'])
            outfile.write('\nCompany: ' + d['OrganizationName'])
            outfile.write('\nJobType: ' + d['JobCategory'][0]['Name'])
            outfile.write('\nPay: ' + d['PositionRemuneration'][0]['MinimumRange'])
            # Qualifications will have to be looked at to see if we can further improve its parsing
            # outfile.write('\nQualifications: ' + d['QualificationSummary'])
            outfile.write('\nLocation: ' + d['PositionLocationDisplay'])
            outfile.write('\n-----------------------\n')
        outfile.close()


def github():
    print("Github api not yet implemented")
