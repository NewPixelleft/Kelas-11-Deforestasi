import pandas as pd
import numpy as np
from scipy.stats import linregress
import plotly.express as px
import plotly.graph_objects as go

tahun = list(i for i in range (2013, 2022))
value = [397370.9,1092181.5,629176.9,480010.8,439439.1,462458.5,115459.8,120705.8,236165.6]

slope, intercept, r_value, p_value, std_err = linregress(tahun, value)
tahun_deforestasi_nol = -intercept / slope
extended_years = np.append(tahun, np.linspace(tahun[-1]+1, tahun_deforestasi_nol, 100))
nilai_regresi = slope * extended_years + intercept

df = pd.DataFrame({'Tahun': tahun, 'Nilai': value})
reg_df = pd.DataFrame({'Year': extended_years, 'Value': nilai_regresi})

dia = px.scatter(df, x='Tahun', y='Nilai', title='Prediksi Deforestasi di Indonesia',
                 labels={'Value' : 'Tahun', 'y':'Deforestasi (Ha)'})

dia.add_scatter(x=reg_df['Year'], y=reg_df['Value'], 
            mode='lines', name='garis\nregresi')

dia.add_trace(go.Scatter( x=[tahun_deforestasi_nol], y=[0], mode='markers+text', name='Hits 0', text=f"{tahun_deforestasi_nol: .2f}" , textposition='top center', marker=dict(size=10, color='red', symbol='x')
))

dia.update_layout(
        title = dict(font=dict(family="Georgia", size=22, color="black"), x = .5, xanchor = 'center'),
        font = dict(family="Arial, sans-serif", size=14, color="black"),
        legend = dict(font=dict(family="Courier New", size=12, color="navy"))
    )

dia.write_image("prediksi.svg")
dia.write_image("prediksi.png")

print ("slope: ", slope)
print ("r_value: ", r_value)
print ("intercept: ", intercept)
print ("tahun_deforestasi_nol: ", tahun_deforestasi_nol)
# dia.show()