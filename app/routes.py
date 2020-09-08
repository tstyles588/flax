from app import app
from flask import render_template

@app.route('/')
def index():
    context = {
        'users': ['josh', 'nisarg', 'ken', 'tomas']
    }
    return render_template('index.html', **context)

    @app.route('/about')
    def about():
        context = {
            'logged_in_user': 'Derek',
            'info_to_display': 'This is Flask'
        }
        return render_template('about.html', **context)
