import requests

def get_dashboard():
    try:
        response = requests.get(
            f"{BASE_URL}/dashboard",
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def predict(data):
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def chat(message):
    try:
        response = requests.post(
            f"{BASE_URL}/chat",
            json={"message": message},
            timeout=60
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    

def get_model_insights():
    try:
        response = requests.get(f"{BASE_URL}/model-insights")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    


def ask_ai(question, features):
    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "question": question,
            "features": features
        }
    )

    return response.json()