
#DESCARGA VIDEOS DE YOUTUBE

from pytube import YouTube
print("------------------------------------")
print(" DESCARGA VIDEOS DE YOUTUBE")
print("------------------------------------" +"\n")



usuario= input("Ingrese la URL: ")
print("-------------------------------------")
print(" OBTENIENDO INFORMACIÓN DEL VIDEO")
print("-------------------------------------"+"\n")
dsc = YouTube(usuario)



print("-------------------------------------")
print(" ESPERE MIENTRAS SE DESCARGA")
print("-------------------------------------"+"\n")

dsc.streams.first().download(r"/data/data/com.termux/files/home/storage/downloads")

print("-------------------------------------")
print(" RUTA DEL VIDEO:STORAGE/DOWNLOADS")
print("-------------------------------------")
#dsc.streams.first().download()

#JavierHack
