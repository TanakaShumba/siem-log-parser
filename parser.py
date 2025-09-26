import json
from collections import Counter

def load_logs(path):
    with open(path, "r") as f:
        return json.load(f)

def summarize_logs(log_file):
    logs = load_logs(log_file)
    events = Counter(log["event"] for log in logs)
    print("Event Summary:")
    for event, count in events.items():
        print(f"  {event}: {count}")
    print("\nDetailed Logs:")
    for log in logs:
        print(f"  {log['timestamp']} - {log['host']} - {log['event']} - {log['user']}")

if __name__ == "__main__":
    summarize_logs("sample_logs.json")
