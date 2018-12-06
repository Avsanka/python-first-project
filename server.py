from flask import Flask, url_for, render_template

app = Flask(__name__)

import pymysql

connection = pymysql.connect(
host='192.168.33.10',
user='remote_user',
password='123123',
db='shop',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor
)

@app.route('/test/')
def test():
    cursor = connection.cursor
    cursor.execute('SELECT * FROM category')
    result = cursor.fetchall()

    return str(result[0])

def generate_links():
    with app.test_request_context():
        first_link = url_for(
            'hello_user',
            username='Nikita'
        )
        second_link = url_for(
            'hello_user',
            username='Danil The Great'
        )
        index_link = url_for('index')
        index_with_params_link = url_for(
            'index',
            param1='param1',
            param2='param2'
        )

        links = {
            "Каталог": first_link,
            "Корзина": second_link,
            'Наш блог': index_link,
            'Гарантии': index_with_params_link,
        }

    return links


@app.route('/')
def index():
    links = generate_links()
    slides = [
        {
            'image_src': 'https://bipbap.ru/wp-content/uploads/2017/04/0_7c779_5df17311_orig.jpg',
            'image_title': 'Image title',
            'heading': 'Отдохните на пляже в Таиланде',
            'subheading': 'Только у нас вы можете заказать билет по самой низкой цене',
        },
        {
            'image_src': 'https://bipbap.ru/wp-content/uploads/2017/04/3-8.jpg',
            'image_title': 'Image 2 title',
            'heading': 'Удивительная природа',
            'subheading': 'Посетите самые живописные места Южной Америки',
        },
        {
            'image_src': 'https://fullpicture.ru/wp-content/uploads/2016/09/africaplaces41.jpg',
            'image_title': 'Озеро в Африке',
            'heading': 'Озеро Виктория',
            'subheading': 'Посетите самое красивое озеро Африки',
        },
        {
            'image_src': 'https://fullpicture.ru/wp-content/uploads/2016/09/africaplaces1.jpg',
            'image_title': 'Водопад Виктория',
            'heading': 'Водопад Виктория',
            'subheading': 'Хотите ли вы посмотреть на самый крупный водопад в мире? Мы можем организовать поездку специально для вас!',
        },
    ]
    return render_template('index.html', links=links, slides=slides)


@app.route('/user/')
@app.route('/user/<username>')
def hello_user(username=None):
    links = generate_links()
    return render_template(
        'user.html',
        username=username,
        links=links,
    )


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
