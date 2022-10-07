**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

![Pods](https://github.com/baocongchen/Metrics-Dashboard-with-Grafana-and-Prometheus/blob/main/answer-img/pods.png "Pods")

## Setup the Jaeger and Prometheus source
![Grafana Home Page](https://github.com/baocongchen/Metrics-Dashboard-with-Grafana-and-Prometheus/blob/main/answer-img/grafana-homepage.png "Grafana Home Page")

## Create a Basic Dashboard
![Grafana Dashboard](https://github.com/baocongchen/Metrics-Dashboard-with-Grafana-and-Prometheus/blob/main/answer-img/grafana-dashboard.png "Grafana Dashboard")

## Describe SLO/SLI

A Service-Level Indicator (SLI) is a specific metric used to measure the performance of a service.
- SLI for *monthly uptime* is percentage of server uptime in a monthly period
- SLI for *request response time* is remote response latency 

## Creating SLI metrics.

1. 99.95% of all response codes from Backend app in the last one month are in 200-399 range. 
2. 0.04% of all response codes from Backend app in the last one month are in 400-499 range. 
3. 0.01% of all response codes from Backend app in the last one month are in 500-599 range. 
4. Average RAM utilization on weekdays is 70% in the past one month. 
5. 50% of 300Mbps Network Bandwidth is utilized on weekdays in the past one month.

## Create a Dashboard to measure our SLIs
![Uptime](https://github.com/baocongchen/Metrics-Dashboard-with-Grafana-and-Prometheus/blob/main/answer-img/uptime.png "Uptime")

## Tracing our Flask App
Jaeger Tracing was implemented in reference-app/backend/app.py and reference-app/frontend/app.py

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
