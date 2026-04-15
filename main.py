import time
from prometheus_client import start_http_server

from config import METRICS_PORT
from exceptions import BackendError
from services.fallback_service import fetch_todos_with_fallback


def main() -> None:
    start_http_server(METRICS_PORT)
    print(f"Prometheus metrics available at: http://localhost:{METRICS_PORT}/metrics")

    while True:
        try:
            todos = fetch_todos_with_fallback()
            print(f"Fetched {len(todos)} todos. First source: {todos[0]['source']}")
        except BackendError as e:
            print(f"Error: {e}")

        time.sleep(5)


if __name__ == "__main__":
    main()