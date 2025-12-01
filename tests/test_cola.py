"""
Módulo: test_cola.py
Descripción: Tests unitarios para la clase Cola usando pytest.
"""

import pytest
import sys
sys.path.insert(0, '../src')
from cola import Cola


class TestColaBasico:
    """Pruebas básicas de creación e inicialización de Cola."""
    
    def test_cola_vacia_al_crear(self):
        """Verifica que una cola nueva está vacía."""
        cola = Cola()
        assert cola.is_empty() is True
    
    def test_size_cola_vacia(self):
        """Verifica que el tamaño de una cola vacía es 0."""
        cola = Cola()
        assert cola.size() == 0
    
    def test_items_lista_vacia(self):
        """Verifica que la lista interna de items es vacía."""
        cola = Cola()
        assert cola.items == []


class TestEnqueue:
    """Pruebas para la operación enqueue (encolar)."""
    
    def test_enqueue_un_elemento(self):
        """Verifica que se puede encolar un elemento."""
        cola = Cola()
        cola.enqueue("A")
        assert cola.size() == 1
        assert cola.front() == "A"
    
    def test_enqueue_multiples_elementos(self):
        """Verifica que se pueden encolar múltiples elementos."""
        cola = Cola()
        cola.enqueue(1)
        cola.enqueue(2)
        cola.enqueue(3)
        assert cola.size() == 3
        assert cola.front() == 1
        assert cola.rear() == 3
    
    def test_enqueue_diferentes_tipos(self):
        """Verifica que se pueden encolar diferentes tipos de datos."""
        cola = Cola()
        cola.enqueue(42)
        cola.enqueue("texto")
        cola.enqueue(3.14)
        cola.enqueue([1, 2, 3])
        cola.enqueue({"clave": "valor"})
        
        assert cola.size() == 5
        assert cola.front() == 42
    
    def test_enqueue_none(self):
        """Verifica que se puede encolar None."""
        cola = Cola()
        cola.enqueue(None)
        assert cola.front() is None
        assert cola.size() == 1


class TestDequeue:
    """Pruebas para la operación dequeue (desencolar)."""
    
    def test_dequeue_cola_vacia_lanza_error(self):
        """Verifica que desencolar de una cola vacía lanza IndexError."""
        cola = Cola()
        with pytest.raises(IndexError):
            cola.dequeue()
    
    def test_dequeue_un_elemento(self):
        """Verifica que se puede desencolar un elemento."""
        cola = Cola()
        cola.enqueue("A")
        elemento = cola.dequeue()
        assert elemento == "A"
        assert cola.size() == 0
    
    def test_dequeue_fifo(self):
        """Verifica que dequeue respeta el orden FIFO (First In, First Out)."""
        cola = Cola()
        cola.enqueue("primero")
        cola.enqueue("segundo")
        cola.enqueue("tercero")
        
        assert cola.dequeue() == "primero"
        assert cola.dequeue() == "segundo"
        assert cola.dequeue() == "tercero"
    
    def test_dequeue_todos_elementos(self):
        """Verifica que podemos desencolar todos los elementos."""
        cola = Cola()
        for i in range(5):
            cola.enqueue(i)
        
        for i in range(5):
            assert cola.dequeue() == i
        
        assert cola.is_empty() is True


class TestFrontYRear:
    """Pruebas para las operaciones front y rear."""
    
    def test_front_cola_vacia_lanza_error(self):
        """Verifica que front() en cola vacía lanza IndexError."""
        cola = Cola()
        with pytest.raises(IndexError):
            cola.front()
    
    def test_rear_cola_vacia_lanza_error(self):
        """Verifica que rear() en cola vacía lanza IndexError."""
        cola = Cola()
        with pytest.raises(IndexError):
            cola.rear()
    
    def test_front_sin_remover(self):
        """Verifica que front() no remueve el elemento."""
        cola = Cola()
        cola.enqueue("A")
        cola.enqueue("B")
        
        frente1 = cola.front()
        frente2 = cola.front()
        
        assert frente1 == frente2 == "A"
        assert cola.size() == 2
    
    def test_rear_sin_remover(self):
        """Verifica que rear() no remueve el elemento."""
        cola = Cola()
        cola.enqueue("X")
        cola.enqueue("Y")
        cola.enqueue("Z")
        
        final1 = cola.rear()
        final2 = cola.rear()
        
        assert final1 == final2 == "Z"
        assert cola.size() == 3
    
    def test_front_y_rear_elemento_unico(self):
        """Verifica que front y rear retornan el mismo elemento si hay solo uno."""
        cola = Cola()
        cola.enqueue("unico")
        
        assert cola.front() == cola.rear() == "unico"


