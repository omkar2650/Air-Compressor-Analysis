import json

try:
    jsonfile = open('F:\Files send by ganesh\sub_meter_data.json', 'r')

except FileNotFoundError:
    print("FileNotFoundError")

jsonData = jsonfile.read()
obj = json.loads(jsonData)


class AirCompressorAnalysis:

    def __init__(self, energy_received__max, energy_received__min):
        self.energy_1 = energy_received__max
        self.energy_2 = energy_received__min

    def EnergyConsumption(self):
        return self.energy_1 - self.energy_2

    def EnergyCost(self):
        return Energy_Consumption * obj['tariff']

    def GHGEmission(self):
        return Energy_Consumption * 0.00082

    def MaximumActivePower(self):
        return obj['active_power__max'] / 1000

    def PercentageLoading(self):
        return ((obj['active_power__avg'] / 1000) * obj['motor_efficiency'] / obj['rated_power']) * 100


Total = AirCompressorAnalysis(obj['energy_received__max'], obj['energy_received__min'])
Energy_Consumption = Total.EnergyConsumption()
Energy_Cost = Total.EnergyCost()
Total.GHGEmission()
Total.MaximumActivePower()
a = Total.PercentageLoading()
print(a)
