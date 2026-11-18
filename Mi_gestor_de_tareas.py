"""
mi_gestor_tareas.py
Proyecto integrador - Gestor de tareas pendientes (To-Do List)

Sustento teorico:
- Trejos Buritica, O. I. (2023a). Cap. 11: Funciones, pp. 369-420.
  Funciones con / sin parametros y con / sin retorno.
- Trejos Buritica, O. I. (2023b). cap. 12: Consejos y reflexiones
  sobre programacion, app. 423-440. Buenas practicas y claridad.
-Python Sofware Foundation. The Python Tutorial: defining functions
 y Modules. Documentacion oficial de Python.
- Van Rossum, G. et al. PEP 257 - Docstring Convetions.
"""

# ------------------------------------------------------------------------------------------
#1. FUNCION SIN PARAMETROS Y CON RETORNO
# ------------------------------------------------------------------------------------------
def obtener_tareas():
    """
    Inicializar y retomar una lista de ejemplo con tareas
    
    Returns:
        list[dict]: Lista de diccionarios. Cada tarea tiene:
            - "descripcion" (str): texto de la tarea.
            - "completada" (bool): True si esta completada, False si esta pendientes
            """
    return [
        {"descripcion": "Elaborar el informe del proyecto integrador", "completada": False},
        {"descripcion": "Revisar los requerimientos con el equipo del proyecto", "completada": True},
        {"descripcion": "Prepaparar la presentacion final del proyecto", "completada": False},
    ]


# -----------------------------------------------------------------------------------------
# 2. FUNCION CON PARAMETROS Y SIN RETORNO
# ------------------------------------------------------------------------------------------
def mostrar_tareas(lista_tareas):
    """
    Mostrar en pantalla la lista de tareas, numeradas.
    
    Args:
        lista_tareas (list[dict]): Lista de tareas a mostrar.
            Cada tarea es un diccionario con "descripcion" y "completada".
            
    Returns:
        None: Solo imprime en pantalla, no retorna valor.
    """
    if not lista_tareas:
        print("\n No ha tareasregistradas.")
        return

    print("\n--- LISTA DE TAREAS---")
    for i, tarea in enumerate(lista_tareas, start=1):
        marca = "[X]" if tarea["completada"] else "[]"
    print(f"{i}. {marca} {tarea['descripcion']}")


# ------------------------------------------------------------------------------------------
# 2b. FUNCION CON PARAMETROS Y SIN RETORNO - SOLO PENDIENTES
# -------------------------------------------------------------------------------------------
def mostrar_tareas_pendientes(lista_tareas):
    """
    Mostrar en pantalla solo las tareas que estan pendientes.
    
    Args:
        lista_tareas (list[dict]): Lista de tareas a filtrar.
        
    Returns:
        None: Solo imprime en pantalla, no retorna valor.
    """
    pendientes = [t for t in lista_tareas if not t["completada"]]
    if not pendientes:
        print("\nNo tienes tareas pendientes. ¡Todo al dia!")
        return

    print("\n--- SOLO TAREAS PENDIENTES---")
    for i, tarea in enumerate(pendientes, start=1):
        print(f"{i}.[] {tarea['descripcion']}")
    print(f"\nTe falta {len(pendientes)} tarea(s) por hacer.")
# --------------------------------------------------------------------------------------------------------------------------
# 3. FUNCION CON PARAMETROS Y CON RETORNO
# --------------------------------------------------------------------------------------------------------------------------
def agregar_tarea(lista_tareas, descripcion):
    """
    agregar una nueva tarea pendiente a la lista.
    
    Args:
        lista_tareas (list[dict]): Lista donde se agregara la tarea.
        descripcion (str): Descripcion de la nueva tarea.
        
    Returns:
        list[dict]: La lista de tareas modificada, con la nueva tarea
            agragada como {"descrpcion": descripcion, "completada": false}.
    """
    descripcion = descripcion.strip()
    if not descripcion:
        print("La descripcion no puede estar vacia.")
        return lista_tareas
    nueva_tarea = {"descripcion": descripcion, "completada": False}
    lista_tareas.append(nueva_tarea)
    print(f"Tarea agregada: '{descripcion}'")
    return lista_tareas


