import os

config = {
    'api_url_template': os.environ.get('API_URL_TEMPLATE'),
    'api_key': os.environ.get('API_KEY'),
    'api_config': {
        'units': 'metric',
        'language': 'ru'
    }
}