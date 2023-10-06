import flask
from flask import Flask, request, render_template
import time
from pymongo import MongoClient
import ssl

# Configuración de MongoDB
# Resto del código...


# Buscar un documento con el nombre "A001"
# Verificar si se encontró un documento

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def inicio():
    while True:
        mongo_uri = "mongodb+srv://pagina:appuai@cluster0.sufar8c.mongodb.net/?retryWrites=true&w=majority"  # Reemplaza con tu URI de MongoDB

        # Crear una conexión MongoDB con SSL
        client = MongoClient(mongo_uri)
        db = client['sensores']
        collection = db['valores']

        # Lista de nombres que quieres buscar
        nombres = ["A001", "A002"]

        valores = []  # Lista para almacenar los valores

        for nombre in nombres:
            # Buscar un documento con el nombre actual
            documento = collection.find_one({"nombre": nombre})

            # Verificar si se encontró un documento
            if documento:
                # Obtener el valor del campo deseado, por ejemplo, 'valor'
                x = documento.get('valor')
                valores.append(x)

        total = sum(valores)  # Calcular la suma de los valores

        print("Valores:", valores)
        print("Suma:", total)

        # Renderizar la plantilla con el valor total
        # Nota: Esto supone que estás utilizando Flask u otro framework web que admite renderizar plantillas
        return render_template("/index.html", x=total)





if __name__ == '__main__':
    app.run(debug=True) 