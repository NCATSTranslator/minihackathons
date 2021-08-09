# Purpose
The purpose of the EGFR workflow is to help a clinician find candidate drugs to treat neonatal inflammatory skin and bowel diseases caused by an overactive EGFR gene. Neonatal inflammatory skin and bowel disease is a rare, life-threatening, autoinflammatory syndrome with immune deficiency disorder characterized by early-onset, life-long inflammation affecting the skin and bowel and is associated with recurrent infections. This query came to us by way of UAB's Precision Medicine Institute.

# Query Notes
```
{"message":
    {"query_graph":
        {
          "nodes": {
            "n0": {
            #This is where we specify that we want our answer to be a chemical substance, e.g., a drug
              "categories": [
                "biolink:ChemicalSubstance"
              ],
              "name": "Chemical Substance",
              #This section imposes the constraint that we want to find ONLY substances that have already been FDA approved
              "constraints": [
                {
                    "id":"biolink:highest_FDA_approval_status",
                    "name":"highest FDA approval status",
                    "operator":"==",
                    "value":"regular approval"
                }
              ]
            },
            "n1": {
            #This is where we specify the gene of interest
              "name": "EGFR",
              "ids": ["NCBIGene:1956"]
            }
          },
          "edges": {
            "e0": {
              "subject": "n0",
              "object": "n1",
              #We want to know what decreases the activity of EGFR. This relationship is expressed in many different ways across different data sources. Here we 
              #gather together the relevant relationships and search across all of them.
              "predicates": [
                "biolink:decreases_abundance_of",
                "biolink:decreases_activity_of",
                "biolink:decreases_expression_of",
                "biolink:decreases_synthesis_of",
                "biolink:increases_degradation_of",
                "biolink:disrupts",
                "biolink:entity_negatively_regulates_entity"
              ]
            }
          }
        }
    }
}
```
