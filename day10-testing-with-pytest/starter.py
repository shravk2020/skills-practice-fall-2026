def fetch_temperature(city):
    """Pretend this calls a real weather API over the network.
    Not implemented here -- in tests, this gets mocked out entirely.
    """
    raise NotImplementedError("this would call a real API in production")


def describe_weather(city):
    """Calls fetch_temperature(city) to get a temperature in Fahrenheit,
    then returns a message:
    - temp < 32: f"{city}: freezing ({temp}°F)"
    - 32 <= temp < 60: f"{city}: cold ({temp}°F)"
    - 60 <= temp < 80: f"{city}: mild ({temp}°F)"
    - temp >= 80: f"{city}: hot ({temp}°F)"

    TODO: implement using fetch_temperature(city).
    """
    pass
