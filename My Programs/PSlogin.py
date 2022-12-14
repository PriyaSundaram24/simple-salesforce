import pandas as pd
from pprint import pprint
from simple_salesforce import Salesforce
sf = Salesforce(password='Trailhead@123', username='priyasundaram@industries.com', security_token='RYEOwQJ8jq9wQJU9ly7lV76S',organizationId='00D5g00000JRSGo')
data = sf.query("SELECT Id, Name FROM Contact")
sf_df = pd.DataFrame(data['records']).drop(columns='attributes')
print(sf_df)

SOQL = "SELECT Id, Email FROM Contact"
data = sf.query(SOQL)
print(data)
for d in data['records']:
    pprint(f"{d['Id']} -- {d['Email']}")
