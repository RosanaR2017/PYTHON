"""Crear archivos JSON desde Python para almacenar datos de ventas. Tener en cuenta información de una venta:

factura, cliente, información del cliente (opcional: nombre, teléfono, correo), vendedor, productos, precios de productos, cantidad de productos, total de la factura. """

import json 
from pprint import pprint
import uuid

class Factura():
    def __init__(self):
        self.factura=""
        self.client_name= None
        self.client_phone= None
        self.email= None
        self.seller=""
        self.prodprice={}  # diccionario que guarda productos y precios.
        self.prodquant={}  # diccionario que guarda productos y cantidades.
        self.total=0       #Total de la factura 
        
        #Las siguientes funciones son setter de mi clase factura.
        def factura(self,client_id):
            self.factura= factura
        def client_name(self,client_name):
            self.client_name=client_name
        def client_phone(self,client_phone):
            self.client_phone=client_phone
        def email(self,email):
            self.email=email
        def seller(self,seller):
            self.seller=seller
        def prodprice(self,prodprice):
            self.prodprice=prodprice
        def prodquant(self,prodquant):
            self.prodquant=prodquant
        def total(self,total):
            self.total=total
        

          
        
    def input_name():
        try:
            client_id=int(input("Please enter client's id:"))
            return client_id
        except:
            print("Invalid Id") 

    def seller():
        while True:
            try:
                seller=input("Enter seller's name: ")
                if seller.replace(" ", "").isalpha():
                    return seller          
            except:
                print("Invalid name, enter it again")


    def optional_info():
        try:
            client_name=input("Please enter client's name:")
            client_phone=int(input("Please enter client's phone number:"))
            email=input("Please enter client's e-mail: ")
            return client_name, client_phone, email
        except:
            client_name= None
            client_phone= None
            email= None
            return client_name, client_phone, email

    def prodprice():
        #list=
        try:
            prodprice=input("Enter the product followed by a space and its price:\n").split(" ")
            print(*prodprice)
        except:
            print("Product's input error.")
    
    def jsonex():

        {"factura":"U123344550",
          "cliente":"Rosana R"

        }
        

def main():
    factura=uuid.uuid4()
    print(factura)  #Print the invoice id.
    client_id=Factura.input_name()
    client_name, client_phone, email =Factura.optional_info()
    print("client name: {} , client phone: {}, email: {} ".format(client_name, client_phone, email))
    seller=Factura.seller()
    print("Seller's name :", seller)
    Factura.prodprice()


if __name__== "__main__" :
    main()