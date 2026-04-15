import json
import logging
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        if hasattr(record, "extra_data"):
            log_entry["extra_data"] = getattr(record, "extra_data")

        return json.dumps(log_entry)


def get_logger(name: str = "fallback_logger") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())

        logger.addHandler(handler)
        logger.propagate = False

    return logger