import pytest
from unittest.mock import patch, MagicMock
from geoloc_util import get_location_data, get_locations_data 

# Test that the API returns a 200 status code
@patch('geoloc_util.requests.get')
def test_api_returns_200(mock_get):
    # Mocking the response to simulate a 200 status code
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "lat": 34.0522,
        "lon": -118.2437,
        "name": "Los Angeles",
        "state": "California",
        "zip": None,
        "country": "US"
    }]
    mock_get.return_value = mock_response

    # Test with a valid city and state
    location = "Los Angeles, California"
    result = get_location_data(location)

    # Assertions
    assert result is not None
    assert "latitude" in result
    assert "longitude" in result
    assert result["place_name"] == "Los Angeles, California"

# Test with a valid city name
def test_valid_city():
    locations = ["Los Angeles"]
    result = get_locations_data(locations)
    
    assert "Los Angeles" in result
    assert isinstance(result["Los Angeles"], dict)
    assert "latitude" in result["Los Angeles"]
    assert "longitude" in result["Los Angeles"]
    assert result["Los Angeles"]["country"] == "US"

# Test with a valid city and state abbreviated
def test_valid_city_state_abbrev():
    locations = ["Madison, WI"]
    result = get_locations_data(locations)
    
    assert "Madison, WI" in result
    assert isinstance(result["Madison, WI"], dict)
    assert "latitude" in result["Madison, WI"]
    assert "longitude" in result["Madison, WI"]
    assert result["Madison, WI"]["country"] == "US"

# Test with a valid US ZIP code
def test_valid_zip_code():
    locations = ["91801"]
    result = get_locations_data(locations)
    
    assert "91801" in result
    assert isinstance(result["91801"], dict)
    assert "latitude" in result["91801"]
    assert "longitude" in result["91801"]
    assert "zip" in result["91801"]
    assert result["91801"]["country"] == "US"

# Test with an invalid location
def test_invalid_location():
    locations = ["Invalid Location"]
    result = get_locations_data(locations)
    
    assert "Invalid Location" in result
    assert result["Invalid Location"] == "Location not found or invalid"

# Test with multiple locations (valid and invalid)
def test_multiple_locations():
    locations = ["Madison, Wisconsin", "12345", "Chicago, IL", "Invalid Location"]
    result = get_locations_data(locations)
    
    # Check the valid city/state
    assert "Madison, Wisconsin" in result
    assert isinstance(result["Madison, Wisconsin"], dict)
    assert "latitude" in result["Madison, Wisconsin"]
    assert "longitude" in result["Madison, Wisconsin"]
    assert result["Madison, Wisconsin"]["country"] == "US"
    
    # Check the valid ZIP code
    assert "12345" in result
    assert isinstance(result["12345"], dict)
    assert "latitude" in result["12345"]
    assert "longitude" in result["12345"]
    assert "zip" in result["12345"]

    # Check the valid city/state abbreviated
    assert "Chicago, IL" in result
    assert isinstance(result["Chicago, IL"], dict)
    assert "latitude" in result["Chicago, IL"]
    assert "longitude" in result["Chicago, IL"]
    assert result["Chicago, IL"]["country"] == "US"
    
    # Check the invalid location
    assert "Invalid Location" in result
    assert result["Invalid Location"] == "Location not found or invalid"

# Test with an empty location input
def test_empty_location():
    locations = [""]
    result = get_locations_data(locations)
    
    assert "" in result
    assert result[""] == "Location not found or invalid"

# Test with a location containing special characters
def test_special_characters_location():
    locations = ["@#$$%"]
    result = get_locations_data(locations)
    
    assert "@#$$%" in result
    assert result["@#$$%"] == "Location not found or invalid"
