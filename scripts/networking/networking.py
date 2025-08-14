import requests


def fetch_data_from_api(url):
    """Fetch data from the specified API URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
