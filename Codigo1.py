import datetime
import sys
import pandas as pd
import csv
import os

menu=1
separador=("*"*30)
contador=1
diccionario_ventas={}
try:
    while menu==1:
        print(separador+"Bienvenidos a SEPHORA" +separador)
        print("1=Registrar una Venta\n2=Consultar ventas de un día específico\n3=Salir")
        opcion=int(input("¿Que opcion desea llevar acabo? : "))
        listasumaprecio=[]
        
        if opcion==1:
            ciclo=1
            print(separador+"Registrador de ventas"+separador)
            while ciclo==1:
                listadescript=[]
                listacantidadt=[]
                listapreciot=[]
                listatiempot=[]
                
                print(f"VENTA {contador}")
                
                descripcion=input("¿Cual la descripcion del articulo? : ")
                listadescript.append(descripcion)
                
                cantidad=int(input("Cantidad de piezas vendidas : "))
                listacantidadt.append(cantidad)
                
                precio=float(input("Precio de venta unitario del articulo : "))
                listasumaprecio.append(precio*cantidad)
                listapreciot.append(precio)
            
                ahora = datetime.datetime.now()
                ahora1=ahora.strftime('%d/%m/%Y')
                listatiempot.append(str(ahora1))
                
                diccionario_ventas["Descripcion"]=listadescript
                diccionario_ventas["Piezas"]=listacantidadt
                diccionario_ventas["Precio"]=listapreciot
                diccionario_ventas["Tiempo"]=listatiempot
                diccionario2=pd.DataFrame(diccionario_ventas)
              
                ruta = "ventas.csv"
                diccionario2.to_csv(ruta, index=None, mode="a", header=not os.path.isfile(ruta))
            
                contador=contador+1            
                print(separador)
                print("Ingresar el numero 1 si deseas seguir registrando ventas\nIngresar el numero 0 si deseas salir del registrador de ventas")
                ciclo=int(input(":"))
                print(separador)
                print("")
                
            
            print(separador)
            print(f"Este es el monto total a pagar : {sum(listasumaprecio)}")
            print(separador)
            

            
            
            
        elif opcion==2:
            try: 
                diccionario3={}
                listadescrip2=[]
                listacantidad2=[]
                listaprecio2=[]
                listatiempo2=[]
                contador=1
                contador1=0
                contador2=0
                print(separador+"Bienvenido al consultador de ventas"+separador)
                print("-"*20)
                dia=(input("Dia en el se que se registro la venta : "))
                mes=input("Mes en el se que registro la venta : ")
                año=input("Año en el se que registro la venta : ")
                
                if len(mes)==1:
                    mes=("0"+ mes)
                    
                if len(dia)==1:
                    dia2=("0"+dia+"/")
                    fecha=(dia2+mes+"/"+año)
                else:
                    fecha=(dia+"/"+mes+"/"+año)
                print("")
                
                
                
                with open ('ventas.csv') as file:
                    reader=csv.reader(file)
                    for registro in reader:
                        contador1=contador1+1
                        if registro[-1]==fecha:
                            
                            listadescrip2.append(registro[0])
                            listacantidad2.append(registro[1])
                            listaprecio2.append(registro[2])
                            listatiempo2.append(registro[3])
                                                        
                        
                            contador=contador+1
                        
                        elif registro[-1]!=fecha:
                            contador2=contador2+1
                    
                    if contador2==contador1:
                        print(f"No hay registros de ventas con la fecha proporcionada:( {fecha} ")
                try:
                    diccionario3["Descripcion del articulo"]=listadescrip2
                    diccionario3["Cantidades"]=listacantidad2
                    diccionario3["Precio del articulo"]=listaprecio2
                    diccionario3["Fecha de compra"]=listatiempo2
                    dataframe=pd.DataFrame(diccionario3)
                    print(dataframe)
                except:
                    print("No se han registrado ventas")

            except:
                print("No se han registrado ventas")
        
        
        elif opcion==3:
            break
        
                    
except:
    print(f"Ocurrió un problema {sys.exc_info()[0]}")

finally:
    print("FIN DEL CODIGO")