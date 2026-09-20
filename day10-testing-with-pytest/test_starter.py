import pytest
from unittest.mock import patch
import starter


@pytest.fixture
def mock_temp():
    """Patches fetch_temperature for the duration of one test, and lets
    that test set whatever return value it needs via mock_temp.return_value.
    """
    with patch("starter.fetch_temperature") as mock:
        yield mock


@pytest.mark.parametrize("temp, expected_category", [
    (10, "freezing"),
    (45, "cold"),
    (70, "mild"),
    (90, "hot"),
])
def test_describe_weather_categories(mock_temp, temp, expected_category):
    mock_temp.return_value = temp
    result = starter.describe_weather("College Park")
    assert expected_category in result
    assert "College Park" in result
    assert str(temp) in result


def test_describe_weather_calls_fetch_with_city_name(mock_temp):
    mock_temp.return_value = 50
    starter.describe_weather("Pleasanton")
    mock_temp.assert_called_once_with("Pleasanton")


def test_fetch_temperature_not_mocked_raises():
    # Sanity check: the real function is genuinely unimplemented, proving
    # the tests above only pass because of the mock, not real network access.
    with pytest.raises(NotImplementedError):
        starter.fetch_temperature("Anywhere")
