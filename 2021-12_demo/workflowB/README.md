# Workflow B: DILI Drug Repurposing

DILI (drug-induced liver injury) is a rare disease or condition with only one consensus treatment: discontinuation of the causal agent. While DILI may resolve after discontinuation of the causal agent, complete resolution may require months or years and, in many cases, the condition deterioriates before resolving and/or becomes chronic. Moreover, DILI is associated with high healthcare costs and high morbidity and mortality, leading to hospitalization, liver transplant, and other poor outcomes.

The intent of Workflow B is two-fold: 

1. Suggest drugs for repurposing, along with evidence of biological plausibility -> DILIN clinical trial

* In natural language, one might ask *are there drugs that can be repurposed to treat phenotypes or traits or outcomes associated with DILI?*

2. Suggest chemicals for liver-on-a-chip screening (or other *in vitro* screening assays), along with evidence of biological plausibility -> NCATS, NIEHS

* Similarly, in natural language, one might ask *are there chemical substances that may serve as drug targets for development of new treatments for phenotypes or traits or outcomes associated with DILI?*

For reference, here is the [workflow mural board](https://app.mural.co/t/ncats3030/m/ncats3030/1620608471364/d9d6ca5aefb8c7af4f756312d2500f0a3f465008), [pre-relay meeting materials](https://drive.google.com/drive/folders/1sCA6iouNHOh9I4ivXrR6DCct6fGgXbXp?usp=sharing), and [Spring 2021 relay meeting materials](https://github.com/ranking-agent/robogallery/tree/master/relay_spring_2021/DILI). Also see mini-hackathon issues #43, #44, #45, #46, #48, and #49.

The workflow is structured as an initial three-hop TRAPI query that runs from input DiseaseOrPhenotypicFeature CURIE to DiseaseOrPhenotypicFeature to Gene to ChemicalSubstance (including approved drugs). A fourth hop then seeks clinical real-world evidence on whether any of the suggested approved drugs are used to treat (biolink:correlated_with, biolink:related_to, etc) the diseases or phenotypic features identified from the first hop, or whether they are used to treat (biolink:correlated_with, biolink:realted_to, etc.) other potentially related traits/diseases, or whether they are associated with adverse events. The fourth hop is intended to provided real-world evidence that might assist with ranking/sorting of answers and/or SME evaluation of results from the third hop. Note that the fourth hop can be executed as a separate one-hop TRAPI query, perhaps after SME review of findings from the initial three-hop TRAPI query, or as a looped fourth hop.

Suggested input CURIES for three- or four-hop TRAPI queries from DiseaseOrPhenotypicFeature:

* DILI - MONDO:0005359
* Toxic liver disease with acute hepatitis - SNOMEDCT:197358007
* Chronic DILI - MESH:D056487
* Hospitalization - MESH:D006760
* Transplanted liver complication - NCIT:C26991

Suggested input CURIES for one-hop TRAPI query from Gene:

* class I HLA-A - NCBIGene:3105
* class I HLA-B - NCBIGene:3106
* ERAP2 - NCBIGene:64167
* EXOC4 - NCBIGene:60412
* PTPN22 - NCBIGene:26191
