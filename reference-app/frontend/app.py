from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config

app = Flask(__name__)

metrics = PrometheusMetrics(app)

metrics.info("frontend_app_info", "Frontend App Info", version="1.0.3")

by_path_counter = metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by paths',
        labels={'path': lambda: request.path}
    )
)

config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name='frontend'
)

tracer= config.initialize_tracer()

@app.route("/")
@by_path_counter
def homepage():
    with tracer.start_span('html'):
        return render_template("main.html")



if __name__ == "__main__":
    app.run()
