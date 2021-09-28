## Clinical real-world evidence: current drugs and potential new insights
See this [google drive folder](https://drive.google.com/drive/folders/1gQC9RhE6jxPWRHm7fMf4MPW3ewq-LH0i).

- **Query 1 (Explore):** Find **drugs** (SmallMolecule) related to **disease X**
- **Query 2 (Explain & Expand):** For 1 or more SME-selected drugs from the Query 1 results, find **drugs** related to a **gene set** that is related to both (1) **disease X** and (2) the **SME-selected drug(s)**
- **Query 3 (Find Research Evidence):** For 1 or more drug results from Query 2, find any associations between the drug and **disease X**

**Note:** Overlay edges can also provide research evidence (links to published papers) for final results

![image](https://user-images.githubusercontent.com/18222763/130814236-7721958b-6896-4b4c-92a9-517169b0202c.png)

## December Demo Narrative

The following provides a high-level narrative for walking through workflow C in the December demo. Note that this should be seen as a template narrative in which the specific disease example (in this case, multiple sclerosis) could be replaced by another disease of interest. By the time of the December demo, we should have two or more solid disease examples in which the narrative outlined below highlights some compelling results.

### Example narrative using multiple sclerosis as the disease of interest

For a disease of interest we would first like to identify drugs that are in some way associated with the disease, based on data from a clinical care setting. These could be drugs (1) used to directly treat the disease, (2) used to treat symptoms or comorbidities often associated with the disease, or possibly (3) drugs used for treating another condition, but which have the side effect of exacerbating the disease of interest.

As an example, say we are interested in drugs associated with multiple sclerosis. We could query Translator for this information as follows:

[_Run query C.1 (or view results previously obtained) using multiple scelerosis as the disease of interest_]

Reviewing results, we see several drugs commonly used in the treatment of multiple sclerosis:

[_Point out examples of drugs used to treat the disease e.g. ocrelizumab, natalizumab_]

We also see drugs that are used to treat symptoms or secondary conditions commonly seen in multiple sclerosis patients:

[_Point out examples of drugs used to treat symptoms, such as pain or muscle spasticity e.g. baclofen, tizanidine, gabapentin, oxybutynin_]

A clinician reviewing these results will easily recognize these expected drugs. Other drugs may be more surprising. In some cases, these may be drugs that are used off-label for the disease or have been in clinical trials for repurposing.

[_Point out examples e.g. imatinib_]

What if Translator could (1) provide information about underlying pathways of action for such drugs (e.g. via specific gene products) and (2) identify an expanded list of drugs that may operate via similar pathways. We can run such a query.

[_Run query C.2 (or view results previously obtained) using natalizumab, imatinib, or another interesting drug_]

Here is a set of genes (or pathways) that are associated with both multiple sclerosis and the drug(s) that we selected from the first query. And here is a group of drugs that are associated with those genes/pathways. Inspecting the drugs, we see some interesting results. Let's look at <_interesting drug such as atorvastatin_>.

[_Highlight some of the drugs in the final group that are interesting (might also highlight some of the genes/pathways)_]

Translator also has an "overlay" feature that can provide additional "provenance" or source information, such as references to published studies reporting evidence of associations between these drugs and the disease of interest. For example, here's a "research evidence" edge connecting the drug <_interesting drug from final results_> to multiple sclerosis. If we click on that edge, we get a list of PubMed IDs for papers that we can look at to understand the basis of these associations.

[_Click on a few PMIDs and highlight some of the published research results_]

We can also include the original disease and this drug of interest in a third query to see what additional associations and research evidence Translator can provide.

[_Run query C.3 (or view results previously obtained) using multiple sclerosis and atorvastatin_]

Emphasize that we could follow a similar investigative/exploratory workflow with other diseases besides multiple sclerosis.

[_Possibly briefly highlight interesting results already generated for other diseases: Systemic Scleroderma, Ehlers-Danlos, Meniere_]

## Example Using Multiple Sclerosis as Disease X

### Query 1: SmallMolecule has_real_world_evidence_of_association_with MONDO:0005301

Results: https://arax.ncats.io/?r=27565

```
{
    "message": {
        "query_graph": {
            "nodes": {
                "n00": {
                    "categories": [
                        "biolink:Disease"
                    ],
                    "ids": [
                        "MONDO:0005301"
                    ],
                    "is_set": false,
                    "constraints": []
                },
                "n01": {
                    "categories": [
                        "biolink:SmallMolecule"
                    ],
                    "is_set": false,
                    "constraints": []
                }
            },
            "edges": {
                "e00": {
                    "subject": "n00",
                    "object": "n01",
                    "predicates": [
                        "biolink:has_real_world_evidence_of_association_with"
                    ],
                    "constraints": [],
                    "exclude": false
                }
            }
        }
    }
}
```

### Query 2: SmallMolecule interacts_with MS/natalizumab Genes

Results: https://arax.ncats.io/?r=27108

```
{
    "workflow": [
        {
            "id": "fill"
        },
        {
            "id": "bind"
        },
        {
            "id": "overlay_compute_ngd",
            "parameters": {
                "virtual_relation_label": "N1",
                "qnode_keys": [
                    "n3",
                    "n1"
                ]
            }
        },
        {
            "id": "overlay_compute_ngd",
            "parameters": {
                "virtual_relation_label": "N2",
                "qnode_keys": [
                    "n2",
                    "n3"
                ]
            }
        },
        {
            "id": "complete_results"
        },
        {
            "id": "filter_results_top_n",
            "parameters": {
                "max_results": 500
            }
        }
    ],
    "message": {
        "query_graph": {
            "nodes": {
                "n0": {
                    "categories": [
                        "biolink:Gene"
                    ],
                    "is_set": true,
                    "constraints": []
                },
                "n1": {
                    "ids": [
                        "CHEMBL.COMPOUND:CHEMBL1201607"
                    ],
                    "categories": [
                        "biolink:SmallMolecule"
                    ],
                    "is_set": false,
                    "constraints": []
                },
                "n2": {
                    "ids": [
                        "MONDO:0005301"
                    ],
                    "categories": [
                        "biolink:Disease"
                    ],
                    "is_set": false,
                    "constraints": []
                },
                "n3": {
                    "categories": [
                        "biolink:SmallMolecule"
                    ],
                    "is_set": false,
                    "constraints": []
                }
            },
            "edges": {
                "e01": {
                    "predicates": [
                        "biolink:interacts_with"
                    ],
                    "subject": "n0",
                    "object": "n1",
                    "constraints": [],
                    "exclude": false
                },
                "e02": {
                    "predicates": [
                        "biolink:genetic_association"
                    ],
                    "subject": "n0",
                    "object": "n2",
                    "constraints": [],
                    "exclude": false
                },
                "e03": {
                    "predicates": [
                        "biolink:interacts_with"
                    ],
                    "subject": "n0",
                    "object": "n3",
                    "constraints": [],
                    "exclude": false
                }
            }
        }
    }
}
```

### Query 3: Multiple sclerosis related_to atorvastatin

Results: https://arax.ncats.io/?r=b7a43315-377e-40c9-9f6b-c92a8295f7d2

```
{
    "message": {
        "query_graph": {
            "nodes": {
                "n00": {
                    "categories": [
                        "biolink:Disease"
                    ],
                    "ids": [
                        "MONDO:0005301"
                    ],
                    "is_set": false,
                    "constraints": []
                },
                "n01": {
                    "categories": [
                        "biolink:SmallMolecule"
                    ],
                    "ids": [
                        "CHEMBL.COMPOUND:CHEMBL1487"
                    ],
                    "is_set": false,
                    "constraints": []
                }
            },
            "edges": {
                "e00": {
                    "subject": "n00",
                    "object": "n01",
                    "predicates": [
                        "biolink:related_to"
                    ],
                    "constraints": [],
                    "exclude": false
                }
            }
        }
    }
}
```