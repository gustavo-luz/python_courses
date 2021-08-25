
"""
file=open('arquivo.txt','w')
file.write('Ola, como vc está?\n')
file.write('bem e vc?')
file.close
"""


#aula 17 

"""
#q3 c

N= int(input('quantos? '))
arq=open('num.txt','w')
arq.close()

for x in range(1,N+1):
    arq=open('num.txt','a')
    arq.write(str(x))
    arq.write('\n')
    arq.close



#e

N= int(input('quantos? '))
arq=open('num.txt','w')


for x in range(1,N):
    arq.write(str(x))
    arq.write('\n')
    arq.close


#q4 c

import csv
dado=[['1','maria','med'],['2','eric','eng']]
with open('person.csv','w') as arq:
    writer=csv.writer(arq,delimiter=';')
    writer.writerows(dado)



#q5 b
with open('reais.txt','w') as arq:
    num=3.4
    arq.write("{0:.3f}\n".format(num))
    num=2.1
    arq.write("{0:.1f}\n".format(num))
    num=4
    arq.write("{0:.5f}\n".format(num))
    num=1.3565
    arq.write("{0:.2f}\n".format(num))
    
  """

  #aula 18 q5 A
import csv
csvReader = csv.reader(open("arquivo.csv", 'wt'), delimiter='\t')
for linha in csvReader:
    print("COD" + linha[0] + " NOME: " + linha[2] + "QTDE: " + int(linha[3]))