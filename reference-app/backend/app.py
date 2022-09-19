from os import getenv
from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo
from jaeger_client import Config
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

JAEGER_AGENT_HOST = getenv('JAEGER_AGENT_HOST', 'localhost')
config = Config(
    config={
        'sampler':
        {
            'type': 'const',
            'param':1
        },
        'logging': True,
        'local_agent': {
            'reporting_host': JAEGER_AGENT_HOST
        },
    },
    service_name="backend"
)
tracer = config.initialize_tracer()

@app.route("/")
def homepage():
    with tracer.start_span('home') as span:
        span.set_tag('home-tag', "Hello, world!")
    return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span('api') as span:
        answer = "something"
        span.set_tag('api-tag', "Hello, world!")
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
