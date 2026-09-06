import unittest


class UXProvenanceTests(unittest.TestCase):
    def test_records_have_transfer_boundaries_and_contraindications(self):
        from nolane_ui.ux_intelligence import UX_PROVENANCE

        self.assertTrue(UX_PROVENANCE)
        for record in UX_PROVENANCE:
            self.assertTrue(record["transfer_boundaries"])
            self.assertTrue(record["contraindications"])
            self.assertTrue(record["verification_modes"])

    def test_missing_id_returns_none_and_queries_are_defensive(self):
        from nolane_ui.ux_intelligence import get_ux_provenance, query_ux_provenance

        self.assertIsNone(get_ux_provenance("missing"))
        rows = query_ux_provenance(limit=1)
        self.assertTrue(rows)
        rows[0]["title"] = "mutated"
        self.assertNotEqual(query_ux_provenance(limit=1)[0]["title"], "mutated")

    def test_query_limit_rejects_bool_and_out_of_range(self):
        from nolane_ui.ux_intelligence import query_ux_provenance

        with self.assertRaises(TypeError):
            query_ux_provenance(limit=True)
        with self.assertRaises(ValueError):
            query_ux_provenance(limit=0)
        with self.assertRaises(ValueError):
            query_ux_provenance(limit=101)


if __name__ == "__main__":
    unittest.main()
