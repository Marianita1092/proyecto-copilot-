"""
Ejemplos prácticos de uso de la estructura de datos Cola (Queue)
Demuestra casos de uso reales en sistemas de software
"""

import sys
from pathlib import Path

# Añadir el directorio src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cola import Cola


def ejemplo_1_banco():
    """
    Ejemplo 1: Sistema de atención de clientes en un banco
    Los clientes llegan y se atienden en orden de llegada (FIFO)
    """
    print("\n" + "="*60)
    print("EJEMPLO 1: Sistema de Atención en Banco")
    print("="*60)
    
    cola_banco = Cola()
    
    # Clientes llegan al banco
    clientes = ["Cliente_001", "Cliente_002", "Cliente_003", 
                "Cliente_004", "Cliente_005"]
    
    print("\n📍 Clientes llegando al banco...")
    for cliente in clientes:
        cola_banco.enqueue(cliente)
        print(f"  ✓ {cliente} llega a la cola")
    
    print(f"\n📊 Total de clientes esperando: {cola_banco.size()}")
    
    # Próximo cliente en ser atendido
    if not cola_banco.is_empty():
        print(f"\n👤 Próximo cliente a atender: {cola_banco.front()}")
    
    # Atender clientes
    print("\n💼 Atendiendo clientes...")
    contador = 1
    while not cola_banco.is_empty():
        cliente = cola_banco.dequeue()
        print(f"  {contador}. Atendiendo a {cliente}")
        contador += 1
    
    print(f"\n✅ Cola vacía. Todos los clientes fueron atendidos.")


def ejemplo_2_impresora():
    """
    Ejemplo 2: Cola de impresión de documentos
    Los documentos se imprimen en el orden que se enviaron
    """
    print("\n" + "="*60)
    print("EJEMPLO 2: Cola de Impresión de Documentos")
    print("="*60)
    
    cola_impresion = Cola()
    
    # Documentos a imprimir
    documentos = [
        {"nombre": "Reporte_Mensual.pdf", "paginas": 5, "usuario": "Ana"},
        {"nombre": "Presentacion.pptx", "paginas": 20, "usuario": "Bruno"},
        {"nombre": "Contrato.docx", "paginas": 3, "usuario": "Carlos"},
        {"nombre": "Especificaciones.pdf", "paginas": 12, "usuario": "Diana"},
    ]
    
    print("\n📄 Enviando documentos a imprimir...")
    for doc in documentos:
        cola_impresion.enqueue(doc)
        print(f"  ✓ {doc['nombre']} ({doc['paginas']} págs, usuario: {doc['usuario']})")
    
    print(f"\n📊 Documentos en cola: {cola_impresion.size()}")
    
    # Simular impresión
    print("\n🖨️  Imprimiendo documentos...")
    documento_actual = 1
    while not cola_impresion.is_empty():
        doc = cola_impresion.dequeue()
        print(f"  [{documento_actual}] Imprimiendo: {doc['nombre']}")
        print(f"      └─ {doc['paginas']} páginas | Usuario: {doc['usuario']}")
        documento_actual += 1
    
    print(f"\n✅ Todos los documentos fueron imprimidos.")


def ejemplo_3_restaurante():
    """
    Ejemplo 3: Sistema de pedidos en un restaurante
    Los pedidos se preparan en orden de llegada
    """
    print("\n" + "="*60)
    print("EJEMPLO 3: Sistema de Pedidos en Restaurante")
    print("="*60)
    
    cola_pedidos = Cola()
    
    # Pedidos que llegan
    pedidos = [
        {"id": 101, "cliente": "Mesa_1", "plato": "Pasta Carbonara", "tiempo": 15},
        {"id": 102, "cliente": "Mesa_2", "plato": "Filete Milanesa", "tiempo": 20},
        {"id": 103, "cliente": "Mesa_3", "plato": "Ensalada Cesar", "tiempo": 10},
        {"id": 104, "cliente": "Mesa_4", "plato": "Pizza Margarita", "tiempo": 18},
    ]
    
    print("\n🍽️  Pedidos recibidos...")
    for pedido in pedidos:
        cola_pedidos.enqueue(pedido)
        print(f"  ✓ Pedido #{pedido['id']}: {pedido['plato']} para {pedido['cliente']}")
    
    print(f"\n📊 Pedidos en espera: {cola_pedidos.size()}")
    
    # Ver primer pedido
    if not cola_pedidos.is_empty():
        primer_pedido = cola_pedidos.front()
        print(f"\n👨‍🍳 Preparando ahora: Pedido #{primer_pedido['id']} ({primer_pedido['plato']})")
    
    # Procesar pedidos
    print("\n⏱️  Procesando pedidos...")
    pedidos_procesados = 0
    while not cola_pedidos.is_empty():
        pedido = cola_pedidos.dequeue()
        pedidos_procesados += 1
        print(f"  ✓ Pedido #{pedido['id']} listo! ({pedido['tiempo']} min)")
    
    print(f"\n✅ {pedidos_procesados} pedidos completados.")


