from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def mission_access():
    if request.method == 'POST':
        astronaut_id = request.form['astronaut_id']
        astronaut_password = request.form['astronaut_password']
        captain_id = request.form['captain_id']
        captain_password = request.form['captain_password']

        return redirect(url_for('access_granted'))

    return render_template('access_form.html')


@app.route('/access_granted')
def access_granted():
    return "Доступ предоставлен. Миссия начнется!"


if __name__ == '__main__':
    app.run(debug=True)
