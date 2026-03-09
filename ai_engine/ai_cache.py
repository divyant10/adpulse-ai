import json
import os

CACHE_FILE = "cache/ai_recommendations.json"


def save_cache(result):

    os.makedirs("cache", exist_ok=True)

    with open(CACHE_FILE, "w") as f:
        json.dump({"result": result}, f)


def load_cache():

    if os.path.exists(CACHE_FILE):

        with open(CACHE_FILE) as f:
            data = json.load(f)
            return data.get("result")

    return None