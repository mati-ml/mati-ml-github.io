import pandas as pd
import flask
from flask import Flask, request, render_template
import time


df = pd.read_json('valores.json')



app = Flask(__name__)    
app.static_folder = 'static'

@app.route('/')
def inicio():
    while True:
        df = pd.read_json('valores.json')
        fila = df[df['nombre'] == 'A001']
        x = fila['valor'].values[0]
        x = int(x)
        print(x)
        
        if x==1:
            print(0)
        else:
            print(1)    

        return render_template("/index.html", x=x)
        time.sleep(3)


if __name__ == '__main__':
    app.run(debug=True)




   
