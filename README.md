1. Get relevant coding regions.
    a. We have 31 pre covid samples, 3 per year from 2010-2019, plus 1 from 2021.
    b. We have 13 during covid samples, 3 from 2021, and 2 per month from January-May of 2022
    c. We have 13 post covid samples, 5 from 2023 and 8 from 2022

2. Align them with MAFFT at the codon level. This didn't change the structure, which makes
sense because we only got the full protein-encoding regions. Better safe than sorry.

3. Partition this aligned file into 3 files with the python script

4. Created xml file for BEAST. Below is my process and the parameters I chose for reference/debate. I I downloaded beast with conda. Did command conda activate beast, then beauti to access beauti gui. Import the 3 files. We can link or unlink models, which means that the partitions share or don't share the models. The substitution model tells us the rleative rates and patterns of different types of substitutions. (i.e. dtails about what regions are evolving most, and in what way). I think unlink all them,since covid-caused evolutionary pressures may have put more pressure on specific regions/functionality, and post-coivd vaccine hesitancy may have caused less evolutionary pressure on surface identifiers. The clock model gives us total mutation rate. The tree model tells us phylogenetic stuff, which should be linked, since we want to compare the phylogeneteic data as a whole. But there is no option to do that given our other parameters, so it is unlinked. No big deal I think. For tips naming, make regex portin '\d\d\d\d-\d\d-\d\d' (without parentheses), then set to parse as calendar date with default argument, then specify origin date to 0. Clock should be random local for all. For MCMC, make length of chain 3 million and have file name stems be flu-strains. I created a tree substitution file and opeartor analysis file. Then I saved the file and ran it in the beast gui.

5. Ran beast. Took an hour and a half. Downloaded tracer (dowloaded tracer tar file from github, ran script) and inputted flu-mutations.log. Someone can grab figures from this by giving it as input to Tracer.

6. Now we have a set of substitution and time tree for each time period. I am going to run TreeAnnotator on each of the six files in order to create an MCC tree file, which is a single tree that best reflects the most likely evolutionary relationships based on the posterior distribution of trees sampled. This will be our input for FigTree. A ten percent burin rate is 300,000. Here are the commands I used (\ is needed as escape char in bash, assumes mcc is a folder you made)
treeannotator -burnin 300000 -heights median flu-mutations.pre-COVID.\(time\).trees mcc/pre-COVID_mcc.\(time\).tree
treeannotator -burnin 300000 -heights median flu-mutations.during-COVID.\(time\).trees mcc/during-COVID_mcc.\(time\).tree
treeannotator -burnin 300000 -heights median flu-mutations.post-COVID.\(time\).trees mcc/post-COVID_mcc.\(time\).tree
treeannotator -burnin 300000 -heights median flu-mutations.pre-COVID.\(subst\).trees mcc/pre-COVID_mcc.\(subst\).tree
treeannotator -burnin 300000 -heights median flu-mutations.during-COVID.\(subst\).trees mcc/during-COVID_mcc.\(subst\).tree
treeannotator -burnin 300000 -heights median flu-mutations.post-COVID.\(subst\).trees mcc/post-COVID_mcc.\(subst\).tree