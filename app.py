#Library
from flask import Flask, request, url_for, render_template
from click import confirm
from statement import *
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/CISearch',methods =['GET','POST'])
def CISearch():
    if request.method == "POST":
        search1 = request.form['cn']

        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = championSearch(conn, search1)
            print(rows)

            # creating dataframe
            df = pd.DataFrame()
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
    
            df.to_html('templates/ChampionItems.html')
        
        
        return render_template('ChampionItems.html')

    return render_template('CISearch.html')
    


@app.route('/champion')
def champion():     
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        rows = championData(conn)
        print(rows)
    
    # creating dataframe
        df = pd.DataFrame()
        for row in rows:
            df2 = pd.DataFrame(list(row)).T
            df = pd.concat([df,df2])
    
        df.to_html('templates/ChampionData.html')
   
    return render_template('ChampionData.html')

@app.route('/CPSearch',methods =['GET','POST'])
def CPSearch():
    if request.method == "POST":
        search1 = request.form['cp']

        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = championPlacement(conn, search1)
            print(rows)

            # creating dataframe
            df = pd.DataFrame()
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
    
            df.to_html('templates/CP.html')
        
        
        return render_template('CP.html')

    return render_template('CPSearch.html')



@app.route('/Comptop',methods =['GET','POST'])
def Comptop():
    if request.method == "POST":
        search1 = request.form['ori']
        search2 = request.form['cl']
        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = compTopChampions(conn, search1, search2)
            print(rows)

            # creating dataframe
            df = pd.DataFrame()
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
    
            df.to_html('templates/TopChampion.html')
        
        
        return render_template('TopChampion.html')

    return render_template('Comptop.html')

#Run the app
if __name__ == '__main__':
    app.run(debug=True)