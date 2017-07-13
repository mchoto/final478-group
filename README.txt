READ ME
 
--Introduction--
The introduction (required) shall consist of a brief paragraph or two that summarizes the purpose and function of this project. This introduction may be the same as the first paragraph on the project page.
The following README file outlines how to install, configure and use the Nevada Restaurant Recommender System. The system provides restaurant suggestions based on Yelp user ratings data for the state of Nevada. It built in Python with the use of Flask, and is only intended to be run locally at this point. 
 When interacting with the application in a browser, the user inputs a restaurant of their choosing and specifies the number of recommendations they would like returned. The top results are returned to them in a list. 
This application could be expanded greatly in scope. Currently, this application is only intended for users in Nevada, but additional states could be easily added. Also, functionality could be introduced to add a third variable of user input to specify type of restaurant (e.g. Chinese, Pizza, etc.). Furthermore, the capability to add a restaurant and/or rating to the database could be added.
 
--File Manifest--
NevadaRecSystem.py
NevadaRecSystem.html
Business_data_set.csv
User_data_set.csv
 
--Installation Instructions--
After downloading and unzipping the Nevada Rec System file:
 - Open the command line
 - change your directory to the location of the unzipped Nevada Rec System
 - run 'pip install flask'
 - run 'set FLASK_APP=NevadaRecSystem.py'
 - run 'flask run'
 - the app takes a few minutes to load, thank you for your patience
 - Navigate to the url listed in your command line (likely: 127.0.0.1:5000)

--Requirements/Configuration instructions--
-Python 3.0 or higher:
--Json
--Pandas as pd
--Numpy as np
--Itemgetter from operator
-Flask
--Flask
--Render_template
--Make_response
--Request
--Redirect
--Url_
--Jsonify from flask.json
 
--Troubleshooting/Known Bugs/FAQ--
If files are moved from their original folders, try redownloading the zip. The .html file should be located in a subfolder named Templates. 
If any changes are made to the .html or .py files, the current python session must be closed and reopened before these changes will be visible on the site. 
 
--Maintainers/Contact info for distributer/Credits--
Monica Choto
Becky Jacob
Norie Kaufmann
 
With special thanks to Aleksander Velkoski, Gatorade, and Cliff Bars.
