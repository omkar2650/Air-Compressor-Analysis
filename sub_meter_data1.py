import json

try:
    jsonfile = open('F:\Files send by ganesh\sub_meter_data.json', 'r')

except FileNotFoundError:
    print("FileNotFound")

jsonData = jsonfile.read()
obj = json.loads(jsonData)


def MaximumActivePower():
    return obj['active_power__max'] / 1000


def PercentageLoading():
    return ((obj['active_power__avg'] / 1000) * obj['motor_efficiency'] / obj['rated_power']) * 100


class AirCompressorAnalysis:
    def __init__(self, energy_received__max, energy_received__min):
        self.energy_1 = energy_received__max
        self.energy_2 = energy_received__min

    def EnergyConsumption(self):
        return self.energy_1 - self.energy_2

    def EnergyCost(self):
        return self.EnergyConsumption() * obj['tariff']

    def GHGEmission(self):
        return self.EnergyConsumption() * 0.00082


Total = AirCompressorAnalysis(obj['energy_received__max'], obj['energy_received__min'])
Total.EnergyConsumption()
Total.EnergyCost()
Total.GHGEmission()
MaximumActivePower()
PercentageLoading()
