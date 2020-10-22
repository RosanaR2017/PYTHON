import json 
import requests
from pprint import pprint 

def get_address(pendientes):    #PENDIENTE EN PROCESO ***ME TOCO PASARLO A LISTA PORQUE SUPUESTAMENTE EN DICCIONARIOS NO SE PUEDE ITERAR.
  try:
    llaves = list(pendientes.keys())
    print(llaves[3]+":",pendientes["age"])
  except:
    print("Problemas en la función get_address")
    
    
def iteraccion(pendientes):   
    for keys in pendientes.keys(): 
      if keys =="age" : print(keys, ":", pendientes["age"])

def print_completeAddress(pendientes):
    for k,v in pendientes["address"].items():
        print(k,":",v)

def main():
    try:
        input= "https://tools.learningcontainer.com/sample-json.json"
        response=requests.get(input)
        pendientes = json.loads(response.text)
        get_address(pendientes)
    except:
        pprint("Problemas de cargue de JSON")

if __name__== "__main__" :
    main()