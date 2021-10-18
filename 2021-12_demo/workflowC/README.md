## Clinical real-world evidence: current drugs and potential new insights
See this [google drive folder](https://drive.google.com/drive/folders/1gQC9RhE6jxPWRHm7fMf4MPW3ewq-LH0i).

Our SME, Dr.  Baranzini, researches multiple sclerosis.

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

**Query C.1** https://arax.ncats.io/?r=f9c78f7b-1f5e-455a-9f5f-e260fb283b49

Reviewing results from **Explanatory Agent**, you see several drugs commonly used in the treatment of multiple sclerosis:
   
 _-- See  disease-modifying drugs: fingolimod, ocrelizumab, natalizumab

We also see drugs that are used to treat symptoms or secondary conditions commonly seen in multiple sclerosis patients:

_-- See drugs used to treat symptoms, such as pain or muscle spasticity e.g. baclofen, tizanidine, gabapentin, oxybutynin_
    
A clinician reviewing these results will easily recognize these expected drugs. Other drugs may be more surprising. In some cases, these may be drugs that are used off-label for the disease or have been in clinical trials for repurposing, or were in the past.
 
_-- See imatinib_

Imatinib (Gleevec), designed to treat cancer, targeting the bcr-abl protein. However, case studies emerged where patients with MS experienced improvements during treatment.

Clicking on imatinib, we can see the evidence, provenance and context for this knowledge. This is from real world data for 10,000+ patients with multiple sclerosis and 10,000,000+ patients overall. This goes beyond co-occurance (drugs that people with MS commonly take) to find drugs that are likely to be more specific to patients who have multiple sclerosis.

Let's look at how Translator can conduct more complex queries, that would be impossible in PubMED, Google, or any single knowledge base. Let's ask about underlying pathways of action for imatinib, and get a list of drugs that may operate via similar pathways.

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

**Query C.4**
From our SME, Dr.  Baranzini, we know that the there has been great advances in treating episodes of exacerbations, but not in stopping the underlying progressive demyelination on nerves. He is interested in drugs that interact with the myelination pathways (GO:0022010)
https://arax.ncats.io/?r=87c5366a-eb0f-4582-8d30-134aa0a95a8c
