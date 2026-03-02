Web Scraping – Multitrabajos

Este proyecto tiene como objetivo extraer información estructurada desde la página pública de Multitrabajos Ecuador, específicamente del listado de empresas que publican ofertas laborales.
Debido a que la página está construida con tecnología JavaScript, el contenido no puede ser extraído mediante métodos tradicionales como requests y BeautifulSoup. Por esta razón, se implementó Selenium para simular un navegador real y capturar el contenido dinámico renderizado.
Librerías Utilizadas
- Selenium:Permite simular un navegador real para renderizar contenido dinámico generado por JavaScript.
- re (Expresiones Regulares):Utilizada para identificar patrones dentro del texto y extraer valores numéricos como:
  - Número de avisos activos
  - Rango de empleados
-  time:Se emplea para controlar los tiempos de espera y asegurar que la página cargue completamente antes de extraer información.
-  pandas: Permite estructurar los datos en un DataFrame, limpiar la información y procesarla para análisis posterior.
-  matplotlib:Se utiliza para generar visualizaciones gráficas de los datos obtenidos.

Proceso de extracción 
- Se construyó un navegador automatizado con Selenium.
- Se definió la URL base y el número de páginas a recorrer (10).
- Para cada página:
  - Se esperó la carga completa del contenido dinámico.
  - Se realizó desplazamiento (scroll) para asegurar la carga total de las tarjetas.
  - Se identificaron las tarjetas que contenían el texto “avisos activos”.
  - Se dividió el contenido de cada tarjeta en líneas de texto.
  - Mediante expresiones regulares (re) se extrajeron los valores numéricos.
  - Se almacenó la información en una lista de diccionarios.
  - Finalmente, se creó un DataFrame estructurado con todos los datos obtenidos.

Campos extraídos
- De cada empresa se obtuvieron los siguientes datos:
- Empresa → Nombre de la organización.
- AvisosActivos → Número de vacantes disponibles.
- Provincia → Ubicación geográfica.
- Empleados → Rango de empleados reportado.

Limpieza y Normalización
Para garantizar calidad en los datos se realizó:
- Eliminación de espacios innecesarios.
- Conversión de valores numéricos.
- Separación del rango de empleados en valores mínimos y máximos.
- Reemplazo de valores nulos:
- Empleados → 0
- Eliminación de registros duplicados.

Se generaron dos archivos:
-  multitrabajos_empresas.csv (datos originales)
-  multitrabajos_empresas_clean.csv (datos procesados)

Visualización

A partir de los datos limpios se generaron:
- Top 10 provincias con mayor cantidad de empleos disponibles.
- Top 10 empresas con mayor número de avisos activos.
