from flask import Flask, url_for, render_template

app = Flask(__name__)


def generate_links():
    with app.test_request_context():
        pinkblacklink = url_for('hello_user', username='Dave Grohl')
        KurtCobain_the_Great_link = url_for('hello_user', username='Kurt Cobain')
        index_link = url_for('index')
        index_with_params_link = url_for('index',
        param1='param1',
        param2='param2')

        links = {
            "Dave Grohl": pinkblacklink,
            "Kurt Cobain": KurtCobain_the_Great_link,
            "Krist Novoselic": index_link,
            "Index with params": index_with_params_link
        }
    return links


@app.route('/')
def index():
   links = generate_links()
   return render_template('index.html', links=links)


@app.route('/user/')
@app.route('/user/<username>')
def hello_user(username=None):
    links=generate_links()
    return render_template('user.html', username=username,links=links)


with app.test_request_context():
    link = url_for('hello_user', username='Pink Black')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
