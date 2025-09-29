import streamlit as st

st.title("Calculadora de materiales para ventanas")

st.write("Ingrese las dimensiones de la ventana en metros:")

ancho = st.number_input("Ancho de la ventana (m)", min_value=0.01, format="%.2f")
alto = st.number_input("Alto de la ventana (m)", min_value=0.01, format="%.2f")

if ancho and alto:
    area_vidrio = ancho * alto * 2  # doble lámina
    longitud_madera_m = (ancho + alto) * 2
    longitud_madera_pies = longitud_madera_m * 3.25

    st.success(f"Área de vidrio requerida: {area_vidrio:.2f} m²")
    st.success(f"Longitud de madera requerida: {longitud_madera_pies:.2f} pies")
else:
    st.info("Ingrese valores mayores a cero para ambas dimensiones.")
