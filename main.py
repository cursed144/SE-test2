from prometheus_client import start_http_server

from config import METRICS_PORT
from exceptions import BackendError
from services.fallback_service import fetch_todos_with_fallback


def main() -> None:
    start_http_server(METRICS_PORT)
    print(f"Prometheus metrics available at: http://localhost:{METRICS_PORT}/metrics")

    try:
        todos = fetch_todos_with_fallback()
        print(f"\nSuccessfully fetched {len(todos)} todos.\n")

        for todo in todos[:10]:
            print(
                f"ID: {todo['id']}, "
                f"Title: {todo['title']}, "
                f"Completed: {todo['completed']}, "
                f"Source: {todo['source']}"
            )

        input("\nPress Enter to exit...\n")

    except BackendError as e:
        print(f"Error: {e}")
        input("\nPress Enter to exit...\n")


if __name__ == "__main__":
    main()