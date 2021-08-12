import unittest
import sub_meter_data1


class testAirCompressorAnalysis(unittest.TestCase):

    def setUp(self):
        self.result = sub_meter_data1.AirCompressorAnalysis(self.data["energy_received__max"], self.data["energy_received__min"])

    def test_EnergyConsumption(self):
        # print(self.data["energy_received__max"])
        EnergyConsumption = (
            self.data['energy_received__max'] - self.data['energy_received__min'])
        self.assertEqual(self.result.EnergyConsumption(), 1000)

    def test_EnergyCost(self):
        self.assertEqual(self.result.EnergyCost(), 10000)

    def test_GHGEmission(self):
        self.assertEqual(self.result.GHGEmission(), 0.82)

    def test_MaximumActivePower(self):
        self.assertEqual(self.result.MaximumActivePower(), 599.391)

    def test_PercentageLoading(self):
        self.assertEqual(self.result.PercentageLoading(), 1743.3145887978142)
