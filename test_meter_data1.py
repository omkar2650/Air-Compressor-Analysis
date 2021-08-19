import unittest
import sub_meter_data1


class TestAirCompressorAnalysis(unittest.TestCase):

    def setUp(self):
        self.result = sub_meter_data1.AirCompressorAnalysis(self.obj["energy_received__max"],
                                                            self.obj["energy_received__min"])

    def test_energy_consumption(self):
        self.result.energy_consumption = (self.obj['energy_received__max'] - self.obj['energy_received__min'])
        self.assertEqual(self.result.energy_consumption(), 1000)

    def test_energy_cost(self):
        self.assertEqual(self.result.energy_cost(), 10000)

    def test_ghg_emission(self):
        self.assertEqual(self.result.ghg_emission(), 0.82)

    def test_MaximumActivePower(self):
        self.assertEqual(self.obj.MaximumActivePower(), 599.391)

    def test_PercentageLoading(self):
        self.assertEqual(self.obj.PercentageLoading(), 1743.3145887978142)