class TestVaciar:
    """Pruebas para la operación vaciar."""
    
    def test_vaciar_cola_vacia(self):
        """Verifica que vaciar una cola vacía no causa error."""
        cola = Cola()
        cola.vaciar()
        assert cola.is_empty() is True
    
    def test_vaciar_cola_con_elementos(self):
        """Verifica que vaciar elimina todos los elementos."""
        cola = Cola()
        cola.enqueue(1)
        cola.enqueue(2)
        cola.enqueue(3)
        
        cola.vaciar()
        
        assert cola.is_empty() is True
        assert cola.size() == 0
    
    def test_vaciar_y_reutilizar(self):
        """Verifica que después de vaciar se puede reutilizar la cola."""
        cola = Cola()
        cola.enqueue("A")
        cola.vaciar()
        cola.enqueue("B")
        
        assert cola.size() == 1
        assert cola.front() == "B"


class TestSize:
    """Pruebas para la operación size."""
    
    def test_size_vacia(self):
        """Verifica que size retorna 0 para cola vacía."""
        cola = Cola()
        assert cola.size() == 0
    
    def test_size_aumenta_con_enqueue(self):
        """Verifica que size aumenta con cada enqueue."""
        cola = Cola()
        assert cola.size() == 0
        cola.enqueue("A")
        assert cola.size() == 1
        cola.enqueue("B")
        assert cola.size() == 2
    
    def test_size_disminuye_con_dequeue(self):
        """Verifica que size disminuye con cada dequeue."""
        cola = Cola()
        cola.enqueue("A")
        cola.enqueue("B")
        assert cola.size() == 2
        cola.dequeue()
        assert cola.size() == 1
        cola.dequeue()
        assert cola.size() == 0


class TestIsEmpty:
    """Pruebas para la operación is_empty."""
    
    def test_is_empty_cola_vacia(self):
        """Verifica que is_empty retorna True para cola vacía."""
        cola = Cola()
        assert cola.is_empty() is True
    
    def test_is_empty_con_elementos(self):
        """Verifica que is_empty retorna False si hay elementos."""
        cola = Cola()
        cola.enqueue("A")
        assert cola.is_empty() is False
    
    def test_is_empty_despues_desencolar_todos(self):
        """Verifica que is_empty es True después de desencolar todos."""
        cola = Cola()
        cola.enqueue("A")
        cola.dequeue()
        assert cola.is_empty() is True


class TestOperacionesSecuenciales:
    """Pruebas de secuencias complejas de operaciones."""
    
    def test_secuencia_enqueue_dequeue(self):
        """Verifica una secuencia mixta de enqueue y dequeue."""
        cola = Cola()
        cola.enqueue(1)
        cola.enqueue(2)
        assert cola.dequeue() == 1
        cola.enqueue(3)
        assert cola.dequeue() == 2
        assert cola.dequeue() == 3
        assert cola.is_empty() is True
    
    def test_simulacion_banco(self):
        """Simula una cola de atención en banco."""
        cola = Cola()
        clientes = ["Ana", "Bruno", "Carlos"]
        
        for cliente in clientes:
            cola.enqueue(cliente)
        
        # Atiende clientes en orden
        assert cola.dequeue() == "Ana"
        assert cola.dequeue() == "Bruno"
        assert cola.dequeue() == "Carlos"
        assert cola.is_empty() is True
    
    def test_alternancia_enqueue_dequeue(self):
        """Prueba alternancia de enqueue y dequeue."""
        cola = Cola()
        
        cola.enqueue("A")
        cola.enqueue("B")
        assert cola.dequeue() == "A"
        
        cola.enqueue("C")
        cola.enqueue("D")
        assert cola.dequeue() == "B"
        assert cola.dequeue() == "C"
        assert cola.dequeue() == "D"


class TestReprYStr:
    """Pruebas para representaciones en string."""
    
    def test_str_cola_vacia(self):
        """Verifica __str__ para cola vacía."""
        cola = Cola()
        assert str(cola) == "Cola vacía"
    
    def test_str_con_elementos(self):
        """Verifica __str__ con elementos."""
        cola = Cola()
        cola.enqueue(1)
        cola.enqueue(2)
        assert "1" in str(cola)
        assert "2" in str(cola)
    
    def test_repr(self):
        """Verifica __repr__."""
        cola = Cola()
        cola.enqueue("X")
        assert "Cola" in repr(cola)


if __name__ == "__main__":
    # Ejecuta los tests con pytest
    pytest.main([__file__, "-v", "--tb=short"])
