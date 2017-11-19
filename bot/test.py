# -*- coding: utf-8 -*-
from funciones import Equipos
import unittest
import json
import urllib

class ClaseTest(unittest.TestCase):
    	"""Reminder test class."""

	def test_setNombre(self):
		equipo = Equipos()
		equipo.setNombre("Unión Deportiva Tesorillo")
		assert equipo.nombre == "Unión Deportiva Tesorillo" 				 				
	def test_setPuntos(self):
		puntos = Equipos()
		puntos.setPuntos("6")
		assert puntos.puntos == "6"
class JSONTest(unittest.TestCase):
	url="http://0.0.0.0:8000/"
	def test_pagina_recibida(self):
		ruta=urllib.urlopen(self.url)
		self.assertEqual(ruta.getcode(),200)
	def test_json_status_ok(self):
		ruta=urllib.urlopen(self.url)
		data = json.load(ruta)
		self.assertEqual(data["status"],"OK")


if __name__ == '__main__':
    unittest.main()
