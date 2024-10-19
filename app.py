from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/authorization' , methods=['GET', 'POST'])
def avtoriza_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']

        if username == 'user' and password == 'user':
            return redirect('/user')
        else:
            return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="..\static\style.css">
</head>
<body>
    <div class="vse">             
        <div class="okno">
            <div class="okno-dialog">
                <div class="okno-content">
                    <img src="../static/img/logo.jpg" >
                    <div class="okno-form">
                        <div class="fufs">
                        <form action="#" method="post">
                            <input class="gril" type="text" placeholder="Логин" name="username">
                            <input type="password" placeholder="Пароль" name="password">
                            <p>Введите корректный логин и пароль</p>
                            <a href="#" class="href">Восстановить</a>
                            <button class="btn">Войти</button>
                        </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
    return render_template('avtoriza.html')


@app.route('/user')
def test_page():
    return render_template('test.html')

@app.route('/')
def index_page():
    return render_template('index.html')


app.run(debug=True)