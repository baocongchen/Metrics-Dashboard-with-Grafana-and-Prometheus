from os import getenv
from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo
from jaeger_client import Config
from prometheus_flask_exporter import PrometheusMetrics
from flask_opentracing import FlaskTracing

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

metrics = PrometheusMetrics(app)

metrics.info("backend_app_info", "Backend App info", version="1.0.3")

by_endpoint_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by request endpoint',
    labels={'endpoint':lambda: request.endpoint}
)

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
    service_name="backend-service"
)
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)

@app.route("/")
@by_endpoint_counter
def homepage():
    with tracer.start_span('home') as span:
        span.set_tag('home-tag', "Hello, world!")
    return "Hello World"


@app.route("/api")
@by_endpoint_counter
def my_api():
    with tracer.start_span('api') as span:
        answer = "Hello, world!"
        span.set_tag('api-tag', answer)
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
@by_endpoint_counter
def add_star():
    with tracer.start_span('star') as span:
        star = mongo.db.stars
        name = request.json["name"]
        distance = request.json["distance"]
        star_id = star.insert({"name": name, "distance": distance})
        new_star = star.find_one({"_id": star_id})
        output = {"name": new_star["name"], "distance": new_star["distance"]}
        span.set_tag('star-tag', 'star')
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
