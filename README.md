
# Construcción de Ventanas

Este proyecto resuelve el problema de cálculo de materiales para la fabricación de ventanas, basado en el ejercicio del libro "CSharp Yellow Book" de Rob Miles.

## Descripción del problema
El fabricante de ventanas necesita calcular la cantidad de materiales requeridos para fabricar una ventana, ingresando el ancho y el alto en metros. El sistema debe mostrar:

- Área total de vidrio requerido (doble lámina, en metros cuadrados)
- Longitud de madera necesaria para el marco (en pies)

Las fórmulas utilizadas son:
- **Área de vidrio** = ancho × alto × 2
- **Longitud de madera** = (ancho + alto) × 2 × 3.25 (pies)

## Ejemplo
Para una ventana de 2 metros de alto y 1 metro de ancho:
- Área de vidrio: 4 m²
- Longitud de madera: 19.5 pies

## Uso de la aplicación
La solución está implementada como una aplicación web con Streamlit.

### Requisitos
- Python 3.8+
- Streamlit

### Instalación de dependencias
```bash
pip install streamlit
```

### Ejecución
```bash
streamlit run app.py
```

Esto abrirá una interfaz web donde puedes ingresar las dimensiones de la ventana y ver los resultados de manera interactiva.

## Autor
Solución generada por GitHub Copilot.
