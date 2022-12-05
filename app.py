#Library
from flask import Flask, request, url_for, render_template
from flask_navigation import Navigation
from click import confirm
from statement import openConnection, closeConnection, championSearch, championData
import pandas as pd

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Champion Items', 'championItems'),
    nav.Item('Champion', 'champion'),
])

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/championItems',methods =['GET','POST'])
def championItems():
    if request.method =='GET':
            #this only takes in one input 'PrimaryEmail'
            return '<form action="/" method="POST"><input name="Champion"><input type ="submit"></form>'  
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        search1 = request.form['Champion']
        rows = championSearch(conn, search1)
        print(rows)

    
    # creating dataframe
        df = pd.DataFrame()
        for row in rows:
            df2 = pd.DataFrame(list(row)).T
            df = pd.concat([df,df2])
    
        df.to_html('templates/ChampionItems.html')
   
    return render_template('ChampionItems.html')


@app.route('/champion')
def champion():
    if request.method =='GET':
            #this only takes in one input 'PrimaryEmail'
            return '<form action="/" method="POST"><input name="Champion"><input type ="submit"></form>'  
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        search1 = request.form['Champion']
        rows = championData(conn)
        print(rows)
    
     # creating dataframe
        df = pd.DataFrame()
        for row in rows:
            df2 = pd.DataFrame(list(row)).T
            df = pd.concat([df,df2])
    
        df.to_html('templates/ChampionData.html')
   
    return render_template('ChampionData.html')

#Run the app
if __name__ == '__main__':
    app.run(debug=True)