import unittest


class UXV2StatusTests(unittest.TestCase):
    def test_status_exposes_integrity_dimensions(self):
        from nolane_ui.ux_intelligence import ux_v2_status

        status = ux_v2_status()
        self.assertTrue(status["valid"])
        self.assertIn("bridge_valid", status)
        self.assertIn("provenance_valid", status)
        self.assertIn("evaluator_valid", status)
        self.assertIn("unresolved_bridge_skills", status)
        self.assertIn("unresolved_evaluator_rules", status)
        self.assertEqual(status["unresolved_bridge_skills"], [])
        self.assertEqual(status["unresolved_evaluator_rules"], [])


if __name__ == "__main__":
    unittest.main()
