from flask import Flask, jsonify
from views import AdsView
from errors import ApiError



app = Flask('app')


@app.errorhandler(ApiError)
def error_handler(error: ApiError):
    response = jsonify({"status": "error", "description": error.message})
    response.status_code = error.status_code

    return response


app.add_url_rule('/ads/<int:ad_id>', view_func=AdsView.as_view('ad_view'), methods=['GET', 'DELETE', 'PATCH'])
app.add_url_rule('/ads/', view_func=AdsView.as_view('ad_create'), methods=['POST'])

app.run()