# Muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hakkinda')
def hakkinda():
    return render_template('about.html')

@app.route('/degisim')
def degisim():
    return render_template('iklim_degisimi.html')

@app.route('/sinav')
def sinav():
    return render_template('iklim_sinav.html')

@app.route("/cevap")
def cevap():
    return render_template("cevaplar.html")

if __name__ == '__main__':
    app.run(debug=True)