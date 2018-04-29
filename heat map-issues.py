
# coding: utf-8

# In[7]:


import pandas as pd
import json


# In[8]:


list_of_issues_dict_data = [json.loads(line) for line in open('SPM587SP18issues.json')]


# In[9]:


from elasticsearch import Elasticsearch,helpers
es=Elasticsearch()


# In[10]:


actions = []
for data in list_of_issues_dict_data:
    action = {
        "_index":"issues",
        "_type": "issue",
        "_id": data['issue_number'],
        "_source": data
    }
    actions.append(action)


# In[11]:


doc= {
    'size': 10000,
    'query': { 
        'match_all': {} 
    }
}
result_without_condition = es.search(index='issues', body=doc,scroll='1h')
result_without_condition



# In[12]:


sid=result_without_condition['_scroll_id']
scroll_size=result_without_condition['hits']['total']


# In[13]:


count=0
final1= []
while(scroll_size>0):
    for doc in result_without_condition['hits']['hits']:
        location_l1=[]
        results=doc['_source']
        count=count+1
        results_labels = dict(s.split(':') for s in results['labels'])
        if 'Latitude' in results_labels.keys():
            if 'Longitude' in results_labels.keys():
                if 'Address' in results_labels.keys():
                    if(results_labels['Latitude']!=None and results_labels['Longitude']!=None and results_labels['Address']!=None):
                        location_l1.append(float(results_labels['Latitude']))
                        location_l1.append(float(results_labels['Longitude']))
                        final1.append(location_l1)
    result_without_condition = es.scroll(scroll_id =sid,scroll= '2m')
    sid=result_without_condition['_scroll_id']
    scroll_size=len(result_without_condition['hits']['hits'])
print("the total records",count)
final1


# In[14]:


import folium
from folium import plugins
print(folium.__version__)


# In[15]:


m= folium.Map(location = [41.852623,-87.611958],zoom_start=10)
m


# In[16]:


m.add_child(plugins.HeatMap(final1,radius=25))
m


# In[17]:


doc1 = {
       'size': 100,
       'query':{
           'bool':{
               'must': [{'match':{'labels':'DetectionPhase:Field'}},{'match':{'labels':'Priority:Critical'}}]
           }
       }
}
result_with_condition = es.search(index='issues',body=doc1,scroll='1h')
result_with_condition



# In[18]:


sid=result_with_condition['_scroll_id']
scroll_size=result_with_condition['hits']['total']


# In[19]:


count=0
finalcond1= []
while(scroll_size>0):
   for doc in result_with_condition['hits']['hits']:
       loc1cond=[]
       results=doc['_source']
       count=count+1
       results_labels = dict(s.split(':') for s in results['labels'])
       if 'Latitude' in results_labels.keys():
           if 'Longitude' in results_labels.keys():
               if 'Address' in results_labels.keys():
                   if(results_labels['Latitude']!=None and results_labels['Longitude']!=None and results_labels['Address']!=None):
                       loc1cond.append(float(results_labels['Latitude']))
                       loc1cond.append(float(results_labels['Longitude']))
                       finalcond1.append(loc1cond)
   result_with_condition = es.scroll(scroll_id =sid,scroll= '2m')
   sid=result_with_condition['_scroll_id']
   scroll_size=len(result_with_condition['hits']['hits'])
print("the total records with condition",count)
finalcond1


# In[20]:


condition_heatmap= folium.Map(location = [41.89323,-87.617419],zoom_start=11)
condition_heatmap


# In[21]:


condition_heatmap.add_child(plugins.HeatMap(finalcond1,radius=15))
condition_heatmap


# In[22]:


doc2 = {
       'size': 100,
       'query':{
           'bool':{
               'must': [{'match':{'labels':'DetectionPhase:Field'}},{'match':{'labels':'Status:Completed'}}]
           }
       }
}
result_with_condition2 = es.search(index='issues',body=doc2,scroll='1h')
result_with_condition2


# In[54]:


sid=result_with_condition2['_scroll_id']
scroll_size=result_with_condition2['hits']['total']


# In[23]:


