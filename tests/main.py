import api

resp = api.clima()

print(resp[0],resp[1],resp[3][1]['date'],resp[3][1]['description'])