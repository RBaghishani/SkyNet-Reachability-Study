import requests
import pandas as pd

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
