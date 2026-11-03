"""
Aerosuite - Main Interactive Entry Point
Author: Ximena Lopez Yau
Description: Advanced command-line interface for aviation management tools.
"""

from core.aircraft_manager import AircraftManager

def main():
	print("=" * 60)
	print("  WELCOME TO AEROSUITE - Advanced Aviation Management System")
	print("=" * 60)

	manager = AircraftManager()

	while True:
		print("\n" + "=" * 30 + " MAIN MENU " + "=" * 30)
		print("1. View current fleet")
		print("2. Register a new aircraft")
		print("3. Search aircraft by ID")
		print("4. Filter aircraft by status (Active / Maintenance)")
		print("5. Update aircraft status")
		print("6. Delete an aircraft")
		print("7. View fleet statistics")
		print("8. Exit")
		print("=" * 71)
        
		choice = input("\nSelect an option (1-8): ").strip()

		if choice == "1":
			print("\n[INFO] Current Fleet Status:")
			for aircraft in manager.list_fleet():
				print(f" - [{aircraft['id']}] {aircraft['model']} | Status: {aircraft['status']} | Location: {aircraft['location']}")

		elif choice == "2":
			print("\n[ACTION] Register a New Aircraft")
			plane_id = input("Enter Aircraft ID (e.g., AERO-005): ").strip()
			model = input("Enter Aircraft Model (e.g., Boeing 787): ").strip()
			status = input("Enter Status (Active / Maintenance): ").strip()
			location = input("Enter Location (e.g., Salt Lake City - SLC): ").strip()

			if plane_id and model and status and location:
				success, msg = manager.add_aircraft(plane_id, model, status, location)
				print(f"\n[SUCCESS] {msg}" if success else f"\n[ERROR] {msg}")
			else:
				print("[ERROR] All fields are required. Please try again.")

		elif choice == "3":
			print("\n[ACTION] Search Aircraft")
			search_id = input("Enter Aircraft ID to search: ").strip()
			result = manager.search_by_id(search_id)
			if result:
				print(f" -> Found: {result['model']} located in {result['location']} with status '{result['status']}'.")
			else:
				print(" -> Aircraft not found in the system.")

		elif choice == "4":
			print("\n[ACTION] Filter Fleet by Status")
			status_filter = input("Enter status to filter by (Active / Maintenance): ").strip()
			filtered = manager.filter_by_status(status_filter)
			if filtered:
				print(f"\n[INFO] Aircraft with status '{status_filter}':")
				for aircraft in filtered:
					print(f" - [{aircraft['id']}] {aircraft['model']} | Location: {aircraft['location']}")
			else:
				print(f" -> No aircraft found with status '{status_filter}'.")

		elif choice == "5":
			print("\n[ACTION] Update Aircraft Status")
			plane_id = input("Enter Aircraft ID to update: ").strip()
			new_status = input("Enter new status (Active / Maintenance): ").strip()
			success, msg = manager.update_status(plane_id, new_status)
			print(f"\n[SUCCESS] {msg}" if success else f"\n[ERROR] {msg}")

		elif choice == "6":
			print("\n[ACTION] Delete Aircraft")
			plane_id = input("Enter Aircraft ID to delete: ").strip()
			confirm = input(f"Are you sure you want to delete {plane_id}? (y/n): ").strip().lower()
			if confirm == 'y':
				success, msg = manager.delete_aircraft(plane_id)
				print(f"\n[SUCCESS] {msg}" if success else f"\n[ERROR] {msg}")
			else:
				print(" -> Deletion cancelled.")

		elif choice == "7":
			print("\n[INFO] Fleet Statistics Summary:")
			stats = manager.get_statistics()
			print(f" ✈️ Total Aircraft: {stats['total']}")
			print(f" ✅ Active Aircraft: {stats['active']}")
			print(f" 🔧 In Maintenance: {stats['maintenance']}")

		elif choice == "8":
			print("\n" + "=" * 60)
			print("  Thank you for using Aerosuite. Goodbye!")
			print("=" * 60)
			break
		else:
			print("[ERROR] Invalid option. Please choose a number between 1 and 8.")

if __name__ == "__main__":
	main()
