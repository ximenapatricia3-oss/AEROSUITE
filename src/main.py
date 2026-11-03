"""
Aerosuite - Main Interactive Entry Point
Author: Ximena Lopez Yau
Description: Interactive command-line interface for aviation management tools.
"""

from core.aircraft_manager import AircraftManager


def main():
	print("=" * 60)
	print("  WELCOME TO AEROSUITE - Aviation Management System")
	print("=" * 60)

	# Inicializar el gestor de flota
	manager = AircraftManager()

	while True:
		print("\n--- Main Menu ---")
		print("1. View current fleet")
		print("2. Register a new aircraft")
		print("3. Search aircraft by ID")
		print("4. Exit")

		choice = input("\nSelect an option (1-4): ").strip()

		if choice == "1":
			print("\n[INFO] Current Fleet Status:")
			for aircraft in manager.list_fleet():
				print(
					f" - [{aircraft['id']}] {aircraft['model']} | "
					f"Status: {aircraft['status']} | Location: {aircraft['location']}"
				)

		elif choice == "2":
			print("\n[ACTION] Register a New Aircraft")
			plane_id = input("Enter Aircraft ID (e.g., AERO-005): ").strip()
			model = input("Enter Aircraft Model (e.g., Boeing 787): ").strip()
			status = input("Enter Status (e.g., Active / Maintenance): ").strip()
			location = input("Enter Location (e.g., Salt Lake City - SLC): ").strip()

			if plane_id and model and status and location:
				manager.add_aircraft(plane_id, model, status, location)
			else:
				print("[ERROR] All fields are required. Please try again.")

		elif choice == "3":
			print("\n[ACTION] Search Aircraft")
			search_id = input("Enter Aircraft ID to search: ").strip()
			result = manager.search_by_id(search_id)
			if result:
				print(
					f" -> Found: {result['model']} located in {result['location']} "
					f"with status '{result['status']}'."
				)
			else:
				print(" -> Aircraft not found in the system.")

		elif choice == "4":
			print("\n" + "=" * 60)
			print("  Thank you for using Aerosuite. Goodbye!")
			print("=" * 60)
			break
		else:
			print("[ERROR] Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
	main()
	
