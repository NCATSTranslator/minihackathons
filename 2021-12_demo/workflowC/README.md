## Overall Workflow
See this [google drive folder](https://drive.google.com/drive/folders/1PHpGOQdikLvnLBVEnTsRwlMNYObtQ1lo) (specifically, these [google slides](https://docs.google.com/presentation/d/1D7DkFW5kQe45DBOQP_m_kka3obGQdTm8AdnU_Akel0c/edit#slide=id.ge177b547c0_0_0))

- **Query 1:** Find **drugs** (ChemicalSubstance) related to **disease X**
- **Query 2:** For 1 or more SME-selected drugs from Query 1, find **drugs** related to a **gene set** that is related both to (1) **disease X** and to (2) the **SME-selected drug(s)**

![image](https://user-images.githubusercontent.com/18222763/124309535-b4e04d80-db1f-11eb-9ffb-f6467a79f29f.png)

## Example Using Multiple Sclerosis as Disease X
### Query 1: ChemicalSubstances related_to MONDO:0005301

The TRAPI query, immediately below, returns **drugs** related to **multiple sclerosis**. Using the ARAX DSL, it is possible to target specific KPs (for example clinical KPs) for more domain-specific knowledge (see DSL Query A, below). This can be further refined by querying a single, specific KP and sorting results based on an edge property (see DSL Query B, below).

**TRAPI 1.1 Query**
Submitted to: https://ars-dev.transltr.io/ars/api/submit
ARS pk: 9434d84a-0977-41db-8fd4-94292b866b97
ARAX results: https://arax.ncats.io/?r=12169

```
{
    "message": {
        "query_graph": {
            "edges": {
                "e00": {
                    "subject": "n00",
                    "object": "n01",
                    "predicates": ["biolink:related_to"]
                }
            },
            "nodes": {
                "n00": {
                    "categories": ["biolink:ChemicalSubstance"]
                },
                "n01": {
                    "categories": ["biolink:Disease"],
                    "ids": ["MONDO:0005301"]
                }
            }
        }
    }
}
```

**ARAX DSL Query A**
The following query specifically targets COHD and Clinical Risk KPs. Results: https://arax.ncats.io/?r=12173.

```
add_qnode(ids=MONDO:0005301, key=n00)
add_qnode(categories=biolink:ChemicalSubstance, key=n01)
add_qedge(subject=n01, object=n00, key=e00, predicates=biolink:related_to)
expand(kp=COHD,edge_key=e00,continue_if_no_results=false,use_synonyms=true,COHD_method=paired_concept_freq,COHD_method_percentile=90)
expand(kp=ClinicalRiskKP, edge_key=e00)
overlay(action=compute_ngd, virtual_relation_label=N1, subject_qnode_key=n01, object_qnode_key=n00)
resultify()
```

**ARAX DSL Query B**
The following query specifically targets the Clinical Risk KP, sorting by the feature_coefficient edge property, and limiting to only the top 30 results. Results: https://arax.ncats.io/?r=12174.

```
add_qnode(ids=MONDO:0005301, key=n00)
add_qnode(categories=biolink:ChemicalSubstance, key=n01)
add_qedge(subject=n01, object=n00, key=e00, predicates=biolink:related_to)
expand(kp=ClinicalRiskKP, edge_key=e00)
overlay(action=compute_ngd, virtual_relation_label=N1, subject_qnode_key=n01, object_qnode_key=n00)
resultify()
filter_results(action=sort_by_edge_attribute, edge_attribute=feature_coefficient, direction=descending, max_results=30, prune_kg=true)
```

### Query 2: ChemicalSubstances related_to MS/imatinib Genes

The TRAPI query, immediately below, is meant to return **drugs** related to a **set of genes** that are related to both (1) **multiple sclerosis** and (2) a single SME-selected drug (from ARAX DSL Query B results, above), **imatinib**. Without operations and other advanced features yet supported by TRAPI, ARS, and some ARAs, the query is under-constrained and does not yield results. However, taking advantage of such features supported by ARAX, results are obtainable using an ARAX DSL query (see DSL Query, below).

**TRAPI 1.1 Query**
Submitted to: https://ars-dev.transltr.io/ars/api/submit
ARS pk: ec03a9bb-af05-4bf3-a57d-f196c02c858b

```
{
    "message": {
        "query_graph": {
            "nodes": {
                "n0": {
                    "categories": ["biolink:Gene"]
                },
                "n1": {
                    "ids": ["CHEBI:45783"],
                    "categories": ["biolink:ChemicalSubstance"]
                },
                "n2": {
                    "ids": ["MONDO:0005301"],
                    "categories": ["biolink:Disease"]
                },
                "n3": {
                    "categories": ["biolink:ChemicalSubstance"]
                }
            },
            "edges": {
                "e01": {
                    "subject": "n0",
                    "object": "n1",
                    "predicates": ["biolink:related_to"]
                },
                "e02": {
                    "subject": "n0",
                    "object": "n2",
                    "predicates": ["biolink:related_to"]
                },
                "e03": {
                    "subject": "n0",
                    "object": "n3",
                    "predicates": ["biolink:related_to"]
                }
            }
        }
    }
}
```

**ARAX DSL Query**
The following query takes advantage of operations and other advanced features currently supported by ARAX. Results: https://arax.ncats.io/?r=12175.

```
add_qnode(key=n0, categories=biolink:Gene, is_set=True)
add_qnode(key=n1, ids=CHEBI:45783, categories=biolink:ChemicalSubstance)
add_qedge(key=e01, subject=n0, object=n1, predicates=biolink:related_to)
add_qnode(key=n2, ids=MONDO:0005301, categories=biolink:Disease)
add_qedge(key=e02, subject=n0, object=n2, predicates=biolink:related_to)
add_qnode(key=n3, categories=biolink:ChemicalSubstance)
add_qedge(key=e03, subject=n0, object=n3, predicates=biolink:related_to)
expand()
overlay(action=compute_jaccard,start_node_key=n1,intermediate_node_key=n0,end_node_key=n3,virtual_relation_label=J1)
overlay(action=compute_jaccard,start_node_key=n2,intermediate_node_key=n0,end_node_key=n3,virtual_relation_label=J2)
overlay(action=compute_ngd,default_value=inf,virtual_relation_label=N1,subject_qnode_key=n3,object_qnode_key=n2)
overlay(action=compute_ngd,default_value=inf,virtual_relation_label=N2,subject_qnode_key=n3,object_qnode_key=n1)
resultify()
filter_results(action=limit_number_of_results, max_results=50, prune_kg=true)
```

### Query 2 Other Results
The following is a list of drugs from Query 1. Links, below, are to Query 2 results using the respective drug. Also included for each is the number of genes (common to the drug and to multiple sclerosis) in the knowledge graph.
- natalizumab (CHEMBL.COMPOUND:CHEMBL1201607) - https://arax.ncats.io/?r=15406 (17 genes)
- ocrelizumab (CHEMBL.COMPOUND:CHEMBL2108041) - https://arax.ncats.io/?r=15411 (0 results)
- baclofen (CHEMBL.COMPOUND:CHEMBL701) - https://arax.ncats.io/?r=15412 (26 genes)
- clevidipine (CHEMBL.COMPOUND:CHEMBL1237132) - https://arax.ncats.io/?r=15413 (0 results)
- amikacin (CHEMBL.COMPOUND:CHEMBL177) - https://arax.ncats.io/?r=15414 (5 genes)
- gadobutrol (CHEMBL.COMPOUND:CHEMBL2218860) - https://arax.ncats.io/?r=15415 (0 results)
- carboprost tromethamine (CHEMBL.COMPOUND:CHEMBL1237105) - https://arax.ncats.io/?r=15416 (0 results)
- trastuzumab (CHEMBL.COMPOUND:CHEMBL1201585) - https://arax.ncats.io/?r=15418 (200 genes)
- cefotaxime sodium (CHEMBL.COMPOUND:CHEMBL1010) - https://arax.ncats.io/?r=15419 (22 genes)
- oxybutynin (CHEMBL.COMPOUND:CHEMBL1231) - https://arax.ncats.io/?r=15420 (8 genes)
- tizanidine (CHEMBL.COMPOUND:CHEMBL1079) - https://arax.ncats.io/?r=15421 (3 genes)
- methylphenidate (CHEMBL.COMPOUND:CHEMBL796) - https://arax.ncats.io/?r=15422 (15 genes)
- phenol (CHEMBL.COMPOUND:CHEMBL14060) - https://arax.ncats.io/?r=15423 (30 genes)
- methylprednisolone (CHEMBL.COMPOUND:CHEMBL650) - https://arax.ncats.io/?r=15424 (34 genes)
- imatinib (CHEMBL.COMPOUND:CHEMBL941) - https://arax.ncats.io/?r=15427 (163 genes)
- thrombin (CHEMBL.COMPOUND:CHEMBL2108110) - https://arax.ncats.io/?r=15430 (146 genes)
- atropine sulfate (CHEMBL.COMPOUND:CHEMBL2146146) - https://arax.ncats.io/?r=15431 (94 genes)
- meperidine (CHEMBL.COMPOUND:CHEMBL607) - https://arax.ncats.io/?r=15435 (14 genes)
- heparin (CHEBI:28304) - https://arax.ncats.io/?r=15436 (250+ genes)
- ropinirole (CHEMBL.COMPOUND:CHEMBL589) - https://arax.ncats.io/?r=15437 (8 genes)