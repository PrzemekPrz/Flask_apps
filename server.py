from flask import Flask, render_template, request
from datetime import datetime
from random import randint, shuffle

guess_this = randint(1, 100)


app = Flask(__name__)

@app.route("/")
def hello():
    return "Witaj użytkowniku!"

@app.route("/godzina")
def godzina():
    czas = datetime.now()
    return czas.strftime("%H:%M")

@app.route("/data")
def data():
    czas = datetime.now()
    return czas.strftime("(%a)%d - %B - %Y")

@app.route("/losuje")
def losuje():
    return str(randint(0, 100))

@app.route("/siema/<imie>")
def siema(imie):
    return render_template("hello.html", name=imie)

@app.route("/dodawanie/<liczba1>/<liczba2>")
def dodawanie(liczba1, liczba2):
    suma = int(liczba1) + int(liczba2)
    return f'Suma  {liczba1} i {liczba2} to {str(suma)}'


@app.route("/losuj")
def losuj():
    liczba1 = randint(0, 6)
    liczba2 = randint(0, 6)
    liczba3 = randint(0, 6)
    return f"Wynik z losowania to {liczba1}, {liczba2} oraz {liczba3}"

@app.route("/lotto")
def lotto():
    kulki = list(range(1,50))
    shuffle(kulki)
    return f'Wylosowanie liczby to : {str(kulki[:6])}'

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['user_name']  # user_name - bo tak jest w HTML
        return 'Witaj ' + name
    else:  # GET
        return render_template('welcome.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['operation']  # tak się nazywa pole w HTML: name="operation"
        print(num1, num2, op)
        if op == 'add':  # taka jest wartość opcji do wyboru w HTML: value="add"
            return str(num1 + num2)
        elif op == 'sub':
            return str(num1 - num2)
        elif op == 'mul':
            return str(num1 *  num2)
        elif op == 'div':
            return str(num1 / num2)
    else:
        return render_template('calculate.html')



@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('guess.html')
    else:
        user_guess = int(request.form['my_guess'])
        if user_guess < guess_this:
            return render_template('guess.html', outcome='Za mało!')
        elif user_guess > guess_this:
            return render_template('guess.html', outcome='Za dużo!')
        else:
            return 'Zgadłeś!'

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        name = request.form['user_name']  # user_name - bo tak jest w HTML
        surname = request.form['user_surname'] # user_surname - bo tak jest w HTML
        return 'Witaj ' + name + " " + surname
    else:  # GET
        return render_template('name.html')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')