count=0
finalcond2= []
while(scroll_size>0):
   for doc in result_with_condition2['hits']['hits']:
       loc1cond=[]
       results=doc['_source']
       count=count+1
       results_labels = dict(s.split(':') for s in results['labels'])
       if 'Latitude' in results_labels.keys():
           if 'Longitude' in results_labels.keys():
               if 'Address' in results_labels.keys():
                   if(results_labels['Latitude']!=None and results_labels['Longitude']!=None and results_labels['Address']!=None):
                       loc1cond.append(float(results_labels['Latitude']))
                       loc1cond.append(float(results_labels['Longitude']))
                       finalcond2.append(loc1cond)
   result_with_condition2 = es.scroll(scroll_id =sid,scroll= '2m')
   sid=result_with_condition2['_scroll_id']
   scroll_size=len(result_with_condition2['hits']['hits'])
print("the total records with condition",count)
finalcond2



# In[24]:


condition_heatmap2= folium.Map(location = [41.89323,-87.617419],zoom_start=11)
condition_heatmap2


# In[25]:


condition_heatmap2.add_child(plugins.HeatMap(finalcond2,radius=15))
condition_heatmap2


# In[27]:


doc3 = {
       'size': 100,
       'query':{
           'bool':{
               'must': [{'match':{'labels':'DetectionPhase:Field'}},{'match':{'labels':'Priority:Critical'}},{'match':{'labels':'Status:Approved'}}]
           }
       }
}
result_with_condition3 = es.search(index='issues',body=doc3,scroll='1h')
result_with_condition3


# In[28]:


sid=result_with_condition3['_scroll_id']
scroll_size=result_with_condition3['hits']['total']


# In[29]:


count=0
finalcond3= []
while(scroll_size>0):
   for doc in result_with_condition3['hits']['hits']:
       loc1cond=[]
       results=doc['_source']
       count=count+1
       results_labels = dict(s.split(':') for s in results['labels'])
       if 'Latitude' in results_labels.keys():
           if 'Longitude' in results_labels.keys():
               if 'Address' in results_labels.keys():
                   if(results_labels['Latitude']!=None and results_labels['Longitude']!=None and results_labels['Address']!=None):
                       loc1cond.append(float(results_labels['Latitude']))
                       loc1cond.append(float(results_labels['Longitude']))
                       finalcond3.append(loc1cond)
   result_with_condition3 = es.scroll(scroll_id =sid,scroll= '2m')
   sid=result_with_condition3['_scroll_id']
   scroll_size=len(result_with_condition3['hits']['hits'])
print("the total records with condition",count)
finalcond3


# In[30]:


condition_heatmap3= folium.Map(location = [41.89323,-87.617419],zoom_start=11)
condition_heatmap3


# In[31]:


condition_heatmap3.add_child(plugins.HeatMap(finalcond3,radius=15))
condition_heatmap3


# In[32]:


doc4 = {
       'size': 100,
       'query':{
           'bool':{
               'must': [
                   {
                       'match':{'labels':'DetectionPhase:Field'}
                   },
                   {  'bool':{
                            'should':[
                                {'match':{'labels':'Priority:Critical'}},
                                {'match':{'labels':'Priority:High'}}
                            ]
                        }
                   },
                   { 'bool':{
                            'should':[
                                {'match':{'labels':'Status:Approved'}},
                                {'match':{'labels':'Status:inProgress'}}
                            ]
                       }
                   }
                   
               ]
          }
   }
}
result_with_condition4 = es.search(index='issues',body=doc4,scroll='1h')
result_with_condition4


# In[33]:


sid=result_with_condition4['_scroll_id']
scroll_size=result_with_condition4['hits']['total']


# In[34]:


count=0
finalcond4= []
while(scroll_size>0):
   for doc in result_with_condition4['hits']['hits']:
       loc1cond=[]
       results=doc['_source']
       count=count+1
       results_labels = dict(s.split(':') for s in results['labels'])
       if 'Latitude' in results_labels.keys():
           if 'Longitude' in results_labels.keys():
               if 'Address' in results_labels.keys():
                   if(results_labels['Latitude']!=None and results_labels['Longitude']!=None and results_labels['Address']!=None):
                       loc1cond.append(float(results_labels['Latitude']))
                       loc1cond.append(float(results_labels['Longitude']))
                       finalcond4.append(loc1cond)
   result_with_condition4 = es.scroll(scroll_id =sid,scroll= '2m')
   sid=result_with_condition4['_scroll_id']
   scroll_size=len(result_with_condition4['hits']['hits'])
print("the total records with condition",count)
finalcond4


# In[35]:


condition_heatmap4= folium.Map(location = [41.89323,-87.617419],zoom_start=11)
condition_heatmap4


# In[36]:


condition_heatmap4.add_child(plugins.HeatMap(finalcond4,radius=15))
condition_heatmap4

