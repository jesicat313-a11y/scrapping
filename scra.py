from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

URL = "https://www.multitrabajos.com/listado-empresas"
driver.get(URL)

time.sleep(10)

# Scroll para cargar más
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

cards = driver.find_elements(By.XPATH, "//a[contains(., 'avisos activos')]")

print("Tarjetas encontradas:", len(cards))

data = []

for card in cards:
    texto = card.text.split("\n")
    
    empresa = texto[0]
    
    avisos = None
    actividad = None
    
    for t in texto:
        if "avisos activos" in t.lower():
            avisos = int(re.search(r"\d+", t).group())
        elif "empleados" not in t.lower() and "avisos" not in t.lower() and len(t) < 40 and t != empresa:
            actividad = t
    
    data.append({
        "Empresa": empresa,
        "AvisosActivos": avisos,
        "Actividad": actividad
    })

df = pd.DataFrame(data).drop_duplicates()
df.head(15)
print(df)