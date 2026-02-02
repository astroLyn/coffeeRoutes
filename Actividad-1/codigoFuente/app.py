from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    # En la fase 2 pondremos el mapa aquí
    return "<h1>Aquí irá el mapa de cafeterías en la Fase 2</h1>"

if __name__ == '__main__':
    app.run(debug=True)