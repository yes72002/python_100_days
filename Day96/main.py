from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from sqlalchemy import func
import requests

import random

app = Flask(__name__)

# https://www.openbrewerydb.org/documentation/#list-breweries
# GET https://api.openbrewerydb.org/v1/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0
# GET https://api.openbrewerydb.org/v1/breweries?per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_city=san_diego&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_dist=32.88313237,-117.1649842&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_ids=701239cb-5319-4d2e-92c1-129ab0b3b440,06e9fffb-e820-45c9-b107-b52b51013e8f
# GET https://api.openbrewerydb.org/v1/breweries?by_name=san_diego&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_state=california&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_postal=92101&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?by_type=micro&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?page=15&per_page=3
# GET https://api.openbrewerydb.org/v1/breweries?per_page=2
# GET https://api.openbrewerydb.org/v1/breweries?by_city=san_diego&per_page=3
# http://127.0.0.1:5000/?by_city=san_diego&per_page=3

@app.route("/")
def home():
    query_string = request.query_string.decode('utf-8')
    print(query_string) # by_city=san_diego&per_page=3

    # by_city = request.args.get('by_city')
    # by_name = request.args.get('by_name')
    # per_page = request.args.get('per_page')
    # 多的argument沒用，他只會判斷第一個跟per_page
    # print(by_city)
    # print(by_name) # 沒有會是None
    # print(per_page)

    api_result = requests.get(f'https://api.openbrewerydb.org/v1/breweries?{query_string}')
    api_response = api_result.json()

    return jsonify(cafe = api_response)


if __name__ == '__main__':
    app.run(debug=True)
