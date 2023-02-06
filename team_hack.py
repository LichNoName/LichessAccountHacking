import berserk
import ndjson
import requests


def hack(team, token):
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)

    r = requests.get("https://lichess.org/api/team/" + team + "/users")
    data = r.json(cls=ndjson.Decoder)
    for i in data:
        user = i['id']
        client.team.kick_member(team, user)
        print(f"{user} был кикнут...")
