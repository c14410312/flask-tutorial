from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Dylan'}

    return render_template('index.html', title='Home', user=user)
    