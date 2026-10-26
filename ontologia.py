hechos = {
    "perro": {
        "animal", "pelo", "cuatroPatas", "amigable", "domestico",
        "leche" 
    },
    "vaca": {
        "animal", "pelo", "leche", "cuatroPatas", "pezuñas",
        "cuerpoRobusto", "pasto", "domestico"
    },
}

# reglas como tuplas

reglas = [
    (("pelo",), "mamifero"),
    (("leche",), "mamifero"),
    (("plumas",), "ave"),
    (("vuela", "huevos"), "ave"),
    (("mamifero", "carne"), "carnivoro"),
    (("mamifero", "pezuñas"), "ungulado"),
    (("carnivoro", "leonado", "manchasOscuras"), "guepardo"),
    (("carnivoro", "leonado", "manchasNegras"), "tigre"),
    (("ungulado", "cuelloLargo", "manchasOscuras"), "jirafa"),
    (("ungulado", "rayasNegras"), "cebra"),
    (("ave", "nada", "blancoNegro"), "pinguino"),
    (("ave", "vuelaMuyBien"), "albatros"),
    (("pelo", "cuatroPatas", "amigable"), "puedeSerPerro"),
    (("amigable", "domestico", "pelo", "cuatroPatas"), "perro"),
    (("pelo", "leche"), "mamifero"),
    (("mamifero", "pezuñas", "cuerpoRobusto"), "puedeSerVaca"),
    (("cuatroPatas", "pezuñas", "pasto"), "puedeSerVaca"),
]

# relaciones
relaciones = [
    ("perro", "es_un", "animal"),
    ("vaca", "es_un", "animal"),
    ("mamifero", "subclase_de", "animal"),
    ("ave", "subclase_de", "animal"),
    ("carnivoro", "subclase_de", "mamifero"),
    ("ungulado", "subclase_de", "mamifero"),
    ("perro", "tiene_propiedad", "pelo"),
    ("perro", "tiene_propiedad", "cuatroPatas"),
    ("perro", "tiene_propiedad", "amigable"),
    ("perro", "tiene_propiedad", "domestico"),
    ("vaca", "tiene_propiedad", "pelo"),
    ("vaca", "tiene_propiedad", "leche"),
    ("vaca", "tiene_propiedad", "pezuñas"),
    ("vaca", "tiene_propiedad", "cuerpoRobusto"),
    ("vaca", "se_alimenta_de", "pasto"),
]

def inferir(propiedades, reglas_aplicables):
    """Aplica encadenamiento hacia adelante hasta que no haya nuevas conclusiones."""
    conocidas = set(propiedades)
    cambio = True
    while cambio:
        cambio = False
        for premisas, conclusion in reglas_aplicables:
            if set(premisas).issubset(conocidas) and conclusion not in conocidas:
                conocidas.add(conclusion)
                cambio = True
    return conocidas

def mostrar_resultados():
    print("=== Ontología de animales ===")
    for nombre, propiedades in hechos.items():
        inferidas = inferir(propiedades, reglas)
        print(f"\\n{nombre.capitalize()}:")
        print("  Hechos iniciales:", ", ".join(sorted(propiedades)))
        print("  Propiedades inferidas:", ", ".join(sorted(inferidas)))
    print("\\n=== Relaciones ===")
    for origen, relacion, destino in relaciones:
        print(f"{origen} --{relacion}--> {destino}")

if __name__ == "__main__":
    mostrar_resultados()