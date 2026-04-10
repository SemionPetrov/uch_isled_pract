# Импортируем основной класс Flask
from flask import Flask, render_template, request
from werkzeug.utils import redirect
import sqlite3

app = Flask(__name__)
ADMIN_PASSWORD = "okyrvamatka"

def init_db():
    with sqlite3.connect("games.db") as conn:
        with open("data.sql", "r", encoding="utf-8") as f:
            script = f.read()
            conn.executescript(script)


@app.route("/")
def hello():
    return render_template("index.html")



@app.route("/games")
def MyGame():
    with sqlite3.connect("games.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, min_players, max_players, min_play_time, max_play_time, UPDT FROM games")
        games = cursor.fetchall()
    return render_template("games.html", games=games)




@app.route("/about_me")
def about_me():
    return render_template("about_me.html")




@app.route("/add")
def form_add_game():
    return render_template("add.html")




@app.route("/add_games", methods=['POST'])
def add_game():
    password = request.form.get("password")


    if password != ADMIN_PASSWORD:
        return """<script>alert("Неверный пароль!"); window.history.back();</script>""", 403

    title = request.form["title"]
    description_game = request.form["description"]
    mi_number_player = request.form["min_number_player"]
    ma_number_player = request.form["max_number_player"]
    mi_playing_time = request.form['min_playing_time']
    ma_playing_time = request.form['max_playing_time']
    UPDT= 1

    with sqlite3.connect("games.db") as conn:
        conn.execute("""
            INSERT INTO games (title, description, min_players, max_players, min_play_time, max_play_time, UPDT)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            description_game,
            mi_number_player,
            ma_number_player,
            mi_playing_time,
            ma_playing_time,
            UPDT))
    return redirect("/add")





@app.route("/update_game", methods = ['POST'])
def up_gam():

    password = request.form.get("password")
    if password != ADMIN_PASSWORD:
        return """<script>alert("Неверный пароль!"); window.history.back();</script>""", 403
    with sqlite3.connect("games.db") as conn:
        cursor = conn.cursor()
        number_game = request.form["num_gam"]
        cursor.execute(f"UPDATE games SET UPDT = 0 WHERE id = {number_game}")
        cursor.execute("SELECT id, title, description, min_players, max_players, min_play_time, max_play_time, UPDT FROM games")
        games = cursor.fetchall()
    return render_template("games.html", games=games, )





@app.route("/save_update", methods = ['POST'])
def s_u():
    number_game = request.form["num_gam"]
    title = request.form["title"]
    description_game = request.form["description"]
    mi_number_player = request.form["min_number_player"]
    ma_number_player = request.form["max_number_player"]
    mi_playing_time = request.form['min_playing_time']
    ma_playing_time = request.form['max_playing_time']
    UPDT = 1
    with sqlite3.connect("games.db") as conn:
        cursor = conn.cursor()
        conn.execute("""
        UPDATE games SET 
        title = ?, 
        description = ?, 
        min_players = ?, 
        max_players = ?, 
        min_play_time = ?, 
        max_play_time = ?,
        UPDT = 1 
        WHERE id = ?
        """,
(
        title,
        description_game,
        mi_number_player,
        ma_number_player,
        mi_playing_time,
        ma_playing_time,
        number_game
        ))
        cursor.execute("SELECT id, title, description, min_players, max_players, min_play_time, max_play_time, UPDT FROM games")
        games = cursor.fetchall()
    return render_template("games.html", games=games)






@app.route("/delete_game", methods = ['POST'])
def del_gam():
    password = request.form.get("password")
    if password != ADMIN_PASSWORD:
        return """<script>alert("Неверный пароль!"); window.history.back();</script>""", 403

    number_game = request.form["num_gam"]
    with sqlite3.connect("games.db") as conn:
        conn.execute(f"""DELETE FROM games
            WHERE (id) = {number_game}""")
    return redirect("/games")







if __name__ == "__main__":
    init_db()
    app.run(debug=True)