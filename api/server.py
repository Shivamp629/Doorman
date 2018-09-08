from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

USERS = {
    '1': {'user': 'raghav'
              'playlist':
                {

                }
              'emotion':
              },

    '2': {'user': 'varun'
              'playlist':
                {

                }
              'emotion':
              },


    '3': {'user': 'shivam'
              'playlist':
                {

                }
              'emotion':
              },

    '4': {'user': 'akhila'
              'playlist':
                {

                }
              'emotion':
              }
}


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="user {} doesn't exist".format(USERS[user_id].user))

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
api.add_resource(Playlist, '/users/<user_id>/playlist')
api.add_resource(Song, '/users/<user_id>/playlist/song')

if __name__ == '__main__':
    app.run(debug=True)
