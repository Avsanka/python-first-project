from flask import Flask, url_for, render_template
from repository import shop

app = Flask(__name__)


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

def convert(x):
    return{
        'category_id': x.get('id'),
        'heading': x.get('title'),
        'image_title': x.get('title'),
        'subheading': x.get('description'),
        'image.src': x.get('image_url')
    }


@app.route('/')
def index():
    links = generate_links()

    categories = shop.find_all_categories()
    slides = list()
    for x in categories:
        slide = {
        'category_id': x.get('id'),
        'heading': x.get('title'),
        'image_title': x.get('title'),
        'subheading': x.get('description'),
        'image_src': x.get('image_url')
    }
    slides.append(slide)

    return render_template('index.html', links=links, slides=slides)


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

@app.route('/category/<int:category_id>')
def category_page(category_id):
    links = generate_links()

    category = shop.find_category(category_id)
    products = shop.find_products_by_category(category_id)

    return render_template(
        'category.html',
        products=products,
        category=category,
        links=links,
    )

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
