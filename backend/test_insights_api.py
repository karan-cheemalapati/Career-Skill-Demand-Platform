import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health():
    response = requests.get(f"{BASE_URL}/insights/health")
    print("HEALTH:", response.status_code)
    print(response.json())
    print("-" * 50)


def test_questions():
    response = requests.get(f"{BASE_URL}/insights/questions")
    print("QUESTIONS:", response.status_code)
    print(response.json())
    print("-" * 50)


def test_metadata():
    response = requests.get(f"{BASE_URL}/insights/filters/metadata")
    print("METADATA:", response.status_code)
    print(response.json())
    print("-" * 50)


def test_text_insights():
    payload = {
        "text": "Python SQL machine learning communication research",
        "mode": "full"
    }
    response = requests.post(f"{BASE_URL}/insights/text", json=payload)
    print("TEXT INSIGHTS:", response.status_code)
    print(response.json())
    print("-" * 50)


def test_filter():
    params = {
        "skill": "Programming",
        "min_salary": 80000,
        "min_skill_score": 3.5,
        "education": "Bachelor's degree"
    }
    response = requests.get(f"{BASE_URL}/insights/occupations/filter", params=params)
    print("FILTER:", response.status_code)
    print(response.json())
    print("-" * 50)


def test_occupation_detail():
    response = requests.get(f"{BASE_URL}/insights/occupation/15-1252")
    print("OCCUPATION DETAIL:", response.status_code)
    print(response.json())
    print("-" * 50)


if __name__ == "__main__":
    test_health()
    test_questions()
    test_metadata()
    test_text_insights()
    test_filter()
    test_occupation_detail()