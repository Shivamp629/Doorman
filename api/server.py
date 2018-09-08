from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions


app = FlaskAPI(__name__)


@app.route("/users", methods=['GET', 'POST'])
def user_list():
    if request.method == 'GET':
        data = str(request.data.get('text', ''))
        return '', status.HTTP_200_OK

    if request.method == 'POST':
        data = str(request.data.get('text', ''))
        return '', status.HTTP_201_CREATED


@app.route("/logs/<string:user>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(user):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        data = str(request.data.get('text', ''))
        return ''

    elif request.method == 'DELETE':
        return '', status.HTTP_204_NO_CONTENT

    elif request.method == 'GET':
        return '', status.HTTP_200_OK


if __name__ == "__main__":
    app.run(debug=True)
