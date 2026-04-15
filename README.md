# SE-test

Python project that implements a **fallback mechanism** between two backends and exposes **Prometheus metrics**.

## Backends

- Primary: `https://jsonplaceholder.typicode.com/todos`
- Secondary: `https://dummyjson.com/todos`

## Task 1: Fallback

The application first requests data from the **primary backend**.  
If it fails, it automatically switches to the **secondary backend**.

Returned data is normalized into a common format and the first 10 todos are printed.

## Task 2: Prometheus metric

The project uses `prometheus_client` and exposes metrics at:

`http://localhost:8000/metrics`

A Counter named `fallback_total` tracks how many times the fallback has been triggered.

## Install

```bash
pip install -r requirements.txt

Run
python main.py
Test

Normal case:

run the app
primary backend should respond
/metrics should show fallback_total 0.0

Fallback case:

temporarily change the primary URL in config.py to an invalid endpoint
run the app again
the app should use the secondary backend
/metrics should show fallback_total 1.0