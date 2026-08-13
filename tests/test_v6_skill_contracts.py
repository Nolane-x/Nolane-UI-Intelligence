import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from nolane_ui.source_intelligence import mandatory_v6_source_routes

NEW={
 'performing-ui-repository-archaeology':('researching-ui-implementation-ecosystems','ui-source-research-dossier'),
 'synthesizing-cross-source-ui-language':('selecting-ui-building-blocks','ui-cross-source-synthesis'),
 'auditing-ui-research-depth':('critiquing-research-validity','ui-research-depth-findings'),
 'benchmarking-ui-skill-effect':('testing-skill-interactions','ui-skill-effect-benchmark'),
}

class V6SkillContractsTests(unittest.TestCase):
    def test_manifest_and_graph_declare_exact_four_new_owners(self):
        manifest=json.loads((ROOT/'knowledge/v6-skill-manifest.json').read_text())
        graph=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']
        self.assertEqual({x['name'] for x in manifest['skills']},set(NEW))
        for name,(parent,output) in NEW.items():
            self.assertIn(name,graph)
            self.assertEqual(graph[name]['parent'],parent)
            self.assertEqual(graph[name]['output'],output)
            text=(ROOT/'skills'/name/'SKILL.md').read_text()
            self.assertIn('Hard gate',text)
            self.assertIn('falsif',text.lower())
            self.assertIn('recovery',text.lower())

    def test_outputs_are_unique_across_graph(self):
        graph=json.loads((ROOT/'skills/skill-graph.json').read_text())['skills']
        outputs=[graph[n]['output'] for n in NEW]
        self.assertEqual(len(outputs),len(set(outputs)))
        for name in NEW:
            self.assertTrue(graph[name].get('ownership'))

    def test_material_external_influence_hard_routes_archaeology_and_research_audit(self):
        routes=mandatory_v6_source_routes({'external_source_usage':'adapt','external_source_count':1,'visual_ambition':'exceptional'})
        self.assertIn('performing-ui-repository-archaeology',routes)
        self.assertIn('auditing-ui-research-depth',routes)

    def test_multiple_material_sources_route_synthesis(self):
        routes=mandatory_v6_source_routes({'external_source_usage':'adapt','external_source_count':3})
        self.assertIn('synthesizing-cross-source-ui-language',routes)

    def test_skill_effect_evaluation_routes_benchmark_owner(self):
        routes=mandatory_v6_source_routes({'skill_effect_evaluation':True})
        self.assertIn('benchmarking-ui-skill-effect',routes)

if __name__=='__main__': unittest.main()
