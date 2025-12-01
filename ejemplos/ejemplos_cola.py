"""
Módulo: ejemplos_cola.py
Descripción: Ejemplos prácticos de uso de la estructura Cola.
"""

import sys
sys.path.insert(0, '../src')
from cola import Cola


def ejemplo_1_basico():
    """Ejemplo básico: operaciones fundamentales de enqueue y dequeue."""
    print("=" * 60)
    print("EJEMPLO 1: Operaciones Básicas")
    print("=" * 60)
    
    cola = Cola()
    
    print("\n1. Creamos una cola vacía:")
    cola.mostrar()
    
    print("\n2. Encolamos elementos:")
    cola.enqueue("Cliente 1")
    cola.enqueue("Cliente 2")
    cola.enqueue("Cliente 3")
    cola.mostrar()
    
    print(f"\n3. Tamaño de la cola: {cola.size()}")
    print(f"   Primer elemento (frente): {cola.front()}")
    print(f"   Último elemento (final): {cola.rear()}")
    
    print("\n4. Desencolamos elementos (en orden FIFO):")
    cola.dequeue()
    cola.mostrar()
    
    cola.dequeue()
    cola.mostrar()
    
    print("\n5. Verificamos si la cola está vacía:")
    print(f"   ¿Cola vacía? {cola.is_empty()}")


def ejemplo_2_simulacion_caja_banco():
    """Ejemplo práctico: Simulación de una cola de atención en un banco."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 2: Simulación de Cola en Caja de Banco")
    print("=" * 60)
    
    cola_banco = Cola()
    
    print("\nClientes llegando al banco:")
    clientes = ["Ana García", "Bruno López", "Carlos Martín", "Diana Ruiz", "Enrique Flores"]
    for cliente in clientes:
        cola_banco.enqueue(cliente)
    
    cola_banco.mostrar()
    
    print("\n\nAtendiendo clientes (orden FIFO):")
    while not cola_banco.is_empty():
        cliente = cola_banco.dequeue()
        print(f"   → Atendiendo a: {cliente}")
        cola_banco.mostrar()


def ejemplo_3_gestion_impresoras():
    """Ejemplo práctico: Gestión de cola de impresión."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 3: Cola de Impresión")
    print("=" * 60)
    
    cola_impresion = Cola()
    
    print("\nDocumentos enviados a imprimir:")
    documentos = [
        "Reporte_Ventas.pdf",
        "Contrato_Cliente.docx",
        "Factura_001.pdf",
        "Propuesta_Proyecto.pptx"
    ]
    
    for doc in documentos:
        cola_impresion.enqueue(doc)
        print(f"   📄 {doc} → En cola")
    
    cola_impresion.mostrar()
    
    print("\n\nImprimiendo documentos (orden FIFO):")
    contador = 0
    while not cola_impresion.is_empty():
        doc = cola_impresion.dequeue()
        contador += 1
        print(f"   🖨️  [{contador}] Imprimiendo: {doc}")


def ejemplo_4_manejo_errores():
    """Ejemplo: Manejo de errores en operaciones de cola."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 4: Manejo de Errores")
    print("=" * 60)
    
    cola = Cola()
    
    print("\n1. Intento de desencolar de una cola vacía:")
    try:
        cola.dequeue()
    except IndexError as e:
        print(f"   ❌ {e}")
    
    print("\n2. Intento de ver el frente de una cola vacía:")
    try:
        cola.front()
    except IndexError as e:
        print(f"   ❌ {e}")
    
    print("\n3. Encolamos datos y operamos normalmente:")
    cola.enqueue("Dato A")
    cola.enqueue("Dato B")
    cola.mostrar()
    print(f"   Frente: {cola.front()}")
    print(f"   Tamaño: {cola.size()}")


def ejemplo_5_tipos_datos_mixtos():
    """Ejemplo: Cola con diferentes tipos de datos."""
    print("\n\n" + "=" * 60)
    print("EJEMPLO 5: Cola con Tipos de Datos Mixtos")
    print("=" * 60)
    
    cola_mixta = Cola()
    
    print("\nEncolando diferentes tipos de datos:")
    cola_mixta.enqueue(42)
    cola_mixta.enqueue("Cadena de texto")
    cola_mixta.enqueue(3.14)
    cola_mixta.enqueue(True)
    cola_mixta.enqueue([1, 2, 3])
    cola_mixta.enqueue({"clave": "valor"})
    
    cola_mixta.mostrar()
    
    print("\nDesencolando e identificando tipos:")
    while not cola_mixta.is_empty():
        elemento = cola_mixta.dequeue()
        print(f"   Tipo: {type(elemento).__name__:15} | Valor: {elemento}")


if __name__ == "__main__":
    # Ejecuta todos los ejemplos
    ejemplo_1_basico()
    ejemplo_2_simulacion_caja_banco()
    ejemplo_3_gestion_impresoras()
    ejemplo_4_manejo_errores()
    ejemplo_5_tipos_datos_mixtos()
    
    print("\n\n" + "=" * 60)
    print("✓ Todos los ejemplos completados")
    print("=" * 60)
