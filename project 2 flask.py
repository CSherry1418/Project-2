#!/usr/bin/env python
# coding: utf-8

# In[31]:


from flask import Flask, jsonify, render_template
import json
import os
import pandas as pd
from flask_cors import CORS
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from sql_setup import setup_dependencies
engine, session, , Rushing = setup_dependencies(app)


# In[38]:


app = Flask(__name__)
CORS(app)


# In[39]:


@app.route('/')
def welcome():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Baseball API!<br/>"
        f"Available Routes:<br/>"
    )


# In[40]:


@app.route("/<table>/<x>/<y>")
def get_data(table, x, y):

    if(x == y):
        return jsonify([])
    
    data = pd.read_sql_table(table, engine)[['name', x, y]]

    return data.to_json()


# In[41]:


@app.route('/<table>')
def populate_dropdown(table):

    options = [x for x in pd.read_sql_table(table, engine).columns if x not in exclusions]

    return jsonify(options)


# In[42]:


@app.route('/table/<table>/<x>/<y>')
def get_table_data(table, x, y):
    data = pd.read_sql_table(table, engine)[['name', x, y]]
    table_data = []
    for ind, row in data.iterrows():
        d = {
            'name': row['name'],
            'x': row[x],
            'y': row[y]
        }
        table_data.append(d)
    return jsonify(table_data)
def insert_data():
    import sys
    sys.path.append("..")
    import data_insert
    data_insert.insert_all()


# In[43]:


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000)) # this sets the port to 8000 locally, and ${PORT} environment variable on Heroku
    app.run(host='0.0.0.0', port=port, debug=True)

