from pyscript import display, document

non_metals = {
        "H": ("Hydrogen", "H", 1, 1.008),
        "He": ("Helium", "He", 2, 4.0026),
        "C": ("Carbon", "C", 6, 12.011),
        "N": ("Nitrogen", "N", 7, 14.007),
        "O": ("Oxygen", "O", 8, 15.999),
        "F": ("Fluorine", "F", 9, 18.998),
        "Ne": ("Neon", "Ne", 10, 20.180),
        "P": ("Phosphorus", "P", 15, 30.974),
        "S": ("Sulfur", "S", 16, 32.06),
        "Cl": ("Chlorine", "Cl", 17, 35.45),
        "Ar": ("Argon", "Ar", 18, 39.948),
        "Se": ("Selenium", "Se", 34, 78.971),
        "Br": ("Bromine", "Br", 35, 79.904),
        "Kr": ("Krypton", "Kr", 36, 83.798),
        "I": ("Iodine", "I", 53, 126.90),
        "Xe": ("Xenon", "Xe", 54, 131.29),
        "R": ("Radon", "R", 86, 222)
    }

def display_non_metals():
        document.getElementById("output").innerHTML = ""
        for symbol, name in non_metals.items():
            document.getElementById("output").innerHTML += f"{symbol}: {name}<br>"

element1 = document.getElementById('element1').value.strip().title()

element_info = non_metals.get(element1,("Element not found","-","-"))
document.getElementById('result').innerHTML = f"""

<b>Element:</b> {element_info[0]} <br>
<b>Symbol:</b> {element_info[1]} <br>
<b>Atomic Number:</b> {element_info[2]} <br>
<b>Atomic Mass:</b> {element_info[3]} <br>
"""