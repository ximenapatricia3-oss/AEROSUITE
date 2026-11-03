"""
Aerosuite - Main Entry Point
Author: Ximena Lopez Yau
Description: Core initialization script for aviation management tools.
"""

from core.aircraft_manager import AircraftManager


def main():
	print("=" * 60)
	print("  WELCOME TO AEROSUITE - Aviation Management System")
	print("=" * 60)

	# Inicializar el gestor de flota
	manager = AircraftManager()

	# 1. Mostrar la flota actual
	print("\n[INFO] Current Fleet Status:")
	for aircraft in manager.list_fleet():
		print(f" - [{aircraft['id']}] {aircraft['model']} | Status: {aircraft['status']} | Location: {aircraft['location']}")

	# 2. Agregar una nueva aeronave de prueba
	print("\n[ACTION] Registering a new aircraft...")
	manager.add_aircraft("AERO-004", "Bombardier Challenger 350", "Active", "Salt Lake City (SLC)")

	# 3. Buscar una aeronave específica
	search_id = "AERO-004"
	print(f"\n[INFO] Searching for aircraft ID: {search_id}")
	result = manager.search_by_id(search_id)
	if result:
		print(f" -> Found: {result['model']} located in {result['location']} with status '{result['status']}'.")
	else:
		print(" -> Aircraft not found.")

	print("\n" + "=" * 60)
	print("  Aerosuite execution completed successfully.")
	print("=" * 60)


if __name__ == "__main__":
	main()

