'''
Visuals Generator

Pulls/queries data using the boto3 module to generates graphs

The graphs generated are referenced as Flask routes in app.py

ie datascienceskills.herokuapp.com/dynamicGph can call a method
dynamicGraph in genGraphs.py. This allows the graph to be used in
an img tag in HTML by the link above
'''