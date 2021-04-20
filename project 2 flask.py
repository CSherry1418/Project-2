
from flask import Flask, jsonify, render_template
import json
import os
import pandas as pd
from flask_cors import CORS
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from sql_setup import setup_dependencies
engine, session, , Rushing = setup_dependencies(app)



app = Flask(__name__)
CORS(app)



@app.route('/')
def welcome():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Baseball API!<br/>"
        f"Available Routes:<br/>"
    )


engine = create_engine("Resources\MLB_combined_db.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

@app.route("Resources\MLB_combined_db.sqlite/mlb_wins")
def mlb_wins():
    session = Session(engine)
    results = session.query(Team.name).all()
    session.close()
    all_teams = list(np.ravel(results))
    return jsonify(all_teams)


@app.route("Resources\MLB_db.sql/mlb_beer_prices")
def mlb_beer_prices():
    session = Session(engine)
    results = session.query(Team.nickname, Team.price).all()
    session.close()

    all_teams = []
    for nickname, price, price_per_ounce in results:
        team_dict = {}
        team_dict["nickname"] = nickname
        team_dict["price"] = price
        all_teams.append(team_dict)

    return jsonify(all_teams)


if __name__ == '__main__':
    app.run(debug=True)

