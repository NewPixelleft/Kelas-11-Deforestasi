import pandas as pd
import plotly.express as px

# membaca file csv 
dat_deforestasi = pd.read_csv('data_deforestasi.csv')

# membuat global array tahun
tahun = [col for col in dat_deforestasi.columns if col.isnumeric()]
print(tahun)

dat_temp = dat_deforestasi.iloc[0]

for baris in range (0, len(dat_deforestasi)):
    data_temp = dat_deforestasi.iloc[baris]
    nilai = [data_temp[i] for i in tahun]
    judul = "Deforestasi Netto Provinsi " + data_temp['Provinsi']

    if baris == len(dat_deforestasi) - 1:
        judul = "Deforestasi Netto " + data_temp['Provinsi']

    diagram = px.bar(x = tahun, y = nilai, labels = {'x': 'Tahun', 'y' : 'Deforestasi (Ha)'}, title = judul)

    diagram.update_layout(
        title = dict(font=dict(family="Georgia", size=22, color="black"), x = .5, xanchor = 'center'),
        font = dict(family="Arial, sans-serif", size=14, color="black"),
        legend = dict(font=dict(family="Courier New", size=12, color="navy"))
    )
    diagram.update_layout(
        plot_bgcolor='white',    
        paper_bgcolor='white',   
    )

    diagram.update_xaxes(
        showgrid=True,
        gridcolor='lightgrey',
        gridwidth=1,
        zeroline=False
    )

    diagram.update_yaxes(
        showgrid=True,
        gridcolor='lightgrey',
        gridwidth=1,
        zeroline=False
    )

    diagram.write_image("diagrams/svg/" + str(baris) +"_"+ data_temp['Provinsi'] + ".svg")
    diagram.write_image("diagrams/png/" + str(baris) +"_"+ data_temp['Provinsi'] + ".png")
