from wit import Wit
import pywapi


# Quickstart example
# See https://wit.ai/l5t/Quickstart

access_token = 'YOUR_WIT_TOKEN_HERE'

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def say(session_id, context, msg):
    print(msg)

def merge(session_id, context, entities, msg):
    loc = first_entity_value(entities, 'location')
    if loc:
        context['loc'] = loc
    return context

def error(session_id, context, e):
    print(str(e))

def fetch_weather(session_id, context):
    location = context['loc']
    location_id = pywapi.get_loc_id_from_weather_com(location)[0][0]
    weather_com_result = pywapi.get_weather_from_weather_com(location_id)
    context['forecast'] = weather_com_result["current_conditions"]["text"]
    return context

actions = {
    'say': say,
    'merge': merge,
    'error': error,
    'fetch-weather': fetch_weather,
}
client = Wit(access_token, actions)

session_id = 'YOUR_WIT_USERNAME_HERE'
place = raw_input("Enter City Name:")
client.run_actions(session_id, 'weather in %s'%place, {})