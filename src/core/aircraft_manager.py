"""
Aerosuite - Aircraft Manager Module
Author: Ximena Lopez Yau
Description: Handles aircraft data registration, status checking, and system logs.
"""

class AircraftManager:
    def __init__(self):
        # Base de datos simulada de aeronaves en el sistema
        self.fleet = [
            {"id": "AERO-001", "model": "Boeing 737", "status": "Active", "location": "Salt Lake City (SLC)"},
            {"id": "AERO-002", "model": "Airbus A320", "status": "Maintenance", "location": "Ogden (OGD)"},
            {"id": "AERO-003", "model": "Embraer E195", "status": "Active", "location": "Boise (BOI)"}
        ]

    def list_fleet(self):
        """Devuelve la lista completa de aeronaves registradas."""
        return self.fleet

    def add_aircraft(self, aircraft_id, model, status, location):
        """Agrega una nueva aeronave a la flota."""
        new_plane = {
            "id": aircraft_id,
            "model": model,
            "status": status,
            "location": location
        }
        self.fleet.append(new_plane)
        print(f"[SUCCESS] Aircraft {aircraft_id} ({model}) added successfully.")

    def search_by_id(self, aircraft_id):
        """Busca una aeronave por su identificador único."""
        for plane in self.fleet:
            if plane["id"].upper() == aircraft_id.upper():
                return plane
        return None
    