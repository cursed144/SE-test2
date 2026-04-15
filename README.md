# SE-test

Python project that implements a fallback mechanism between two backends and exposes Prometheus metrics.

## Backends

- Primary: `https://jsonplaceholder.typicode.com/todos`
- Secondary: `https://dummyjson.com/todos`

## Task 1: Fallback

The application first requests data from the primary backend. If it fails, it automatically switches to the secondary backend.

Returned data is normalized into a common format, and the first 10 todos are printed.

## Task 2: Prometheus metric

The project uses `prometheus_client` and exposes metrics at:

`http://localhost:8000/metrics`

A Counter named `fallback_total` tracks how many times the fallback has been triggered.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Test

### Normal case

- Run the app
- The primary backend should respond
- `/metrics` should show `fallback_total 0.0`

### Fallback case

- Temporarily change the primary URL in `config.py` to an invalid endpoint
- Run the app again
- The app should use the secondary backend
- `/metrics` should show `fallback_total 1.0`

## Task 3: JSON logs

The application logs every fallback event in JSON format.

Each fallback log contains:
- timestamp
- log level
- message
- logger name
- extra data such as the primary backend error and fallback target

This makes fallback events easier to monitor and analyze.

## Task 4: Prometheus in Docker

Prometheus was started in Docker using Docker Compose and configured to scrape the application's `/metrics` endpoint.

The metric `fallback_total` was successfully collected and visualized in the Prometheus UI at `http://localhost:9090`.

The graph shows the counter increasing when fallback events occur. If the application is restarted, the counter returns to zero because the metric is stored in memory.
