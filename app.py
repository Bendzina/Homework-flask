# აღწერეთ ჩანაწერის განახლების ლოგიკ, გამოიყენეთ html 
# ფაილები რომელიც გიტჰაბზეა ატვირთული
from flask import Flask, request, render_template, redirect, url_for
from models import db, Cars

app = Flask(__name__)

# Database configuration
host = 'localhost'
port = 5432
database = 'flask_db'
user = 'postgres'
password = '1234'

app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Home route
@app.route('/')
def index():
    all_data = Cars.query.all()

    print(all_data)

    return render_template('index.html', cars=all_data)

# Route to insert a new car
@app.route('/insert', methods=['GET', 'POST'])
def insert():

    if request.method == 'POST':

        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car = Cars(manufacturer, model, instock, price)
        db.session.add(car)
        db.session.commit()

        return redirect(url_for('Index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    car = Cars.query.get(id)
    db.session.delete(car)
    db.session.commit()

    return redirect(url_for('Index'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        car = Cars.query.get(id)

        car.manufacturer = request.form['manufacturer']
        car.model = request.form['model']
        car.instock = request.form['instock']
        car.price = request.form['price']

        db.session.commit()

        return redirect(url_for('Index'))


# if __name__ == '__main__':

#     with app.app_context():
#         db.create_all()

#     app.run(debug=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)



    