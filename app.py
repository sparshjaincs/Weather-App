from flask import Flask,render_template,url_for,request
import sqlite3 as sql
import requests
app =Flask(__name__)

weather_data=[]
@app.route("/" , methods=['POST','GET'])

def index():
    db = sql.connect("cities.db")
    cursor=db.cursor()	
    if request.method == 'POST':
        new_city = request.form.get('city')
        cursor.execute("select * from city") 
        cities = [ city[0] for city in cursor.fetchall() ]
        if new_city and new_city not in cities :
            cursor.execute(f"insert into city values('{new_city}')")
            db.commit()
    cursor.execute("select * from city")
    cities = [ city[0] for city in cursor.fetchall() ]
    cursor.close()
    db.close()

    
    weather_data =[]
    
    
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=63823cbc5100cc9809fb0e1d14ebf946"
        data=requests.get(url).text
        weather={
                'city':city,
                'temperature':data['main']['temp']
                }
        weather_data.append(weather)

        
    return render_template("index.html",weather_data=weather_data)


if __name__=='__main__':
    app.run(debug=True)
