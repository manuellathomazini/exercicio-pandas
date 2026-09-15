import pandas as pd
import numpy as np

dataset = r"C:\Users\manut\OneDrive\Desktop\exercicio-pandas\dataset_falhas_maquinas.xlsx"
df = pd.read_excel(dataset)

#1. Crie um filtro para selecionar apenas as máquinas do tipo M, depois do tipo H, depois do tipo L.

m_filter = df['Tipo'] == 'M'
h_filter = df['Tipo'] == 'H'
l_filter = df['Tipo'] == 'L'

#2. Crie um filtro para selecionar apenas as falhas do tipo Power Failure.

pf_filter = df['Tipo da Falha'] == 'Power Failure'

#3. Verifique quais máquinas aparecem quando há apenas falhas do tipo power failure.

pf_df = df[pf_filter]
print(pf_df)

#4. Qual a faixa de valores de temperatura do processo, torque e velocidade de rotação quando há apenas falhas do tipo power failure?

temp_min = pf_df['Temperatura Processo [K]'].min()
temp_max = pf_df['Temperatura Processo [K]'].max()

torq_min = pf_df['Torque [Nm]'].min()
torq_max = pf_df['Torque [Nm]'].max()

vr_min = pf_df['Velocidade Rotacao [rpm]'].min()
vr_max = pf_df['Velocidade Rotacao [rpm]'].max()

print(f'Temperatura Processo [K] (Power Failure): de {temp_min} a {temp_max}')
print(f'Torque [Nm] (Power Failure): de {torq_min} a {torq_max}')
print(f'Velocidade Rotacao [rpm] (Power Failure): de {vr_min} a {vr_max}')

#5. Se existem diferentes máquinas quando há falhas do tipo power failure, será que é correto verificar a faixa de valores de temperatura do processo, torque e velocidade de rotação sem separar o tipo de máquina?
#6. Mostre a curva de velocidade de rotação quando houver apenas falhas do tipo power failure.
#7. Mostre a curva de velocidade de rotação quando houver apenas falhas do tipo power failure, considerando o tipo de máquina.
#8. Quais insights foi possível observar?