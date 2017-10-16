# -*- coding: utf-8 -*-
from funciones import Equipos
import unittest

class ClaseTest(unittest.TestCase):
    	"""Reminder test class."""

	def test_setNombre(self):
		equipo = Equipos()
		equipo.setNombre("Unión Deportiva Tesorillo")
		assert equipo.nombre == "Unión Deportiva Tesorillo"
		#self.assertEqual("UDT",Equipos.setNombre("Unión Deportiva 				Tesorillo"))
		#assertEqual("Unión Deportiva 					Tesorillo",equipo.setNombre("Unión Deportiva 					Tesorillo"))
	def test_setPuntos(self):
		puntos = Equipos()
		puntos.setPuntos("6")
		assert puntos.puntos == "6"


if __name__ == '__main__':
    unittest.main()
