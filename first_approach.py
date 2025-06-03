import requests
import os
from dotenv import load_dotenv
import time
start_time = time.time()
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8080/fragment?id=')
ok_code=True
next_fragment = 1
my_dict={}
while ok_code:
    x = requests.get(BASE_URL + str(next_fragment))    
    data=x.json()    
    if x.ok:
        print(f"Fragmento {next_fragment}: {data} , response {x.status_code}")
        my_dict[data["index"]] = data["text"]
    else:
        ok_code = False
        print(f"Error al obtener el fragmento {next_fragment}: {data}")
dict_ordenado=dict(sorted(my_dict.items()))

print(" ".join(dict_ordenado.values()))
end_time = time.time()   
print(f"Tiempo total: {end_time - start_time} segundos") 
