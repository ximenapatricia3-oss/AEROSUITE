"""
Aerosuite - Aviation Logistics and Operations Core
Author: Ximena López Yau
"""


class AerosuiteCore:
	def __init__(self):
		self.flights = []
		self.maintenance_alerts = []

	def register_flight(self, flight_id, origin, destination, status="Scheduled"):
		flight = {
			"flight_id": flight_id,
			"origin": origin,
			"destination": destination,
			"status": status,
		}
		self.flights.append(flight)
		print(f"Flight {flight_id} successfully registered: {origin} -> {destination}")

	def add_maintenance_alert(self, aircraft_id, component, severity="Medium"):
		alert = {
			"aircraft_id": aircraft_id,
			"component": component,
			"severity": severity,
			"status": "Pending Inspection",
		}
		self.maintenance_alerts.append(alert)
		print(f"Maintenance Alert: Aircraft {aircraft_id} - {component} ({severity} priority)")

	def get_operational_status(self):
		print("\n--- Aerosuite System Status ---")
		print(f"Total active flights tracked: {len(self.flights)}")
		for flight in self.flights:
			print(
				f"Flight: {flight['flight_id']} | Route: {flight['origin']} to "
				f"{flight['destination']} | Status: {flight['status']}"
			)
		print("\n--- Maintenance Tracking ---")
		print(f"Total pending alerts: {len(self.maintenance_alerts)}")
		for alert in self.maintenance_alerts:
			print(
				f"Aircraft: {alert['aircraft_id']} | Issue: {alert['component']} | "
				f"Priority: {alert['severity']} | Status: {alert['status']}"
			)


if __name__ == "__main__":
	system = AerosuiteCore()
	system.register_flight("AES-101", "Salt Lake City (SLC)", "Lima (LIM)", "On Time")
	system.register_flight("AES-102", "Lima (LIM)", "Santiago (SCL)", "Boarding")
	system.add_maintenance_alert("BOE-737-08", "Engine Turbine Check", "High")
	system.get_operational_status()
