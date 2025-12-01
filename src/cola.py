"""
Módulo: cola.py
Descripción: Implementación de la estructura de datos Cola (Queue)
             usando una lista de Python.
Autor: Estructura de Datos 2
"""


class Cola:
    """
    Clase que implementa una Cola (FIFO - First In, First Out).
    
    Atributos:
        items (list): Lista interna que almacena los elementos de la cola.
    
    Métodos:
        enqueue(elemento): Añade un elemento al final de la cola.
        dequeue(): Extrae y devuelve el primer elemento de la cola.
        is_empty(): Verifica si la cola está vacía.
        size(): Retorna el número de elementos en la cola.
        front(): Retorna el primer elemento sin extraerlo.
        rear(): Retorna el último elemento sin extraerlo.
        mostrar(): Imprime los elementos de la cola.
        vaciar(): Elimina todos los elementos de la cola.
    """
    
    def __init__(self):
        """Inicializa una cola vacía."""
        self.items = []
    
    def enqueue(self, elemento):
        """
        Añade un elemento al final de la cola.
        
        Args:
            elemento: El elemento a añadir a la cola.
        
        Returns:
            None
        """
        self.items.append(elemento)
        print(f"✓ Elemento '{elemento}' encolado.")
    
    def dequeue(self):
        """
        Extrae y devuelve el primer elemento de la cola.
        
        Returns:
            El primer elemento de la cola.
        
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("Error: No se puede desencolar de una cola vacía.")
        elemento = self.items.pop(0)
        print(f"✓ Elemento '{elemento}' desencolado.")
        return elemento
    
    def is_empty(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Retorna el número de elementos en la cola.
        
        Returns:
            int: La cantidad de elementos en la cola.
        """
        return len(self.items)
    
    def front(self):
        """
        Retorna el primer elemento de la cola sin extraerlo.
        
        Returns:
            El primer elemento de la cola.
        
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("Error: La cola está vacía.")
        return self.items[0]
    
    def rear(self):
        """
        Retorna el último elemento de la cola sin extraerlo.
        
        Returns:
            El último elemento de la cola.
        
        Raises:
            IndexError: Si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("Error: La cola está vacía.")
        return self.items[-1]
    
    def mostrar(self):
        """
        Imprime todos los elementos de la cola de forma legible.
        
        Returns:
            None
        """
        if self.is_empty():
            print("Cola: [ VACÍA ]")
        else:
            print(f"Cola: {' <- '.join(map(str, self.items))}")
            print(f"     (frente)                          (final)")
    
    def vaciar(self):
        """
        Elimina todos los elementos de la cola.
        
        Returns:
            None
        """
        self.items.clear()
        print("✓ Cola vaciada.")
    
    def __str__(self):
        """Representación en string de la cola."""
        if self.is_empty():
            return "Cola vacía"
        return str(self.items)
    
    def __repr__(self):
        """Representación técnica de la cola."""
        return f"Cola({self.items})"
