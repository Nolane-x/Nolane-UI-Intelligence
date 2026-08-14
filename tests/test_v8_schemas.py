import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class V8SchemaTests(unittest.TestCase):
    def test_all_v8_schemas_exist_and_parse(self):
        for rel in (
            'schemas/agent-interop.schema.json',
            'schemas/asset-provenance-ledger.schema.json',
            'schemas/external-skill-trust.schema.json',
            'schemas/visual-media-plan.schema.json',
            'schemas/creative-toolchain.schema.json',
            'schemas/visual-asset-integration.schema.json',
        ):
            path=ROOT/rel
            self.assertTrue(path.is_file(),rel)
            self.assertIsInstance(json.loads(path.read_text(encoding='utf-8')),dict,rel)

if __name__=='__main__': unittest.main()
