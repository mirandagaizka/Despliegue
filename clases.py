class Participante:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def es_mayor_edad(self):
        return self.edad >= 18


class Taller:
    def __init__(self, nombre, limite_asistentes):
        self.nombre = nombre
        self.limite_asistentes = limite_asistentes
        self.lista_inscritos = []

    def cupos_disponibles(self):
        return self.limite_asistentes - len(self.lista_inscritos)

    def inscribir_participante(self, participante):
        if participante.es_mayor_edad() and self.cupos_disponibles() > 0:
            self.lista_inscritos.append(participante)
            return True
        return False


class SistemaReservas:
    def __init__(self):
        self.talleres = []

    def agregar_taller(self, taller):
        self.talleres.append(taller)

    def procesar_pago(self, participante, monto):
        """Simula una pasarela de pago. Devuelve True si exitoso, False si falla."""
        if monto > 0:
            print(f"  💳 Pago de {monto}€ procesado para {participante.nombre}")
            return True
        else:
            print(f"  ❌ Pago fallido para {participante.nombre} (monto inválido)")
            return False

    def registrar_participante_en_taller(self, participante, taller, monto=10):
        """Solo registra si el pago es exitoso y el taller existe."""
        if taller not in self.talleres:
            return False
        if not self.procesar_pago(participante, monto):
            return False
        return taller.inscribir_participante(participante)

    def listar_participantes_taller(self, taller):
        return [p.nombre for p in taller.lista_inscritos]