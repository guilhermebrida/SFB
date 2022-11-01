import serial
from tkinter import filedialog as dlg
import re
from pprint import pprint
from tkinter import * 
import asyncio
from time import sleep
import serial
import time
import codecs
import binascii





#abrir arquivo SFB
path = dlg.askopenfilename()
f = open(path,encoding='utf-8' ,errors='ignore')
conteudo = f.read()
# print(conteudo)

# converte SFB em hex e separa em 4bytes
conv = binascii.hexlify(conteudo.encode())
separarByte = re.findall('..',conv.decode())

# separar em 1040 caracteres hex q é 520 bytes
separar = re.findall(r'.{1040}',conv.decode())
print(separar)
print(len(separar[0]))
print(len(separarByte))


# bloco =[]
# for i in range(520):
#     bloco.append(separarByte[i])
# print(bloco)
# converter cabeçalho para hex
cabeçalho =  'BINAVSFB'
cabeçalhoHex = binascii.hexlify(cabeçalho.encode())
print(cabeçalhoHex)

# converter SN para hex
SN = '38L10071'
snHex = binascii.hexlify(SN.encode())
print(snHex)


print(len(separar))