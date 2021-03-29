#make a POST request
import requests
import pandas as pd
dictToSend = {
    'ATTN':0,
    'IMPULSV-1':0,
    'MEMORY':1,
    'DEMEN-1':2,
    'SCHIZO-1':1,
    'DEMEN-2':1,
    'SUBSTANS-1':0,
    'SUBSTANS-2':0,
    'SUBSTANS-3':0,
    'SCHIZO-2':2,
    'BIPOLAR-1':2,
    'BIPOLAR-2':0,
    'DEPR-1':1,
    'PA':2,
    'FEAR':0,
    'ANX':2,
    'PTSD':1, 
    'DETACH':1, 
    'PTSD-2':True,
    'BLANK':1,
    'APPEAR FEAR':2, 
    'FACITIOUS':1,
    'MULTI PERSON':2,
    'SLEEP DISORDR':2, 
    'NARCOLEP':1,
    'SLEEP PARAL-1':1,
    'SLEEP PARAL-2':2,
    'SNORE':1,
    'SLEEP WALK':2,
    'PYRO':2,
    'HAIR LSS':0,
    'GAMBLE':2, 
    'STEAL':0,
    'IMPULSV-2':0,
    'SUICIDE':0,
    'ALONE':2, 
    'NARCISSISTIC':0,
    'COLD': 2,
    'DEPENDENT':0,
    'DEPENDENT-2':2,
    'PARANOID':0,
    'ECCENTRIC':2,
    'OCD':2,
    'ANTISOCIAL-1':2,
    'ANTISOCIAL-2':0,
    'LYING':2,
    'SCHIZOAFFECT':2,
    'DEMEN-3':0,
    'PTSD-1':2,
    'Patient': "A150"
}

# new_x = pd.DataFrame.from_dict(dictToSend, orient = "index").transpose()

# print(new_x.head())

res = requests.post('http://127.0.0.1:5000/v1/predict', json=dictToSend)
#dictFromServer = res.json()
print(res.json())