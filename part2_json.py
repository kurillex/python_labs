import requests
import json
from funcs import *

steam_id_Roma = '76561198996672380'  # Roman Zaharchenko
steam_id_Kirill = '76561198359905514'  # Kuranov Kirill

api_key = 'MY_KEY'


def get_steam_api():
    url_nickname = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/'
    url_stats = 'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/'
    params = {
        'key': 'MY_KEY',
        'steamids': steam_id_Roma,  # for stats
        'steamid':  steam_id_Roma,  # for nickname
        'appid': '730',
        'format': 'json'
    }
    response_nickname = requests.get(url_nickname, params=params)
    response_analysis(response_nickname)
    data_nickname = response_nickname.json()

    response_stats = requests.get(url_stats, params=params)
    response_analysis(response_stats)
    data_stats = response_stats.json()

    data_final = get_stats_from_jsons(data_nickname, data_stats)
    write_json(data_final)


def get_stats_from_jsons(data1, data2):
    data_new = {}

    nickname = data1['response']['players'][0]['personaname']
    kills = data2['playerstats']['stats'][0]['value']
    deaths = data2['playerstats']['stats'][1]['value']
    time_played = data2['playerstats']['stats'][2]['value']
    mvps = next((item for item in data2['playerstats']['stats'] if item["name"] == 'total_mvps'))['value']
    matches = next((item for item in data2['playerstats']['stats'] if item["name"] == 'total_matches_played'))['value']
    wins = next((item for item in data2['playerstats']['stats'] if item["name"] == 'total_matches_won'))['value']

    data_new['nickname'] = nickname
    data_new['kills'] = kills
    data_new['deaths'] = deaths
    data_new['K/D'] = kills / deaths
    data_new['hours_played'] = round(time_played / 3600, 3)
    data_new['mvps'] = mvps
    data_new['matches'] = matches
    data_new['wins'] = wins
    data_new['%'] = round(wins / matches * 100, 1)

    return data_new




