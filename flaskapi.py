from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

import datetime

class HelloWorld(Resource):
    def get(self):
        return {
            'hello': 'world',
            'message': 'Server is running!',
            'date': str(datetime.datetime.now())
        }


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)
