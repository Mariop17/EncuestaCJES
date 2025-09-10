
import pandas as pd
import streamlit as st
import webbrowser

# Cargar datos desde el archivo Excel
df = pd.read_excel("Links Encuesta 2025 - El Salvador.xlsx", sheet_name="Consolidado", engine="openpyxl")

# Crear la aplicación web
st.set_page_config(page_title="Encuesta Creciendo Juntos 2025", layout="centered")
st.title("Encuestas El Salvador 2025")
st.write("Ingrese el código del empleado para ver su información y acceder a la encuesta.")

# Entrada del código
codigo = st.text_input("Código del empleado")

# Buscar y mostrar resultados
if codigo:
    resultado = df[df['Código'].astype(str) == codigo]
    if not resultado.empty:
        nombre = resultado.iloc[0]['Nombres']
        apellido = resultado.iloc[0]['Apellidos']
        link = resultado.iloc[0]['Link de Encuesta']

        st.success("Empleado encontrado:")
        st.write(f"**Nombres:** {nombre}")
        st.write(f"**Apellidos:** {apellido}")
        st.text_area("Link de Encuesta", value=link, height=100)

        # Botón para abrir el link
        if st.button("Abrir Encuesta en el Navegador"):
            webbrowser.open_new_tab(link)
    else:
        st.error("Código no encontrado. Verifique e intente nuevamente.")

# Instrucciones para compartir
st.markdown("---")
st.markdown("### ¿Cómo compartir esta app?")
st.markdown("Puedes subir este archivo y el Excel a [Streamlit Cloud](https://streamlit.io/cloud) para que otros puedan acceder desde cualquier navegador.")
