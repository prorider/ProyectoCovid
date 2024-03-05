#!/usr/bin/env python
# coding: utf-8

# PROYECTO SQL

# In[1]:


import pandas as pd
import sqlite3


# In[12]:


datos_muertes = pd.read_excel(r'C:\Users\poNze\OneDrive\Documentos\Proyecto SQl covid\CovidDeaths.xlsx')
datos_vacunacion = pd.read_excel(r'C:\Users\poNze\OneDrive\Documentos\Proyecto SQl covid\Covidvacunacion.xlsx')
conexion = sqlite3.connect(r'C:\Users\poNze\OneDrive\Documentos\Proyecto SQl covid\Covid.db')

datos_muertes.to_sql('Muertes',conexion, if_exists='replace',index=False)
datos_vacunacion.to_sql('Vacunacion',conexion, if_exists='replace',index=False)


# In[ ]:





# In[ ]:




