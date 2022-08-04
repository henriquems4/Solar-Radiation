import pandas as pd
lat = 0
lon = 0

with open('locais.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
    lines[i] = lines[i].split(",")

while True:
    nome_planta = input("Qual o Nome da Planta que pretende verificar?").lower()
    valor = 0
    for i in lines:
        if nome_planta == i[0]:
            lat = i[1]
            lon = i[2]
            valor = 1
            potencia_nominal = i[3]
    if valor == 1:
        break
    print('nenhum valore introduzido é válido')

start = input("Qual a data de inicio? (yyyymmdd) ")
end = input("Qual a data final? (yyyymmdd) ")
data = pd.read_csv('https://power.larc.nasa.gov/api/temporal/daily/point?parameters=RH2M,PRECTOTCORR&community=RE&longitude='+(str(lon))+'&latitude='+str(lat)+'&start='+str(start)+'&end='+str(end)+'&format=CSV',skiprows=10)
df = data[data.RH2M != -999.00]
print('A humidade média (%) é: ',df['RH2M'].mean())
print('A precipitação total é: ',df['PRECTOTCORR'].sum())
data2 = pd.read_csv('https://power.larc.nasa.gov/api/temporal/hourly/point?Time=LST&parameters=T2M,WS10M&community=RE&longitude='+str(lon)+'&latitude='+str(lat)+'&start='+str(start)+'&end='+str(end)+'&format=CSV',skiprows=10)
df2 = data2[data2.T2M != -999.00]
df2 = df2[df2.WS10M != -999.00]
print('O valor máximo de temperatura foi ',df2['T2M'].max())
print('O valor mínimo de temperatura foi ',df2['T2M'].min())
print('O valor máximo da velocidade do vento foi ',df2['WS10M'].max())
is_data = pd.read_csv('https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=RE&longitude='+str(lon)+'&latitude='+str(lat)+'&start='+str(start)+'&end='+str(end)+'&format=CSV',skiprows=9)
is_data = is_data[is_data.ALLSKY_SFC_SW_DWN != -999.00]
print(is_data['ALLSKY_SFC_SW_DWN'])
#print(is_data_isolar['Daily Yield(kWh)'].sum())
print("Radiação média: ",is_data['ALLSKY_SFC_SW_DWN'].mean())
print("Radiação total: ",is_data['ALLSKY_SFC_SW_DWN'].sum())
#print(is_data['ALLSKY_SFC_SW_DWN'].sum()/29)


