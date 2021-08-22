import json

try:
    jsonfile = open('F:\Files send by ganesh\sub_meter_data.json', 'r')
    jsonData = jsonfile.read()
    obj = json.loads(jsonData)
    # breakpoint()

except FileNotFoundError:
    print("FileNotFound")
    # breakpoint()

    obj = {
        "active_power__avg": 0,
        "active_power__max": 0,
        "demand_total__avg": 0,
        "demand_total__max": 0,
        "demand_total__min": 0,
        "power_factor__avg": 0,
        "current_total__avg": 0,
        "current_total__max": 0,
        "energy_received__max": 0,
        "energy_received__min": 0,
        "no_of_active_readings": 0,
        "reading_unix_timestamp__max": 0,
        "tariff": 0,
        "motor_efficiency": 0,
        "rated_power": 1,
        "run_hours": 0
    }


def maximum_active_power():
    return obj['active_power__max'] / 1000


def percentage_loading():
    return ((obj['active_power__avg'] / 1000) * obj['motor_efficiency'] / obj['rated_power']) * 100


class AirCompressorAnalysis:
    def __init__(self, energy_received__max, energy_received__min):
        self.energy_1 = energy_received__max
        self.energy_2 = energy_received__min

    def energy_consumption(self):
        return self.energy_1 - self.energy_2

    def energy_cost(self):
        return self.energy_consumption() * obj['tariff']

    def ghg_emission(self):
        return self.energy_consumption() * 0.00082


# Total = AirCompressorAnalysis(obj['energy_received__max'], obj['energy_received__min'])
# Total.energy_consumption()
# Total.EnergyCost()
# Total.ghg_emission()
# maximum_active_power()
# percentage_loading()

