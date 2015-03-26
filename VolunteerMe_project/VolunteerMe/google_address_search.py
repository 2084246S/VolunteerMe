import urllib2
import json


def run_query(location):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    # Should not use raw key
    address = location.replace(' ', '+')  # '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    # address = urlencode(address);

    final_url = '{0}address={1}'.format(base_url, address)

    results = []

    try:
        response = urllib2.urlopen(final_url).read()

        json_response = json.loads(response)

        #Change to only a single result
        for result in json_response['results']:
            results.append({
                'lat': result['geometry']['location']['lat'],
                'lng': result['geometry']['location']['lng']})

        #DEBUG
        print(final_url)

    except:
        #TODO perform error checking
        pass

    return results