import unittest

from geo_engine import generate_grid_hash


class GenerateGridHashTests(unittest.TestCase):
    def test_maps_positive_coordinates_to_grid_cell(self):
        self.assertEqual(generate_grid_hash(17.4435, 78.3772), "17.0_78.0")

    def test_floors_negative_coordinates(self):
        self.assertEqual(generate_grid_hash(-1.2, -2.3), "-2.0_-3.0")

    def test_accepts_valid_custom_precision(self):
        self.assertEqual(generate_grid_hash(17.4, 78.3, precision=0.5), "17.0_78.0")

    def test_rejects_out_of_range_latitude(self):
        with self.assertRaisesRegex(ValueError, "Latitude"):
            generate_grid_hash(91, 78)

    def test_rejects_out_of_range_longitude(self):
        with self.assertRaisesRegex(ValueError, "Longitude"):
            generate_grid_hash(17, 181)

    def test_rejects_non_positive_precision(self):
        for precision in (0, -1):
            with self.subTest(precision=precision):
                with self.assertRaisesRegex(ValueError, "precision"):
                    generate_grid_hash(17, 78, precision)

    def test_rejects_non_finite_values(self):
        with self.assertRaisesRegex(ValueError, "finite"):
            generate_grid_hash(float("nan"), 78)


if __name__ == "__main__":
    unittest.main()
