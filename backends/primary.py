import requests
from typing import List, Dict, Any

from config import PRIMARY_URL, TIMEOUT
from exceptions import BackendError


def fetch_from_primary() -> List[Dict[str, Any]]:
    try:
        response = requests.get(PRIMARY_URL, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, list):
            raise BackendError("Primary backend returned unexpected format.")

        return [
            {
                "id": item.get("id"),
                "title": item.get("title"),
                "completed": item.get("completed"),
                "source": "primary",
            }
            for item in data
        ]

    except (requests.RequestException, ValueError) as e:
        raise BackendError(f"Primary backend failed: {e}")