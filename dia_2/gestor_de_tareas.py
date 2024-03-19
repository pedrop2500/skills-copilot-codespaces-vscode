class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    """
    Clase que representa un gestor de tareas.

    Attributes:
        tareas (list): Lista de tareas almacenadas en el gestor.
    """

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        """
        Agrega una tarea al gestor.

        Args:
            tarea (objeto): La tarea a agregar.
        """
        self.tareas.append(tarea)

    def listar_tareas(self):
        """
        Lista todas las tareas almacenadas en el gestor.
        """
        for tarea in self.tareas:
            print(tarea)

    def marcar_completada(self, tarea):
        """
        Marca una tarea como completada.

        Args:
            tarea (objeto): La tarea a marcar como completada.
        """
        if tarea in self.tareas:
            tarea.completada = True
        else:
            print("La tarea no existe")

    def eliminar_tarea(self, tarea):
        """
        Elimina una tarea del gestor.

        Args:
            tarea (objeto): La tarea a eliminar.
        """
        if tarea in self.tareas:
            self.tareas.remove(tarea)
        else:
            print("La tarea no existe")

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

# Ejemplo de uso
gestor = GestorTareas()

tarea1 = Tarea("Hacer la compra")
tarea2 = Tarea("Limpiar la casa")

gestor.agregar_tarea(tarea1)
gestor.agregar_tarea(tarea2)

gestor.listar_tareas()

gestor.marcar_completada(tarea1)

gestor.listar_tareas()
tarea3 = Tarea("Sacar la basura")
gestor.agregar_tarea(tarea3)

gestor.listar_tareas()

gestor.marcar_completada(tarea2)

gestor.listar_tareas()