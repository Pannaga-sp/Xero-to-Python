#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import re
import pandas as pd


# In[6]:


myjsonfile = open('E:/Traffic Radius - Blackcoffer/xero_output.json', 'r')
jsondata = myjsonfile.read()


# In[7]:


#Parse
obj = json.loads(jsondata)


# In[8]:


print(str(obj['Id']))
print(str(obj['Status']))
print(str(obj['Invoices']))


# In[9]:


list = obj['Invoices']
print(list)
print(len(list))

for i in range(len(list)):
    print("Invoices of  ", i, "is........")
    print("InvoiceID:",list[i].get("InvoiceID"))
    print("InvoiceNumber:",list[i].get("InvoiceNumber"))
    #print("Company:",list[i].get("Reference.split()"))
    print("Reference:",list[i].get("Reference"))
    print("AmountPaid:",list[i].get("AmountPaid"))
    print("DateString:",list[i].get("DateString"))
    print("Status:",list[i].get("Status"))
    print("Total:",list[i].get("Total"))


# In[10]:


df = pd.DataFrame(list, columns = ['InvoiceID', 'InvoiceNumber', 'Reference', 'AmountPaid', 'DateString', 'Status', 'Total'])


# In[11]:


df.head()


# In[12]:


df.to_excel("E:/Traffic Radius - Blackcoffer/xero_output.xlsx")


# In[13]:


# Define a list of field keys to extract from
field_key = 'Invoices'

# Define the target word
target_word = 'SEO'

# Load the DataFrame from a CSV file
df = pd.read_excel('E:/Traffic Radius - Blackcoffer/xero_output.xlsx')

# Create a new column 'reference_1' with empty values
df['reference_1'] = ''

# Iterate through each field key
for key in field_keys:
    # Access the nested field containing the sentence
    #print(obj['Invoices'][0]['Reference'])
    field = obj['Invoices'][0]['Reference']
    
    # Access the sentence within the field
    #sentence = field['sentence']

    # Apply regex pattern matching
    match = re.search(rf'\b({target_word})\b', field)

    # Extract the specific word using regex capturing groups
    if match:
        word = match.group(1)
        # Store the extracted word in the 'reference_1' column for the matching row
        df.loc[df['field_key'] == key, 'reference_1'] = word

# Save the updated DataFrame to a CSV file
df.to_excel('E:/Traffic Radius - Blackcoffer/xero_output.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




