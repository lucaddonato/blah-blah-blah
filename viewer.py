from flask import Flask, request, send_from_directory, render_template_string
import os
from datetime import datetime

app = Flask(__name__)
SCREENSHOT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screenshots')
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'screenshot' not in request.files:
        return {"error": "Arquivo 'screenshot' não enviado"}, 400

    file = request.files['screenshot']
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(SCREENSHOT_FOLDER, filename)
    file.save(filepath)

    return {"status": "ok", "filename": filename}, 200

@app.route('/')
def index():
    if not os.path.exists(SCREENSHOT_FOLDER) or not os.listdir(SCREENSHOT_FOLDER):
        return "<h1>Nenhuma imagem encontrada na pasta 'screenshots'.</h1>"
        
    arquivos = sorted(os.listdir(SCREENSHOT_FOLDER), reverse=True)
    imagens_html = ''.join([f'<img src="/img/{nome}" width="500"><br>' for nome in arquivos])
    return render_template_string(f"""
    <html><body>
    <h1>Prints de Tela</h1>
    {imagens_html}
    </body></html>
    """)

@app.route('/img/<path:nome>')
def serve_img(nome):
    return send_from_directory(SCREENSHOT_FOLDER, nome)
