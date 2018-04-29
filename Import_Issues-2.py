
# coding: utf-8

# In[8]:


# pip install github3.py command for install github3
# execute pip install github3.py command from the the command window/terminal

import github3
import json


# In[9]:


# Get an API key for GitHub and set it as GITHUB_TOKEN
# Here is the URL to generate your GITHUB_TOKEN
# https://help.github.com/articles/creating-an-access-token-for-command-line-use/

GITHUB_TOKEN = '550859d1782ee70a21aa5f9a8e8065bf2e2ef2dd'
ORG = 'SPM587SP18'                     
REPO = 'SCM587SP18'
FILENAME_ISSUES = ORG + 'issues.json'


# In[10]:


gh = github3.login(token=GITHUB_TOKEN)

f = open(FILENAME_ISSUES, 'w')
for issue in gh.search_issues('type:issue repo:SPM587SP18/SCM587SP18'):          # Find issues from given Repo
            label_name=[]
            data={}
            
            current = issue.as_json()
            current_issue =json.loads(current)
           
            data['issue_number']=current_issue["number"]                          # Get issue number              
            data['created_at']= current_issue["created_at"][0:10]                 # Get created date of issue
            if current_issue["closed_at"] == None:
                data['closed_at']= current_issue["closed_at"]
            else:
                data['closed_at']= current_issue["closed_at"][0:10]               # Get closed date of issue
            for label in current_issue["labels"]:
                label_name.append(label["name"])                                  # Get label name of issue
            data['labels']= label_name
            data['State'] = current_issue["state"]                                # It gives state of issue like closed or open
            data['Author'] = current_issue["user"]["login"]                       # Get Author of issue
            out=json.dumps(data)                                                  # save this all information to a JSON file
            f.write(out+ '\n')
f.close()

