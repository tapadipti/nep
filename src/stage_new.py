import json, os

metrics_dict = {"loss": 0.05, "accuracy": 0.95}

OUTPUT_DIR = "output"
METRICS_FILE = os.path.join(OUTPUT_DIR, "metrics.json")
with open(METRICS_FILE, "w") as f:
    f.write(json.dumps(metrics_dict))


