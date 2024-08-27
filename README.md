# Geolocation Utility - Fetch Coding Challenge

This project is a coding challenge for the Software Development Engineer in Test (SDET) position at Fetch. The challenge involves creating a Python utility that retrieves the latitude, longitude, place name, and country information for given locations using the OpenWeather Geocoding API. The utility can handle inputs in the form of city names, state abbreviations, or zip codes, and it can process multiple locations at once.

Additionally, the utility includes a feature to convert US state abbreviations to full state names before making the API request. The code is designed with testing in mind and includes a test suite using `pytest`.

## Features

- Retrieve geolocation data (latitude, longitude) for cities, states, and zip codes.
- Convert state abbreviations (e.g., "WI") to full state names (e.g., "Wisconsin").
- Handle multiple location inputs via the command line.
- Display output in a readable format: place name, country, and coordinates.

## Setup

This repo requires [python3](https://www.python.org/downloads/) and pip. This test was developed in python 3.12.2

1. Clone the repository: 
 ```git clone git@github.com:asalazar516/fetch_geoloc_coding_exercise.git ```

1. Set up your OpenWeather API key:
    1. Obtain an API key from [OpenWeather](https://openweathermap.org/api).
    1. Replace the placeholder in the script (geoloc_util.py) with your actual API key

### Install Requirements

To run this utility and its tests, you need the following Python packages:

- `requests`
- `pytest`

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the utility from the command line run

```bash
python geoloc_util.py {location}
```

You can also run the utility by adding multiple locations (locations argument is optional):
Example
```bash
python geoloc_util.py --locations "Springfield" "Los Angeles, CA" "91801"
```

### Running the tests
The utility includes a test suite using pytest. You can run the tests to verify that the utility works as expected.
To run the test suite with added logs, run
``` bash
python -m pytest .\test_geoloc_util.py -vs
```

## Attributions
The us_state_abbreviations.py script was adapted from a gist by Jeff Paine. You can find the original gist [here](https://gist.github.com/JeffPaine/3083347#file-us_state_abbreviations-py).