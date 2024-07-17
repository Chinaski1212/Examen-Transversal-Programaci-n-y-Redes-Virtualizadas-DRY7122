from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>Nombres de los integrantes:</h1>
        <ul>
            <li>Rodrigo Sanhueza</li>
            <li>Abraham Gallardo</li>
            <li>Cristobal Escala</li>
        </ul>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)
