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
            df = pd.DataFrame(pd.np.empty((0, 3)))    

            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Name', 'Components', 'Count']
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
        df.columns = ['Name', 'Origin 1', 'Origin 2', 'Class 1', 'Class 2', 'Cost']

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
            df = pd.DataFrame(pd.np.empty((0, 3)))    
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Name', 'Class 1', 'Class']
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
            df = pd.DataFrame(pd.np.empty((0, 4)))
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Name', 'Item 1', 'Item 2', 'Item 3']
            df.to_html('templates/TopChampion.html')
        
        
        return render_template('TopChampion.html')

    return render_template('Comptop.html')

@app.route('/origin')
def origin():     
    database = r"tft_data.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        rows = originData(conn)
        print(rows)
    
    # creating dataframe
        df = pd.DataFrame()
        for row in rows:
            df2 = pd.DataFrame(list(row)).T
            df = pd.concat([df,df2])
        df.columns = ['Index','Origin',
        'Tier',
        'Description',
        'Required 1',
        'Bonus  1', 
        'Required 2',
        'Bonus 2', 
        'Required 3',
        'Bonus 3', 
        'Required 4',
        'Bonus 4', 
        'Required 5',
        'Bonus 5', 
        'Required 6',
        'Bonus 6', 
        'Required 7',
        'Bonus 7', 
        'Required 8',
        'Bonus 8']
        df.to_html('templates/originData.html')
   
    return render_template('originData.html')

@app.route('/OSearch',methods =['GET','POST'])
def OSearch(): 
    if request.method == "POST":
        search1 = request.form['ori']    
        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = originSearch(conn, search1)
            print(rows)
    
            # creating dataframe
            df = pd.DataFrame(pd.np.empty((0, 20)))    
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Index','Origin',
            'Tier',
            'Description',
            'Required 1',
            'Bonus  1', 
            'Required 2',
            'Bonus 2', 
            'Required 3',
            'Bonus 3', 
            'Required 4',
            'Bonus 4', 
            'Required 5',
            'Bonus 5', 
            'Required 6',
            'Bonus 6', 
            'Required 7',
            'Bonus 7', 
            'Required 8',
            'Bonus 8']
            df.to_html('templates/OResults.html')
        
        return render_template('OResults.html')
   
    return render_template('OSearch.html')

@app.route('/CSearch',methods =['GET','POST'])
def CSearch(): 
    if request.method == "POST":
        search1 = request.form['cn']    
        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = championInfo(conn, search1)
            print(rows)
    
            # creating dataframe
            df = pd.DataFrame(pd.np.empty((0, 15)))   
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Champion',
            'Origin1',
            'Origin2',
            'Class1',
            'Class2',
            'Cost', 
            'Mana',
            'Starting Manga', 
            'Armor',
            'Magic Resistance', 
            'Attack Speed',
            'Critical Rate', 
            'Range',
            'Ability', 
            'Ability Description']
            df.to_html('templates/CResults.html')
        
        return render_template('CResults.html')
   
    return render_template('CSearch.html')

@app.route('/ISearch',methods =['GET','POST'])
def ISearch(): 
    if request.method == "POST":
        search1 = request.form['component']    
        database = r"tft_data.sqlite"
        # create a database connection
        conn = openConnection(database)
        with conn:
            rows = items(conn, search1)
            print(rows)
    
            # creating dataframe
            df = pd.DataFrame(pd.np.empty((0, 5)))
            for row in rows:
                df2 = pd.DataFrame(list(row)).T
                df = pd.concat([df,df2])
            df.columns = ['Item',
            'Component 1',
            'Component 2',
            'Description',
            'Tier']
            df.to_html('templates/IResults.html')
        
        return render_template('IResults.html')
   
    return render_template('ISearch.html')

#Run the app
if __name__ == '__main__':
    app.run(debug=True)