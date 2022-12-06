from __future__ import print_function

import requests
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
data={
    'name':'abc'
}
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
header={
'Authorization': creds,
'Accept': 'application/json',
'Content-Type': 'application/json',
}
api='AIzaSyBzoJFtT2qG5jaLhLDIFyzCxpY7d0er64k'

url=f'https://www.googleapis.com/drive/v3/drives?requestId=kauiehiueh&key={api},'

a=requests.post(url,headers=header,data=data)
print(a.content)