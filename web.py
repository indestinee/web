from flask import Flask, render_template, redirect, url_for

if __name__ == '__main__':
    app = Flask(__name__, static_folder='templates', static_url_path='')
    app.config['SECRET_KEY'] = 'AKALFHUEWSAiowqjodas'  

@app.route("/")
def index(): 
    html_items = {
        'template_name_or_list': 'index.html',
        'icss': get_ics(),
    }
    return render_template(**html_items)

if __name__ == '__main__':
    port = 1236
    app.run(host='::', port=port, debug=True)
