from prometheus_client import Counter

fallback_counter = Counter(
    "fallback_total",
    "Number of times the fallback to the secondary backend was triggered"
)