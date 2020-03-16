from . import dynamo_db
from boto3.dynamodb.conditions import Attr

# query with param state, role ie. entry level or junior, top 2 tech

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'DistrictofColumbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'NorthCarolina',
        'ND': 'NorthDakota',
        'NE': 'Nebraska',
        'NH': 'NewHampshire',
        'NJ': 'NewJersey',
        'NM': 'NewMexico',
        'NV': 'Nevada',
        'NY': 'NewYork',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'RhodeIsland',
        'SC': 'SouthCarolina',
        'SD': 'SouthDakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'WestVirginia',
        'WY': 'Wyoming'
}

def query(table_name, state, technologies):
    table = dynamo_db.Table(table_name)

    technologies = technologies.lower().split(',')
    attributes = Attr('Technology').contains(technologies[0])
    for i in range(1, len(technologies)):
        attributes = (attributes | Attr('Technology').contains(technologies[i]))

    if state != "ANY":
        attributes = (Attr('State').eq(state) | Attr('State').eq(states[state])) & attributes

    data = table.scan(
        TableName=table_name,
        FilterExpression=attributes
    )
    return data['Items']


# function to give count of items in database

def count():
    cnt = 0
    git_table = dynamo_db.Table('GitHubJobs')
    usa_table = dynamo_db.Table('USAJobs')
    table1 = git_table.scan()
    table2 = usa_table.scan()
    data1 = table1['Items']
    data2 = table2['Items']
    while 'LastEvaluatedKey' in table1:
        table1 = git_table.scan(ExclusiveStartKey=table1['LastEvaluatedKey'])
        data1.extend(table1['Items'])

    while 'LastEvaluatedKey' in table2:
        table2 = usa_table.scan(ExclusiveStartKey=table2['LastEvaluatedKey'])
        data2.extend(table2['Items'])
    cnt = len(data1) + len(data2)

    return cnt
