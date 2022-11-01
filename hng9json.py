from flask import Flask, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class theo(Resource):
    def get(self):
        all = jsonify({
            "slackUsername": "greatchudim",
            "backend": True,
            "age": 29,
            "bio": "A budding Python Developer, curious and ready to break boundaries."
        })

        return all


api.add_resource(theo, "/")

app.run()
