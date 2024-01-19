import requests
import pandas as pd
from geopy.geocoders import Nominatim

def get_country_info(city, username):
    base_url = f'http://api.geonames.org/searchJSON?name={city}&maxRows=1&username={username}'

    try:
        response = requests.get(base_url)
        data = response.json()

        print(f"City: {city}, Response: {data}")

        if 'geonames' in data and data['geonames']:
            return data['geonames'][0]['countryName']
        else:
            return 'Unknown'

    except requests.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return 'Unknown'

# Load your existing meta.csv DataFrame
meta_data = pd.read_csv('../data/reachability-meta.csv')

# Replace 'your_geonames_username' with your actual Geonames username
username = 'alaadra8'

# Create a new 'country' column based on the Geonames API
meta_data['country'] = meta_data['name'].apply(lambda city: get_country_info(city, username))

# Save the modified DataFrame back to the meta.csv file
meta_data.to_csv('../data/reachability-meta.csv', index=False)

## For the unknown ones 
geolocator = Nominatim(user_agent="xxxx@gmail.com")
meta_data = pd.read_csv('./data/reachability-meta.csv')
unknown_cities = meta_data.loc[meta_data['country'] == 'Unknown']

def city_state_country(row):
    coord = f"{row['latitude']}, {row['longitude']}"
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    country = address.get('country', '')
    row['country'] = country
    print(row)
    return row

unknown_cities = unknown_cities.apply(city_state_country, axis=1)
print(unknown_cities)
meta_data.update(unknown_cities)
meta_data.to_csv('./data/reachability-meta.csv', index=False)