from flask import Flask, render_template, request, jsonify
import time # Importamos time para simular latencia

app = Flask(__name__)

# Base de datos simulada en memoria (se borra al reiniciar)
puntos_cafe = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mapa')
def mapa():
    return render_template('map.html')

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.get_json()
    
    # 1. Simulación de Latencia (1.5 segundos)
    # Esto es CRUCIAL para ver tu spinner de carga en el frontend
    time.sleep(1.5)
    
    # 2. Guardar datos (simulado)
    nuevo_punto = {
        'lat': data['lat'],
        'lng': data['lng'],
        'nombre': "Nuevo Café Detectado"
    }
    puntos_cafe.append(nuevo_punto)
    
    # 3. Retornar éxito
    return jsonify({'status': 'success', 'message': 'Punto guardado correctamente', 'data': nuevo_punto})

if __name__ == '__main__':
    app.run(debug=True)