from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

metrics.info("frontend_app_info", "Frontend App Info", version="1.0.3")

by_path_counter = metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by paths',
        labels={'path': lambda: request.path}
    )
)


@app.route("/")
@by_path_counter
def homepage():
    return render_template("main.html")



if __name__ == "__main__":
    app.run()
