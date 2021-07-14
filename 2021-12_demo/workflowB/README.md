# Workflow B: DILI Drug Repurposing

DILI (drug-induced liver injury) is a disease or condition with only one consensus treatment: discontinue the causal drug. DILI may resolve after discontinuation of drug; however, in some cases, the condition deterioriates or becomes chronic and may result in hospitalization, liver transplant, or other costly outcomes with high morbidity and mortality.

The intent of Workflow B is two-fold: 

1. Suggest drugs for repurposing, along with evidence of biological plausibility -> DILIN clinical trial (steroids? prednisone?)

- In natural language, one might ask *are there drugs that can be repurposed to treat phenotypes or traits associated with DILI?*

2. Suggest chemicals for liver-on-a-chip screening (or other *in vitro* screening assays), along with evidence of biological plausibility -> NCATS, NIEHS

- Similarly, in natural language, one might ask *are there chemical substances that may serve as drug targets for treatment of phenotypes or traits associated with DILI?*

For reference, here is the [workflow mural board](https://app.mural.co/t/ncats3030/m/ncats3030/1620608471364/d9d6ca5aefb8c7af4f756312d2500f0a3f465008), [pre-relay meeting materials](https://drive.google.com/drive/folders/1sCA6iouNHOh9I4ivXrR6DCct6fGgXbXp?usp=sharing), and [Spring 2021 relay meeting materials](https://github.com/ranking-agent/robogallery/tree/master/relay_spring_2021/DILI).

The workflow is structured as an initial three-hop TRAPI query that runs from input DiseaseOrPhenotypicFeature CURIE to DiseaseOrPhenotypicFeature to Gene to ChemicalSubstance (including approved drugs). An optional fourth hop then seeks clinical real-world evidence on whether any of the identified drugs are used to treat the traits or phenotypic features identified from the first hop, or other traits/diseases, or perhaps seek real-world clinical evidence on adverse events or risks associated with those drugs. Note that the fourth hop can be executed as a separate one-hop TRAPI query, perhaps after SME review of findings from the initial three-hop TRAPI query, or as a looped fourth hop.

Suggested input CURIES: DILI (MONDO:0005359), toxic liver disease with acute hepatitis (SNOMEDCT:197358007), chronic DILI (MESH:D056487), hospitalization (MESH:D006760), transplanted liver complication (NCIT:C26991).