# ------------------------------------------------------------------------------------------------------------------------
# 4. FUNCION CON PARAMETROS Y SIN RETORNO + MANEJO DE ERRORES
# -------------------------------------------------------------------------------------------------------------------------
def marcar_completada(lista_tareas, posicion):
    """
    Marcar como completada la tarea ubicada en una posicion dada.
    
    Args:
        lista_tareas (list[dict]): Lista de tareas a modificar.
        posicion (int): Numero de posicion que ve el usuario (empieza en 1).
        
    Returns:
        None: Modifica la lista original, no retorma valor.
    """
    try:
        # El usuario ve posiciones desde 1; en Python los indices vas desde 0.
        indice = posicion - 1
        if indice < 0:
            raise IndexError("Posicion menor 1.")
        tarea = lista_tareas[indice]
        if tarea["completada"]:
            print("Esa tarea ya estaba marcada como completada.")
        else:
            tarea["completada"] = True
            print(f"tarea '{tarea['descripcion']}' marca como completada.")
    except IndexError:
        print("Error: la posicion ingresada no existe. Verifica el numero de la tarea.")
    except TypeError:
        print("Error: la posicion debe ser un numero entero.")


# -----------------------------------------------------------------------------------------------------------------------
# 5. FUNCION RECURSIVA CON PARAMETROS Y CON RETORNO
# -----------------------------------------------------------------------------------------------------------------------
def contar_tareas_pendientes(lista_tareas, indice=0):
    """
    Contar de forma recursiva cuantas tareas estan pendientes.
    
    Args:
        lista_tareas (list[dict]): Lista de tareas a recorrer.
        indice (int): Indice actual desde donde se sigue contando. Inicia en 0.
        
    Returns:
        int: Numero total de tareas con "completada" en False.
    """
    # CASO BASE: si el indice llego al final de la lista, ya no hay nada que contar.
    if indice == len(lista_tareas):
        return 0

    # CASO RECURSIVO: se revisa la tarea actual y se resuelve el resto
    # del problema llamado a la misma funcion con indice + 1.
    if not lista_tareas[indice]["completada"]:
        # Tarea pendiente: 1 + lo que falte por contar en el resto de la lista.
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)
    # Tarea completada: 0 + lo que le falte por contar en el resto de la lista.
    return contar_tareas_pendientes(lista_tareas, indice + 1)


# -------------------------------------------------------------------------------------------------------------------------
# FLUJO PRINCIPAL - MENU DE CONSOLA
# -------------------------------------------------------------------------------------------------------------------------
def main():
    """Ejecutar el menu principal del gestor de tareas."""
    lista_tareas = obtener_tareas()

    while True:
        print("\===== GESTOR DE TAREAS =====")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Mostrar total de tareas pendientes")
        print("5. salir")
        opcion = input("Elige una opcion (1-5):").strip()

        if opcion == "1":
            mostrar_tareas(lista_tareas)

        elif opcion == "2":
            descripcion = input("Escribe la descripcion de la nueva tarea:")
            lista_tareas = agregar_tarea(lista_tareas, descripcion)

        elif opcion == "3":
            mostrar_tareas(lista_tareas)
            try:
                posicion = int(input("Escribe el numero de la tarea a marcar: "))
                marcar_completada(lista_tareas, posicion)
            except ValueError:
                print("Error: debes ingresar un numero entero.")

        elif opcion == "4":
            total = contar_tareas_pendientes(lista_tareas)
            print(f"\nTotal de tareas pendientes: {total}")

        elif opcion == "5":
            print("Gracias por usar el gestor de tareas. Hasta pronto!")
            break

        else:
            print("Opcion no valida. Elige un numero del 1 al 5")


if __name__ == "__main__":
    main()