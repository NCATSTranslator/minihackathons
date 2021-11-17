# Clinical real-world evidence: current drugs and potential new insights

_Immune-mediated inflammatory diseases (IMIDs)_

[Slides in google drive](https://drive.google.com/drive/folders/1gQC9RhE6jxPWRHm7fMf4MPW3ewq-LH0i)

## Queries

1. **Drugs** known to treat or prevent **diseases XYZ**
2. Clinical real-world insights on **drugs** taken by patients with **diseases XYZ**
3. Investigate expert-recommended **candidate drugs for repurposing** for **disease Q** to look for connections with **gene pathway P**
4. Search more broadly for **drugs** used in the real world with patients with **diseases QRS** that are **connected to gene pathway P**
---
**Philip Mease, MD** is a rheumatologist who is working on immune-mediated inflammatory diseases (IMIDs) with an interdisciplinary team including gastroenterologists and data scientists. Team members want to learn more about the many-to-many maps between thousands of IMIDs and immunomodulatory drugs. **Systemic sclerosis** (sometimes called **scleroderma** ) is a spectrum of rare diseases related to excess collagen, which can lead to fibrosis of the skin, internal organs, or both.

### Query C1: MDs looking at drugs used for patients with IMIDs

ARS, [ARAX](https://arax.ncats.io/?r=32493), [JSON](https://github.com/NCATSTranslator/minihackathons/blob/main/2021-12_demo/workflowC/C1.json)

Literature shows a vast number of medications that may treat IMIDs. However, the team was interested in seeing real world use of drugs for patients with IMIDs: approved and off-label.

Structured EHR data does not track why a drug is prescribed treating because it is usually obvious to other clinicians, and any unusual treatments are only explained in free text notes. If you only look at drugs that co-occur with scleroderma, you&#39;ll see a vast list, starting with things like acetaminophen (Tylenol) because it&#39;s so common for patients in general.

Translator knowledge providers have developed techniques, including relative frequency and machine learning to derive knowledge about what drugs people are prescribed or administered that are **likely to be related** to a specific disease. These might be a disease modifying drugs, or medications that treats symptoms or secondary conditions related to the disease.

**Mycophenolate mofetil**
- **CREST syndrome**. Notice translator automatically mapped to subtypes of scleroderma, including this rare disease.
- **Systemic sclerosis:** Columbia Open Health Data (COHD), direct statistics: Chi squared and observed to expected ratio. **Multiomics** : Here&#39;s data from another knowledge provider. Note the **size of the population,** reported in **log** to avoid differential privacy attacks. Order of magnitude: Log 7 **10,000,000** patients, log 3, **1,000** with systemic sclerosis.
---
**Dr. Sergio Baranzini, PhD** is a biomedical expert in Multiple Sclerosis. There have been great advances in treating multiple sclerosis exacerbations, but not in stopping the underlying progressive demyelination on nerves. Dr. Baranzini is interested in drugs that interact with the central nervous systems (CNS) myelination gene pathways. A paper that came out this year included a list of eight candidates for drug repurposing for progressive multiple sclerosis. He would like to see whether/how these drugs connect with CNS myelination pathways.

### Query C2: Investigating whether drug repurposing candidates connect to CNS myelination

[ARS](https://arax.ncats.io/?r=a49d8280-724d-42cf-8b6e-14227f6fefd7), [alt ARS](https://arax.ncats.io/?r=f58348a7-4491-4bbc-bb44-50e8aae16590), [ARAX](https://arax.ncats.io/?r=31733), [JSON](https://github.com/NCATSTranslator/minihackathons/blob/main/2021-12_demo/workflowC/C2.json)

Aragorn or ARAX. Choose **clemastine**. Click on edge to STAT3. This is now in clinical trials for remyelination.

Choose **nimodipine**. Click on the edges to multiple sclerosis. SME thinks the mechanism of action makes sense. See nimodipine note on **PMID:28381594**. Nimodipine fosters remyelination in a mouse model

### Query C3: Investigation of potential candidates connected to CNS myelination

[ARS](https://arax.ncats.io/?r=c97d96f8-73fc-42cb-9d5f-5ec7e4cbc7f8), [alt ARS](https://arax.ncats.io/?r=cbbab5fd-8776-4563-99a5-2e7e95390b9c), [ARAX](https://arax.ncats.io/?r=32237), [JSON](https://github.com/NCATSTranslator/minihackathons/blob/main/2021-12_demo/workflowC/C3.json)

Translator independently finds both existing drugs and several that experts suggested: Metformin, clemastine, thioctic acid, niacin, tamoxifen. It does not find nimodipine in this query, but it found an alternate calcium channel blocker ( **nifedipine** ), and new evidence just came out in mouse models: [PMID 33709265](https://pubmed.ncbi.nlm.nih.gov/33709265).

The SME is intrigued by **quercetin** (plant-based), and **dasatinib** (a tyrosine kinase inhibitor) and will
