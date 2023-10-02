import app
import flask
from flask import Flask, request, render_template
import time
from pymongo import MongoClient
import ssl
# Configuración de MongoDB
mongo_uri = "mongodb+srv://pagina:appuai@cluster0.sufar8c.mongodb.net/?retryWrites=true&w=majority"  # Reemplaza con tu URI de MongoDB
client = MongoClient(mongo_uri)#,ssl=True,
        #ssl_cert_reqs=ssl.CERT_REQUIRED,
        #ssl_ca_certs="/cacert.pem")
db = client['sensores']
collection = db['valores']

# Buscar un documento con el nombre "A001"
documento = collection.find_one({"nombre": "A001"})

# Verificar si se encontró un documento
if documento:
    # Obtener el valor del campo deseado, por ejemplo, 'valor'
    x= documento.get('valor')
print(x)



app = Flask(__name__)    
app.static_folder = 'static'

@app.route('/')
def inicio():
    while True:
        mongo_uri = "mongodb+srv://pagina:appuai@cluster0.sufar8c.mongodb.net/?retryWrites=true&w=majority"  # Reemplaza con tu URI de MongoDB
        client = MongoClient(mongo_uri,ssl=True,
                ssl_cert_reqs=ssl.CERT_REQUIRED,
                ssl_ca_certs="cacert.pem")
        db = client['sensores']
        collection = db['valores']

            # Buscar un documento con el nombre "A001"
        documento = collection.find_one({"nombre": "A001"})

            # Verificar si se encontró un documento
        if documento:
               # Obtener el valor del campo deseado, por ejemplo, 'valor'
            x= documento.get('valor')
            print(x)
            return render_template("/index.html", x=x)
        time.sleep(3)


if __name__ == '__main__':
    app.run(debug=True)