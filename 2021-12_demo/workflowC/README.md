## Clinical real-world evidence: current drugs and potential new insights
See [slides in google drive](https://drive.google.com/drive/folders/1gQC9RhE6jxPWRHm7fMf4MPW3ewq-LH0i).

**Immune-mediated inflammatory diseases**

Dr. Sergio Baranzini, multiple sclerosis.

SME, Dr. Philip Mease, rheumatolgy

- **Query 1 (Explore):** Find **drugs** (SmallMolecule) related to **disease X** from real-world evidence
- **Query 2 (Explain & Expand):** For a SME-selected drug from Query 1 results, find **drugs** related to a **gene set** that is related to both (1) **disease X** and (2) the **SME-selected drug(s)**
- **Query 3 (Find More Knowledge):** For a SME-selected drug from Query 2, find associations between the drug and **disease X**

**Note:** Overlay edges can also provide research evidence (links to published papers) for final results

![image](https://user-images.githubusercontent.com/18222763/130814236-7721958b-6896-4b4c-92a9-517169b0202c.png)

## December Demo Narrative

The following provides a high-level narrative for walking through workflow C in the December demo. Note that this should be seen as a template narrative in which the specific disease example (in this case, multiple sclerosis) could be replaced by another disease of interest. By the time of the December demo, we should have two or more solid disease examples in which the narrative outlined below highlights some compelling results.

### Example narrative using multiple sclerosis as the disease of interest

For a disease of interest we would first like to identify drugs that are in some way associated with the disease, based on data from a clinical care setting. These could be drugs (1) used to directly treat the disease, (2) used to treat symptoms or comorbidities often associated with the disease, or possibly (3) drugs used for treating another condition, but which have the side effect of exacerbating the disease of interest.

As an example, say we are interested in drugs associated with multiple sclerosis. We could query Translator for this information as follows:

**Query C.1: Real world evidence on drugs for patient with multiple sclerosis**

[JSON](https://github.com/NCATSTranslator/minihackathons/blob/main/2021-12_demo/workflowC/C.1a_SmallMolecule_real_world_evidence_MultSclerosis.json)

[ARS result](https://arax.ncats.io/?r=f87a7926-50ab-4c5d-b021-9acdece57c47)

We could look at drugs commonly taken by patients with multiple sclerosis (most frequent drug is Tylenol). We want to see drugs that are more related to multiple sclerosis (MS), or unexpectedly used more often in patients with MS. EHRs do not have structured information on why a drug is being given, but Translator uses explainable machine learning at scale to support this.

Reviewing results from **Explanatory Agent**, you see several drugs commonly used in the treatment of multiple sclerosis:
   
 _-- See  disease-modifying drugs: fingolimod, ocrelizumab, natalizumab

We also see drugs that are used to treat symptoms or secondary conditions commonly seen in multiple sclerosis patients:

_-- See drugs used to treat symptoms, such as pain or muscle spasticity e.g. baclofen, tizanidine, gabapentin, oxybutynin_
    
A clinician reviewing these results will easily recognize these expected drugs. Other drugs may be more surprising. In some cases, these may be drugs that are used off-label for the disease or have been in clinical trials for repurposing, or were in the past.
 
_-- See imatinib_

Imatinib (Gleevec), designed to treat cancer, targeting the bcr-abl protein. Blocking PDGF-CC signaling ameliorates neuroinflammation by inhibiting disruption of the blood–brain barrier. However, case studies emerged where patients with MS experienced improvements during treatment. Clicking on this edge, we can see the evidence, provenance and context for this knowledge. This is from real world data for 10,000+ patients with multiple sclerosis and 10,000,000+ patients overall.

_-- See clevedipine_

Clicking on imatinib, we can see the evidence, provenance and context for this knowledge. This is from real world data from logistic regression analysis for 10,000+ patients with multiple sclerosis and 10,000,000+ patients overall (positive_cohort_order_of_magnitude, negative_cohort_order_of_magnitude). This goes beyond co-occurance (drugs that people with MS commonly take) to find drugs that are likely to be more specific to patients who have multiple sclerosis. This seems unsual. It's a dihydropyridine calcium channel blocker. We'll investigate this one too.

Now let's look at how Translator can conduct more complex queries, that would be impossible in PubMED, Google, or any single knowledge base. Let's ask about underlying pathways of action for imatinib, and get a list of drugs that may operate via similar pathways.

**Query C.2 Working earlier, returning soon**
 https://arax.ncats.io/beta/?r=846

Here is a set of genes (or pathways) that are associated with both multiple sclerosis and clevedipine. And here is a group of drugs that are associated with those genes/pathways.

Inspecting the drugs in **ARAX**, we see some interesting results.

_-- Click on nimodipine_
This is a dihydropyridine calcium channel blocker, invented for treating systemic hypertension. It prevent vasoconstriction in the smooth muscle cells of blood vessels, and has a preference to act on cerebral blood vessels since it is lipophilic and can cross the blood-brain barrier.

Translator can also provide additional information, such as references to published studies reporting evidence of associations between these drugs and the disease of interest. For example, here's a "research evidence" edge connecting nimodipine to multiple sclerosis. If we click on that edge, we get a list of PubMed IDs for papers that we can look at to understand the basis of these associations.

_-- CLick on a few PMIDs and highlight published research PMID #### (TBD)

**Query C.2 Current query**
https://arax.ncats.io/?r=8257a139-bb29-47ba-a86b-611e44d8b1b0
_-- Click on simvistatin

This is a statin used to lower cholesterol. It is, in fact being investigated in clinical trial. https://clinicaltrials.gov/ct2/show/NCT03896217.

**Query C.3**
We can also include the original disease and this drug of interest in a third query to see what additional knowledge Translator can provide.https://arax.ncats.io/?r=8a313286-e04d-44f2-9a92-c63abd7287b7

BTE: PMID:28381594
ARAX: PMID:32293054

**Query C.4, under construction**
From our SME, Dr.  Baranzini, we know that the there has been great advances in treating episodes of exacerbations, but not in stopping the underlying progressive demyelination on nerves. He is interested in drugs that interact with the myelination pathways (GO:0022010)
https://arax.ncats.io/?r=87c5366a-eb0f-4582-8d30-134aa0a95a8c

Note IGF (will connect to nimdipine).

**Query C.5, under construction, rare disease**
SME, Dr. Mease, Systemic Scleroris, Psoriasis, Psoriatic Arthritis
