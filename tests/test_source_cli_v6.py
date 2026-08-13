import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SourceCLIV6Tests(unittest.TestCase):
    def test_source_plan_emits_role_specific_obligations(self):
        source = {"id":"react-bits","role":"animated-component-gallery","drift":"very-high","verify_live_before_use":True,"url":"https://github.com/DavidHDev/react-bits"}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(source, f); path=f.name
        run = subprocess.run([sys.executable, str(ROOT/'scripts/nui-source-plan'), '--source', path, '--usage','adapt','--visual-ambition','exceptional'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(run.returncode,0,run.stderr)
        result=json.loads(run.stdout)
        kinds={o['artifact_class'] for o in result['obligations']}
        self.assertIn('component-source', kinds)
        self.assertIn('accessibility-fallback', kinds)
        self.assertTrue(result['snapshot_required'])

    def test_source_audit_returns_nonzero_for_readme_only(self):
        dossier={"source_id":"x","source_role":"animated-component-gallery","usage":"adapt","snapshot":{"canonical_url":"https://example.com/x","ref":"main","commit_sha":"abcdef1","retrieved_at":"2026-08-13"},"task_fit":{"need":"x","why_this_source":"x","source_role_fit":True},"inspected_artifacts":[{"kind":"readme","path":"README.md","finding":"x","evidence_ref":"x"},{"kind":"license","path":"LICENSE","finding":"x","evidence_ref":"y"}],"mechanisms":[],"license":{"evidence_refs":["y"]},"accessibility":{"evidence_refs":["x"]},"performance":{"evidence_refs":["x"]},"unread_material":[],"stop_reason":"x"}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(dossier,f); path=f.name
        run=subprocess.run([sys.executable,str(ROOT/'scripts/nui-source-audit'),path],cwd=ROOT,text=True,capture_output=True)
        self.assertEqual(run.returncode,2)
        result=json.loads(run.stdout)
        self.assertFalse(result['valid'])
        self.assertTrue(any('README-only' in e for e in result['errors']))

    def test_source_audit_accepts_deep_dossier(self):
        dossier={"source_id":"icons","source_role":"icon-system","usage":"inspire","visual_ambition":"flagship","snapshot":{"canonical_url":"https://github.com/lucide-icons/lucide","ref":"main","retrieved_at":"2026-08-13"},"task_fit":{"need":"coherent icon grammar","why_this_source":"broad consistent symbol system","source_role_fit":True},"inspected_artifacts":[{"kind":"readme","path":"README.md","finding":"scope","evidence_ref":"r"},{"kind":"mechanism-bearing-evidence","path":"icons/airplay.svg","finding":"stroke grammar","evidence_ref":"m"},{"kind":"icon-catalog","path":"icons","finding":"coverage","evidence_ref":"c"},{"kind":"symbol-conventions","path":"CONTRIBUTING.md","finding":"construction rules","evidence_ref":"s"},{"kind":"accessibility-guidance","path":"docs/accessibility.md","finding":"label semantics","evidence_ref":"a"},{"kind":"naming-tags","path":"tags.json","finding":"semantic discovery taxonomy","evidence_ref":"t"},{"kind":"framework-delivery","path":"packages/lucide-react","finding":"React delivery boundary","evidence_ref":"f"},{"kind":"license","path":"LICENSE","finding":"reuse terms","evidence_ref":"l"}],"mechanisms":[{"name":"consistent stroke grammar","evidence_artifact_paths":["icons/airplay.svg","CONTRIBUTING.md"],"transfer_boundary":"learn construction rhythm, preserve local semantics","product_fit":"supports coherent product iconography"}],"unread_material":[],"stop_reason":"construction grammar and semantic boundary characterized"}
        with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as f:
            json.dump(dossier,f); path=f.name
        run=subprocess.run([sys.executable,str(ROOT/'scripts/nui-source-audit'),path],cwd=ROOT,text=True,capture_output=True)
        self.assertEqual(run.returncode,0,run.stdout+run.stderr)
        self.assertTrue(json.loads(run.stdout)['valid'])

if __name__=='__main__': unittest.main()
