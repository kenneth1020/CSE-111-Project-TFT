#Library
from django.http import HttpResponse
from django.template import loader
from flask import Flask, request, url_for, render_template
from click import confirm
from statement import openConnection, closeConnection, championSearch, championData
import pandas as pd

app = Flask(__name__)

def testing(request):
    template = loader.get_template('navbar.html')
    return HttpResponse(template.render(request))

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


#Run the app
if __name__ == '__main__':
    app.run(debug=True)