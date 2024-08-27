import requests
import argparse
from us_state_abbreviations import abbreviation_to_name  # Import the state abbreviation to name mapping


API_KEY = 'f897a99d971b5eef57be6fafa0d83239' 

# Update the input if the state is abbreviated
def convert_state_abbreviation(location):
    parts = location.split(", ")
    if len(parts) == 2:
        city, state_abbr = parts
        state_name = abbreviation_to_name.get(state_abbr.upper(), state_abbr)
        return f"{city}, {state_name}"
    return location


def get_location_data(location):
    location = convert_state_abbreviation(location)  # Convert state abbreviation to full name if necessary
    base_url = "http://api.openweathermap.org/geo/1.0/"
    
    if location.isdigit() and len(location) == 5:  # Assuming it's a US ZIP code
        url = f"{base_url}zip?zip={location},US&appid={API_KEY}"
    else:
        url = f"{base_url}direct?q={location}&limit=1&appid={API_KEY}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:  # If the response is a list and not empty
            data = data[0]  # Use the first location in the list
        if data:
            return {
                "latitude": data.get("lat"),
                "longitude": data.get("lon"),
                "place_name": f"{data.get('name')}, {data.get('state', '').strip()}",
                "zip": data.get('zip'),
                "country": data.get("country")
            }
    return None

def get_locations_data(locations):
    results = {}
    for location in locations:
        data = get_location_data(location)
        if data:
            results[location] = data
        else:
            results[location] = "Location not found or invalid"
    return results

def main():
    parser = argparse.ArgumentParser(description="Geolocation Utility")
    parser.add_argument('locations', nargs='*', help="List of locations to lookup")
    parser.add_argument('--locations', nargs='*', help="Alt to provide locations")
    
    args = parser.parse_args()

    # Combine locations from both options if provided
    locations = args.locations or args.locations

    if not locations:
        print("No locations provided. Please specify locations to look up.")
        return
    
    location_data = get_locations_data(locations)

    for location, data in location_data.items():
        if isinstance(data, dict):
            place_name = data.get('place_name', 'Unknown Place')
            country = data.get('country', 'Unknown Country')
            zip = data.get('zip', '') or ''
            latitude = data.get('latitude', 'Unknown Latitude')
            longitude = data.get('longitude', 'Unknown Longitude')
            print(f"Place: {place_name} {zip}\nCountry: {country}\nCoordinates: ({latitude}, {longitude})\n")
        else:
            print(f"{location}: {data}")

if __name__ == "__main__":
    main()