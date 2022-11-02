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

msg = 80000000

# criando bloco de envio
bloco =[]
bloco.append(cabeçalhoHex.decode()+separar[0]+snHex.decode()+str(msg))
bloco2 = re.findall('........',''.join(bloco))
print(bloco2,len(bloco2)*4)

# XOR a cada 4bytes
cs=0
for i in range(len(bloco2)):
    cs ^= int(bloco2[i],16)
print(cs,hex(cs))
hexcs = hex(cs).replace('0x','')
print(hexcs)
bloco2.append(hexcs)

final = 'C0'
bloco2.append(final)
print(bloco2)

for i in range(len(separar)):
    msg = msg + i
    bloco.append(cabeçalhoHex.decode()+separar[i]+snHex.decode()+str(msg))
    bloco2 = re.findall('........',''.join(bloco))
    for j in range(len(bloco2)):
        cs ^= int(bloco2[j],16)
    hexcs = hex(cs).replace('0x','')
    bloco2.append(hexcs)
    bloco2.append(final)
    print(f'bloco {i}: ',bloco2)

