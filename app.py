# app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def plot():
    # Gerar dados para o gráfico
    x = range(1, 11)
    y = [i**2 for i in x]
    
    # Criar o gráfico
    plt.figure()
    plt.plot(x, y)
    plt.title('Gráfico Simples')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Renderizar no template HTML
    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
