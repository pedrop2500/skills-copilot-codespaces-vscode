import unittest
from gestor_de_tareas import GestorTareas
from gestor_de_tareas import Tarea

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        tarea = Tarea("Hacer la compra")
        self.gestor.agregar_tarea(tarea)
        self.assertIn(tarea, self.gestor.tareas)

    def test_listar_tareas(self):
        tarea1 = Tarea("Hacer la compra")
        tarea2 = Tarea("Lavar los platos")
        self.gestor.agregar_tarea(tarea1)
        self.gestor.agregar_tarea(tarea2)
        self.assertEqual(len(self.gestor.tareas), 2)
        self.assertIn(tarea1, self.gestor.tareas)
        self.assertIn(tarea2, self.gestor.tareas)

    def test_marcar_completada(self):
        tarea = Tarea("Hacer la compra")
        self.gestor.agregar_tarea(tarea)
        self.gestor.marcar_completada(tarea)
        self.assertTrue(tarea.completada)

    def test_eliminar_tarea(self):
        tarea = Tarea("Hacer la compra")
        self.gestor.agregar_tarea(tarea)
        self.gestor.eliminar_tarea(tarea)
        self.assertNotIn(tarea, self.gestor.tareas)

if __name__ == '__main__':
    unittest.main()