#!/usr/bin/env python
# coding: utf-8

# PROYECTO SQL

# In[1]:


import pandas as pd
import sqlite3


# In[12]:


datos_muertes = pd.read_excel(r'directorio.xlsx')
datos_vacunacion = pd.read_excel(r'directorio.xlsx')
conexion = sqlite3.connect(r'directorio\Covid.db')

datos_muertes.to_sql('Muertes',conexion, if_exists='replace',index=False)
datos_vacunacion.to_sql('Vacunacion',conexion, if_exists='replace',index=False)


# In[ ]:





# In[ ]:




