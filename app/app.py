from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about-us")
def about_us():
    return render_template('about_us.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route("/dasboard")
def dasboard():
    return render_template('dasboard.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)

    #activar entorno         vistual.venv\Scripts\activate
    #correr aplicacion       python app\app.py run
    #                        flask --app app\app.py run 