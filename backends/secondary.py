import requests
from typing import List, Dict, Any

from config import SECONDARY_URL, TIMEOUT
from exceptions import BackendError


def fetch_from_secondary() -> List[Dict[str, Any]]:
    try:
        response = requests.get(SECONDARY_URL, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict) or "todos" not in data:
            raise BackendError("Secondary backend returned unexpected format.")

        return [
            {
                "id": item.get("id"),
                "title": item.get("todo"),
                "completed": item.get("completed"),
                "source": "secondary",
            }
            for item in data["todos"]
        ]

    except (requests.RequestException, ValueError) as e:
        raise BackendError(f"Secondary backend failed: {e}")