from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
    db = SQLAlchemy(app)

    class Games(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        game = db.Column(db.String(100), nullable=False)
        year = db.Column(db.String(100), nullable=False, unique=True)

    with app.app_context():
        db.create_all()

    @app.route('/add_game', methods=['POST'])
    def add_game():
        game = request.form['game']
        year = request.form['year']

        new_game = Games(game=game, year=year)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('base'))

    @app.route('/')
    def base():
        games = Games.query.all()
        return render_template('base.html', games=games)

    @app.route('/clear_database', methods=['POST'])
    def clear_database():
        db.session.query(Games).delete()
        db.session.commit()
        return redirect(url_for('base'))

    app.run(port=5001)
