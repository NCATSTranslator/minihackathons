# Workflow D: EXPLAIN
This workflow is designed to demonstrate the Translator's abilitiy to explain a biological phenomenon or observation by filling in
missing pieces of a possible mechaistic causal chain that connected the two concepts observed to be associated. Currenly, queries assume a particulr struture of the explanantion, embodied by the query graph (in the future ientifyng the best query graph will be part of the task by the Translator)
The four initial queries for a first round of testing (strating July 2021) seek to answer the following questions:

D.1. Why do Crohn disease patients have a higher risk to develop
Parkinson’s disease?

D.2. Why do SSRI (a group of anti-depressants) have cardio-protective
effect?

D.4. Why are serum kynurenine and tryptophan in COVID-19 patients
anti-correlated?

D.6. A patient has very high ferritin levels and a biotech contact says
that metformin may lower ferritin. Can we determine why?

(D.3 and D.5 are alternative TRAPI queries of D.2. ad D.4, respectively)

These queries were reverse-engineered from known or possible answers, determined by literature or the neighborhood explorer
tool that gives GUI access to (SPOKE)[https://spoke.rbvi.ucsf.edu/], and may need to be broken down into step-wise queries for a realistic
Translator workflow since there is no operation yet to "connect the dots witout specified qgraph structure"
