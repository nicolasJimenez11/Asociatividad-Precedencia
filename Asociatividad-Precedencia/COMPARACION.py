from lark import Lark
from lark.tree import pydot__tree_to_png # Requiere: pip install pydot

# --- GRAMÁTICAS CON NOMBRES RENOMBRADOS ---

# 1. Prueba de Asociatividad por IZQUIERDA
# Renombrado: 'exp_izq' -> 'jerarquia_baja', 'atom' -> 'unidad'
g_izq = """
    ?start: jerarquia_baja
    ?jerarquia_baja: jerarquia_baja "$" unidad | unidad
    ?unidad: "id"
    %import common.WS
    %ignore WS
"""

# 2. Prueba de Asociatividad por DERECHA
# Renombrado: 'exp_der' -> 'jerarquia_derecha', 'atom' -> 'unidad'
g_der = """
    ?start: jerarquia_derecha
    ?jerarquia_derecha: unidad "#" jerarquia_derecha | unidad
    ?unidad: "id"
    %import common.WS
    %ignore WS
"""

# 3. Prueba de PRECEDENCIA (Combinada)
# Renombrado: 'exp_suma' -> 'nivel_bajo', 'exp_mult' -> 'nivel_alto', 'atom' -> 'unidad'
g_prec = """
    ?start: nivel_bajo
    ?nivel_bajo: nivel_bajo "+" nivel_alto | nivel_alto
    ?nivel_alto: nivel_alto "*" unidad    | unidad
    ?unidad: "id" | "(" nivel_bajo ")"
    %import common.WS
    %ignore WS
"""

def generar_imagenes_renombradas():
    pruebas = [
        ("Prueba_Izquierda", g_izq, "id $ id $ id"),
        ("Prueba_Derecha", g_der, "id # id # id"),
        ("Prueba_Precedencia", g_prec, "id + id * id")
    ]

    for nombre, bnf, cadena in pruebas:
        print(f"Generando: {nombre}.png...")
        parser = Lark(bnf, parser='lalr')
        tree = parser.parse(cadena)
        pydot__tree_to_png(tree, f"{nombre}.png")

if __name__ == "__main__":
    generar_imagenes_renombradas()
    print("\nImágenes generadas con los nuevos nombres de reglas.")