def ejemplo_4_tareas_servidor():
    """
    Ejemplo 4: Cola de tareas en un servidor web
    Las solicitudes se procesan en orden FIFO
    """
    print("\n" + "="*60)
    print("EJEMPLO 4: Cola de Tareas en Servidor Web")
    print("="*60)
    
    cola_solicitudes = Cola()
    
    # Solicitudes HTTP
    solicitudes = [
        {"id": 1, "tipo": "GET", "endpoint": "/api/usuarios", "usuario": "app_1"},
        {"id": 2, "tipo": "POST", "endpoint": "/api/datos", "usuario": "app_2"},
        {"id": 3, "tipo": "GET", "endpoint": "/api/productos", "usuario": "app_3"},
        {"id": 4, "tipo": "PUT", "endpoint": "/api/perfil", "usuario": "app_1"},
        {"id": 5, "tipo": "DELETE", "endpoint": "/api/cache", "usuario": "app_4"},
    ]
    
    print("\n🌐 Solicitudes llegando al servidor...")
    for solicitud in solicitudes:
        cola_solicitudes.enqueue(solicitud)
        print(f"  ✓ [{solicitud['id']}] {solicitud['tipo']} {solicitud['endpoint']}")
    
    print(f"\n📊 Solicitudes en cola: {cola_solicitudes.size()}")
    print(f"⏳ Próxima a procesar: Solicitud #{cola_solicitudes.front()['id']}")
    
    # Procesar solicitudes
    print("\n⚙️  Procesando solicitudes...")
    tiempo_promedio = 0
    num_solicitudes = cola_solicitudes.size()
    
    while not cola_solicitudes.is_empty():
        solicitud = cola_solicitudes.dequeue()
        tiempo_promedio += 50  # Simulación: 50ms por solicitud
        print(f"  ✓ Procesada solicitud #{solicitud['id']} ({solicitud['tipo']})")
    
    if num_solicitudes > 0:
        print(f"\n✅ {num_solicitudes} solicitudes procesadas.")


def ejemplo_5_estadisticas():
    """
    Ejemplo 5: Demostración de estadísticas y estado de la cola
    """
    print("\n" + "="*60)
    print("EJEMPLO 5: Estadísticas de Cola")
    print("="*60)
    
    cola = Cola()
    
    # Operaciones
    print("\n📈 Monitoreando operaciones de cola...")
    
    print("\n1️⃣  Estado inicial:")
    print(f"   Vacía: {cola.is_empty()}, Tamaño: {cola.size()}")
    
    print("\n2️⃣  Encolando 10 elementos...")
    for i in range(1, 11):
        cola.enqueue(f"Elemento_{i}")
    print(f"   Tamaño actual: {cola.size()}")
    print(f"   Primero: {cola.front()}, Último: {cola.rear()}")
    
    print("\n3️⃣  Desencolando 3 elementos...")
    for _ in range(3):
        cola.dequeue()
    print(f"   Tamaño actual: {cola.size()}")
    print(f"   Primero: {cola.front()}, Último: {cola.rear()}")
    
    print("\n4️⃣  Mostrando estado actual:")
    cola.mostrar()
    
    print("\n5️⃣  Vaciando cola...")
    cola.vaciar()
    print(f"   Vacía: {cola.is_empty()}, Tamaño: {cola.size()}")


def main():
    """Ejecuta todos los ejemplos"""
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + " EJEMPLOS DE USO: ESTRUCTURA DE DATOS COLA (QUEUE) ".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    # Ejecutar todos los ejemplos
    ejemplo_1_banco()
    ejemplo_2_impresora()
    ejemplo_3_restaurante()
    ejemplo_4_tareas_servidor()
    ejemplo_5_estadisticas()
    
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + " FIN DE EJEMPLOS ".center(58) + "█")
    print("█" + " "*58 + "█")
    print("█"*60 + "\n")


if __name__ == "__main__":
    main()
