from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

USERS = {
    'raghav': {'user_id': '1'
              'playlist':
                {

                }
              'emotion':
              },

    'varun': {'user_id': '2'
              'playlist':
                {

                }
              'emotion':
              },


    'shivam': {'user_id': '3'
              'playlist':
                {

                }
              'emotion':
              },

    'akhila': {'user_id': '4'
              'playlist':
                {

                }
              'emotion':
              }
}


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="user {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# user
# shows a single user item and lets you delete a user item
class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        USERS[user_id] = task
        return task, 201


# userList
# shows a list of all USERS, and lets you POST to add new tasks
class Users(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        user_id = int(max(USERS.keys()).lstrip('user')) + 1
        user_id = 'user%i' % user_id
        USERS[user_id] = {'task': args['task']}
        return USERS[user_id], 201


# userList
# shows a list of all USERS, and lets you POST to add new tasks
class DetermineUser(Resource):
    def get(self):
        user_id = get_user_id()
        return {'user': user_id}

##
## Actually setup the Api resource routing here
##
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<user_id>')
api.add_resource(DetermineUser, '/DetermineUser')
api.add_resource(Emotion, '/users/<user_id>/emotion')
api.add_resource(Playlist, '/users/<user_id>/<emotion>/playlist')
api.add_resource(Song, '/users/<user_id>/<emotion>/playlist/<song>')

if __name__ == '__main__':
    app.run(debug=True)
