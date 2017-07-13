#import packages needed to run function
import json
import pandas as pd
import numpy as np
from operator import itemgetter

#import business data
rest = pd.read_excel('restaurant_all_data.xlsx')

#import ratings data
bu = pd.read_excel('business_user_rating.xlsx')

#select the columns from the business data
nbiz = rest[['business_id','state']]

#merget the business names and state with ratings in order to reduce data based on state
new = nbiz.merge(bu, on=('business_id'), how='right')

#reduce data to only include restaurants in state of Nevada
newnew = new[new.state == 'NV']

#drop state column since no longer necessary
newnew = newnew.drop('state', 1)

#create data frame with users as rows and busienss as columns and ratings as values
nevada= pd.pivot_table(newnew, index='user_id', columns='business_id', values='stars', fill_value = None)

#transpose data frame in order to have business as rows and users as columns
nev_t = nevada.T

#make business_id the row names
nev_t['business_id'] = nev_t.index

#merge resturant data with ratings data to get correct index placement of restaurant names
nev = nev_t.merge(rest, on=('business_id'), how='left')

#reset row names to business_id
nev.set_index('business_id', inplace = True)

#drop the unnecessary columns brought in with restaurant data
nev = nev.drop('state', 1)
nev = nev.drop('review_count', 1)
nev = nev.drop('categories', 1)

#grab a list of the restaurant names with the correct indexes
names = list(nev.name)

#drop the name column
ratings = nev.drop('name', 1)

#convert data frame to array and replace NaNs with 0 (needed to run function)
x = np.array(ratings)
rating = np.where(np.isnan(x), 0, x)

#Pearson Similarity gotten from Homework 4
def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar = 0)[0][1]

#function that returns the most similar to the selected restaurant
def print_most_similar(data, businesses, restindex, k, metric=pearsSim):
    lst = []
    if restindex == 123456789:
        return "We're sorry, that restaurant is not in our database. Please try again."
    else:
        for i in range(len(data)):
            if i == restindex:
                pass
            else:
                try:
                    x = metric(data[restindex], data[i])
                    lst.append([i,x])
                except:
                    pass
        s = sorted(lst, key=itemgetter(1),reverse=True)
        neighbors = s[:k]
        sugg = []
        for j in neighbors:
            add = businesses[j[0]]
            sugg.append(add)
        y = str()
        for k in range(len(sugg)):
            x = str("Recommendation {}: {}; ".format(k+1, sugg[k]))
            y += x
        return y

       
#get index of the restaurant written in text box  
def getBusIndex( rest_name, rest_list):
   if rest_name in rest_list:
       for i in range(len(rest_list)):
           if rest_list[i] == rest_name:
               return i
   else:
       i = 123456789
       return i

#import necessary flask packages
from flask import Flask, render_template, make_response, request, redirect, url_for, abort, session
from flask.json import jsonify

#define app
app = Flask(__name__)

#creates landing page
@app.route('/')
def index():
    return render_template('NevadaRecSystem.html')

#connects function with route to html function
@app.route("/getrecomm",methods=['GET','POST'])
def getrecomm():
    restname = request.args.get('restname', type=str)
    number = request.args.get('number', type=int)
    i = getBusIndex(restname, names)
    return make_response(jsonify(result=(print_most_similar(rating, names, i, number))),200)

#runs app      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


