from flask import render_template, request
from app import app

@app.route("/", methods=["GET", "POST"])
def user_form():
    # Инициализация переменных
    user_data = None

    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Сохраняем данные в виде словаря
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

    return render_template('form.html', user_data=user_data)
