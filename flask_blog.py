from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'J.K. Rowling',
        'title': 'Fantastic Beasts and Where to Find Them',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'J.R.R. Tolkien',
        'title': 'The Fall of Gondolin',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts  = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')
    

if __name__ == '__main__':
    app.run(debug=True)