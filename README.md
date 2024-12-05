1. Get relevant coding regions.
    a. We have 31 pre covid samples, 3 per year from 2010-2019, plus 1 from 2021.
    b. We have 13 during covid samples, 3 from 2021, and 2 per month from January-May of 2022
    c. We have 13 post covid samples, 5 from 2023 and 8 from 2022

2. Align them with MAFFT at the codon level. This didn't change the structure, which makes
sense because we only got the full protein-encoding regions. Better safe than sorry.

3. Partition this aligned file into 3 files with the python script

4. Created xml file for BEAST. Below is my process and the parameters I chose for reference/debate. I I downloaded beast with conda. Did command conda activate beast, then beauti to access beauti gui. Import the 3 files. We can link or unlink models, which means that the partitions share or don't share the models. The substitution model tells us the rleative rates and patterns of different types of substitutions. (i.e. dtails about what regions are evolving most, and in what way). I think unlink all them,since covid-caused evolutionary pressures may have put more pressure on specific regions/functionality, and post-coivd vaccine hesitancy may have caused less evolutionary pressure on surface identifiers. The clock model gives us total mutation rate. The tree model tells us phylogenetic stuff, which should be linked, since we want to compare the phylogeneteic data as a whole. For tips naming, make regex portin '\d\d\d\d-\d\d-\d\d' (without parentheses), then set to parse as calendar date with default argument, then specify origin date to 0. Clock should be random local for all. For MCMC, make length of chain 3 million and have file name stems be flu-strains.

