universo = {
   
    "estudiantes": {
        "Pedro": {
            "Grupo": "A",
            "Carrera": "Sistemas",
            "Inscrito": ["Calculo"],
            "Imparte": []
        },
        "Pablo": {
            "Grupo": "B",
            "Carrera": "Administracion",
            "Inscrito": ["Algebra"],
            "Imparte": []
        },
        "Luis": {
            "Grupo": "C",
            "Carrera": "Contabilidad",
            "Inscrito": ["Base_Datos"],
            "Imparte": []
        },
        "Gisell": {
            "Grupo": "E",
            "Carrera": "Sistemas",
            "Inscrito": ["Programacion"],
            "Imparte": []
        },
        "Ana": {
            "Grupo": "F",
            "Carrera": "Sistemas",
            "Inscrito": ["Redes"],
            "Imparte": []
        },
        "Carla": {
            "Grupo": "A",
            "Carrera": "Administracion",
            "Inscrito": [],
            "Imparte": []
        },
        "Sofia": {
            "Grupo": "B",
            "Carrera": "Sistemas",
            "Inscrito": [],
            "Imparte": []
        }
    },
   
    "docentes": {
        "Martinez": {"Imparte": ["Calculo"]},
        "Gonzales": {"Imparte": ["Algebra"]},
        "Bautista": {"Imparte": ["Base_Datos"]},
        "Flores": {"Imparte": ["Programacion"]},
        "Lopez": {"Imparte": ["Calculo"]},
        "Garcia": {"Imparte": ["Redes"]}
    },
    
    "asignaturas": {
        "Calculo": {"Aula": "207"},
        "Programacion": {"Aula": "208"},
        "Base_Datos": {"Aula": "601"},
        "Redes": {"Aula": "208"},
        "Algebra": {"Aula": "207"}
    },
    
    "carreras": ["Sistemas", "Administracion", "Contabilidad", "Industrial"],
    "grupos": ["A", "B", "C", "E", "F"],
    "aulas": ["207", "208", "601"]
}



# ¿x es un estudiante registrado?
def EsEstudiante(x):
    for estudiante, datos in universo["estudiantes"].items():  
        if estudiante == x:
            return True   
    return False          

# ¿x es un profesor registrado?
def EsProfesor(x):
    for docente, datos in universo["docentes"].items():
        if docente == x:
            return True   
    return False          

# ¿x es una materia registrada?
def EsMateria(x):
    for asignatura in universo["asignaturas"].keys():
        if asignatura == x:
            return True  
    return False        

# ¿x es una carrera registrada?
def EsCarrera(x):
    for carrera in universo["carreras"]:
        if carrera == x:
            return True   
    return False         

#  ¿El alumno x está inscrito en la materia y?
def Inscrito(x, y):
    for estudiante, datos in universo["estudiantes"].items():
        if estudiante == x:
            if y in datos["Inscrito"]:  
                return True
    return False

# ¿El profesor x imparte la materia y?
def Imparte(x, y):
    for docente, datos in universo["docentes"].items():
        if docente == x:
            if y in datos["Imparte"]:  
                return True
    return False

# ¿El estudiante x pertenece a la carrera y?
def Pertenece(x, y):
    for estudiante, datos in universo["estudiantes"].items():
        if estudiante == x:
            if datos["Carrera"] == y: 
                return True
    return False


print("--- PRUEBAS DE CONSULTAS V/F ---")


print("1. ¿Ana es estudiante?:", EsEstudiante("Ana"))
print("2. ¿Martínez es estudiante?:", EsEstudiante("Martinez"))


print("3. ¿López es profesor?:", EsProfesor("Lopez"))
print("4. ¿Carla es profesora?:", EsProfesor("Carla"))


print("5. ¿Programación es una materia?:", EsMateria("Programacion"))
print("6. ¿Sistemas es una materia?:", EsMateria("Sistemas"))


print("7. ¿Industrial es una carrera?:", EsCarrera("Industrial"))
print("8. ¿Redes es una carrera?:", EsCarrera("Redes"))


print("9. ¿Luis está inscrito en Base de Datos?:", Inscrito("Luis", "Base_Datos"))
print("10. ¿Luis está inscrito en Álgebra?:", Inscrito("Luis", "Algebra"))


print("11. ¿García imparte Redes?:", Imparte("Garcia", "Redes"))
print("12. ¿García imparte Cálculo?:", Imparte("Garcia", "Calculo"))


print("13. ¿Sofía pertenece a Sistemas?:", Pertenece("Sofia", "Sistemas"))
print("14. ¿Sofía pertenece a Industrial?:", Pertenece("Sofia", "Industrial"))