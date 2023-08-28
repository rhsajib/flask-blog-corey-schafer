from flask import Flask, render_template
from forms import RegistrationForm, LoginForm   


app = Flask(__name__)
app.config['SECRET_KEY'] = '5e1f86e8dc3ccb9b8641dcbec666e5d603fdc8aa'

posts = [
    {
        'author': 'Woki Nia',
        'title': 'Blog Post 1',
        'content': 'first post content'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'second post content'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)