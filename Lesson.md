## Теория на сегодня: создание форм в HTML и обработка данных через Flask

### Введение
Сегодня мы продолжим изучение веб-разработки и сосредоточимся на создании форм на сайте, а также на их обработке через Flask. Формы — важный элемент веб-страниц, позволяющий пользователям вводить и отправлять информацию. Мы узнаем, как создавать формы в HTML, как обрабатывать данные на стороне сервера и как вернуть результаты обратно на клиент.

### Что будет на уроке:
1. Создание формы на сайте.
2. Обработка данных с использованием Flask.
3. Возвращение результатов обработки данных на клиентскую сторону.

### Веб-форма
🧠 Веб-форма — это аналог бумажной формы, которая позволяет пользователям вводить информацию через текстовые поля, кнопки и другие элементы. Формы широко используются для регистрации, входа в аккаунт, отправки заявок, отзывов и других задач.

### 1. Создание формы в HTML

Начнём с создания страницы `blog.html` в проекте. В форме указываются атрибуты:
- `action` — адрес для отправки данных формы.
- `method` — метод отправки данных (GET или POST).

#### Основные теги для создания формы:
- `<form>` — контейнер для элементов формы.
- `<input>` — элемент для ввода данных.
- `<label>` — текстовая метка для полей.
- `<textarea>` — многострочное текстовое поле.
- `<button>` — кнопка для отправки данных.

#### Пример кода формы:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Контактная форма</title>
</head>
<body>
    <h1>Контактная форма</h1>
    <form action="test" method="post">
        <label for="name">Имя:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Электронная почта:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Отправить</button>
    </form>
</body>
</html>
```

#### Объяснение:
- `<form action="test" method="post">` — форма отправляется по адресу `test` с методом `POST`.
- Поля `<input>` собирают имя и почту пользователя.
- Кнопка `<button>` отправляет данные на сервер.

### 2. Взаимодействие с формами через Flask

Для начала работы с Flask создадим правильную структуру проекта:

```
my_flask_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── blog.html
├── main.py
└── static/
```

#### Настройка Flask
1. В файле `__init__.py` создаём экземпляр Flask и настраиваем конфигурацию:

```python
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

from app import routes1
```

2. В файле `routes.py` описываем логику для работы с данными формы.

```python
from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)
```

#### Описание:
- `request.form.get('title')` — получение данных, введённых пользователем в форме.
- Данные сохраняются в список `posts`, который передаётся обратно на страницу.

### 3. Создание HTML-шаблона `blog.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Простой блог</title>
</head>
<body>
    <div class="container">
        <h1>Простой блог</h1>
        <form method="POST" action="/">
            <div class="form-group">
                <label for="title">Заголовок:</label>
                <input type="text" class="form-control" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="content">Текст поста:</label>
                <textarea class="form-control" id="content" name="content" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Отправить пост</button>
        </form>
        <hr>
        <h2>Посты</h2>
        {% for post in posts %}
        <div class="post">
            <h4>{{ post.title }}</h4>
            <p>{{ post.content }}</p>
        </div>
        {% endfor %}
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

Этот шаблон позволяет отображать посты, которые отправляются через форму.

### 4. Запуск приложения

В файле `main.py` мы запускаем приложение:

```python
from app import app

if __name__ == "__main__":
    app.run(debug=True)
```

Теперь ваше приложение готово для работы. Вы можете отправлять данные через форму, и они будут отображаться на странице блога.

### Заключение
Сегодня мы научились создавать веб-формы в HTML и обрабатывать данные на сервере через Flask. Формы являются важным инструментом для взаимодействия пользователей с сайтом, а Flask позволяет легко обрабатывать и возвращать данные.