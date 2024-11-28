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
# Verificar si las columnas existen antes de operar sobre ellas
if 'name' in df.columns:
    df['Nombre'] = df['name'].apply(lambda x: x.get('common') if isinstance(x, dict) else None)
else:
    df['Nombre'] = None

if 'region' in df.columns:
    df['Región'] = df['region']
else:
    df['Región'] = None

if 'population' in df.columns:
    df['Población'] = df['population']
else:
    df['Población'] = None

if 'area' in df.columns:
    df['Área (km²)'] = df['area']
else:
    df['Área (km²)'] = None

if 'borders' in df.columns:
    df['Fronteras'] = df['borders'].apply(lambda x: len(x) if isinstance(x, list) else 0)
else:
    df['Fronteras'] = 0

if 'languages' in df.columns:
    df['Idiomas Oficiales'] = df['languages'].apply(lambda x: len(x) if isinstance(x, dict) else 0)
else:
    df['Idiomas Oficiales'] = 0

if 'timezones' in df.columns:
    df['Zonas Horarias'] = df['timezones'].apply(lambda x: len(x) if isinstance(x, list) else 0)
else:
    df['Zonas Horarias'] = 0

 
