def fetch_temperature(city):
    raise NotImplementedError("this would call a real API in production")


def describe_weather(city):
    temp = fetch_temperature(city)
    if temp < 32:
        category = "freezing"
    elif temp < 60:
        category = "cold"
    elif temp < 80:
        category = "mild"
    else:
        category = "hot"
    return f"{city}: {category} ({temp}°F)"
