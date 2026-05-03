import requests


def get_public_health_fact() -> str:
    """
    Uses a public health API and converts the response into natural language.
    """
    url = "https://disease.sh/v3/covid-19/all"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        cases = data.get("cases", "not available")
        deaths = data.get("deaths", "not available")
        recovered = data.get("recovered", "not available")

        return (
            "Here is a brief public health data summary based on the latest API response: "
            f"globally, there have been approximately {cases:,} reported COVID-19 cases, "
            f"{deaths:,} deaths, and {recovered:,} recoveries. "
            "This information can help researchers understand disease burden at a population level."
        )

    except Exception as e:
        return f"I could not retrieve the API data right now. Error: {e}"