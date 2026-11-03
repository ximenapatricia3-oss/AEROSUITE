"""
Aerosuite - Aircraft Manager Module
Author: Ximena Fletcher
Description: Handles aircraft data registration, status updates, filtering, and fleet statistics.
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
        """Agrega una nueva aeronave a la flota validando que el ID no exista."""
        # Verificar si ya existe
        for plane in self.fleet:
            if plane["id"].upper() == aircraft_id.upper():
                return False, f"Aircraft ID {aircraft_id} already exists."
        
        new_plane = {
            "id": aircraft_id.upper(),
            "model": model,
            "status": status.capitalize(),
            "location": location
        }
        self.fleet.append(new_plane)
        return True, f"Aircraft {aircraft_id} ({model}) added successfully."

    def search_by_id(self, aircraft_id):
        """Busca una aeronave por su identificador único."""
        for plane in self.fleet:
            if plane["id"].upper() == aircraft_id.upper():
                return plane
        return None

    def filter_by_status(self, status):
        """Filtra las aeronaves según su estado (ej. Active, Maintenance)."""
        return [plane for plane in self.fleet if plane["status"].lower() == status.lower()]

    def update_status(self, aircraft_id, new_status):
        """Actualiza el estado de una aeronave existente."""
        plane = self.search_by_id(aircraft_id)
        if plane:
            plane["status"] = new_status.capitalize()
            return True, f"Aircraft {aircraft_id} status updated to '{plane['status']}'."
        return False, "Aircraft not found."

    def delete_aircraft(self, aircraft_id):
        """Elimina una aeronave de la flota por su ID."""
        plane = self.search_by_id(aircraft_id)
        if plane:
            self.fleet.remove(plane)
            return True, f"Aircraft {aircraft_id} has been removed from the fleet."
        return False, "Aircraft not found."

    def get_statistics(self):
        """Devuelve un resumen estadístico de la flota."""
        total = len(self.fleet)
        active = len(self.filter_by_status("Active"))
        maintenance = len(self.filter_by_status("Maintenance"))
        return {
            "total": total,
            "active": active,
            "maintenance": maintenance
        }
    