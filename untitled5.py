# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sMP9IaOK-30ABmZ2UP3v21j_hGlnJl2T
"""

import pandas as pd
import requests
import streamlit as st

# Título de la aplicación
st.title('Aplicación Web: Datos desde una API REST')
# Verificar que la respuesta sea exitosa (código 200)
df= pd.read_csv('database_titanic.csv')
st.write(df.head())
# Selección de columnas y estadísticas
# Verificar si las columnas existen antes de operar sobre ellas
# Selección de columnas relevantes
    df['Nombre'] = df['name'].apply(lambda x: x.get('common') if isinstance(x, dict) else None)
    df['Región'] = df['region']
    df['Población'] = df['population']
    df['Área (km²)'] = df['area']
    df['Fronteras'] = df['borders'].apply(lambda x: len(x) if isinstance(x, list) else 0)
    df['Idiomas Oficiales'] = df['languages'].apply(lambda x: len(x) if isinstance(x, dict) else 0)
    df['Zonas Horarias'] = df['timezones'].apply(lambda x: len(x) if isinstance(x, list) else 0)

 
