from typing import List, Dict, Any

from backends.primary import fetch_from_primary
from backends.secondary import fetch_from_secondary
from exceptions import BackendError
from metrics import fallback_counter
from logger_config import get_logger

logger = get_logger()


def fetch_todos_with_fallback() -> List[Dict[str, Any]]:
    try:
        print("Trying primary backend...")
        return fetch_from_primary()
    except BackendError as primary_error:
        print(primary_error)
        print("Falling back to secondary backend...")

        fallback_counter.inc()

        logger.info(
            "Fallback triggered",
            extra={
                "extra_data": {
                    "primary_error": str(primary_error),
                    "fallback_target": "secondary",
                }
            },
        )

        return fetch_from_secondary()