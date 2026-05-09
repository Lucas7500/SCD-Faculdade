import requests
from const import REST_SERVER_URL

def run():
    print("--- Querying Latest Temperature ---")
    try:
        response = requests.get(f"{REST_SERVER_URL}/latest")
        response.raise_for_status()
        latest = response.json()
        print(f"Latest: {latest['value']}°C at {latest['timestamp']} ({latest['type']})")
    except Exception as e:
        print(f"Error fetching latest: {e}")

    print("\n--- Querying Historical Data ---")
    try:
        response = requests.get(f"{REST_SERVER_URL}/history")
        response.raise_for_status()
        history = response.json()
        for reading in history['readings']:
            print(f"{reading['timestamp']}: {reading['value']}°C ({reading['type']})")
    except Exception as e:
        print(f"Error fetching history: {e}")

if __name__ == '__main__':
    run()
