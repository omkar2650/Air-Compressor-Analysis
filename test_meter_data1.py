import unittest
import sub_meter_data1
import json

try:
    jsonfile = open('F:\Files send by ganesh\sub_meter_data.json', 'r')
    jsonData = jsonfile.read()
    obj = json.loads(jsonData)

    DATA = {
        "active_power__avg": 498089.8825136612,
        "active_power__max": 599391,
        "demand_total__avg": 355313.1898987656,
        "demand_total__min": 104353.44,
        "power_factor__avg": 0.004879012345679004,
        "current_total__avg": 45.231320987654314,
        "current_total__max": 100.476,
        "energy_received__max": 16138742,
        "energy_received__min": 16137742,
        "no_of_active_readings": 366,
        "reading_unix_timestamp__max": 1613836746.21143,
        "tariff": 10,
        "motor_efficiency": 70,
        "rated_power": 2000,
        "run_hours": 10
    }


except FileNotFoundError:

    DATA = {
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


class TestAirCompressorAnalysis(unittest.TestCase):

    def setUp(self):
        self.result = sub_meter_data1.AirCompressorAnalysis(DATA["energy_received__max"],
                                                            DATA["energy_received__min"])

    def test_energy_consumption(self):
        self.assertEqual(self.result.energy_consumption(), DATA["energy_received__max"] - DATA["energy_received__min"])

    def test_energy_cost(self):
        self.assertEqual(self.result.energy_cost(), self.result.energy_consumption() * DATA['tariff'])

    def test_ghg_emission(self):
        self.assertEqual(self.result.ghg_emission(), self.result.energy_consumption() * 0.00082)

    def test_maximum_active_power(self):
        self.assertEqual(sub_meter_data1.maximum_active_power(), DATA['active_power__max'] / 1000)

    def test_PercentageLoading(self):
        self.assertEqual(sub_meter_data1.percentage_loading(),
                         ((DATA['active_power__avg'] / 1000) * DATA['motor_efficiency'] / DATA['rated_power']) * 100)
