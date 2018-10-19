# Prediction of antibiotic resistance in Escherichia coli from large-scale pan-genome data
Danesh Moradigaravand

The emergence of microbial antibiotic resistance is a global health threat. In clinical settings, the key to controlling spread of resistant strains is accurate and rapid detection. As traditional culture-based methods are time consuming, genetic approaches have recently been developed for this task. The detection of antibiotic resistance is typically made by measuring a few known determinants previously identified from genome sequencing, and thus requires the prior knowledge of its biological mechanisms. To overcome this limitation, we employed machine learning models to predict resistance to 11 compounds across four classes of antibiotics from existing and novel whole genome sequences of 1936 E. coli strains. We considered a range of methods, and examined population structure, isolation year, gene content, and polymorphism information as predictors. Gradient boosted decision trees consistently outperformed alternative models with an average accuracy of 0.91 on held-out data (range 0.81-0.97). While the best models most frequently employed gene content, an average accuracy score of 0.90 could be obtained using population structure information alone. Single nucleotide variation data were less useful, and significantly improved prediction only for two antibiotics, including ciprofloxacin. These results demonstrate that antibiotic resistance in E. coli can be accurately predicted from whole genome sequences without a priori knowledge of mechanisms, and that both genomic and epidemiological data can be informative. This paves way to integrating machine learning approaches into diagnostic tools in the clinic.

The test_data directory contains input files and basic ML commands.

/test_data: input data used in the manuscript
/Rcode: R code for population structure matrix generator.

CARD_resistance	CARD resistance results
ResFinder_resistance Resfinder resistance results
GB_tuning.csv	GB (Gradient boosted decision trees) hyperparameter tuning results 
LG_tuning.csv	LG (Logistic Regression) hyperparameter tuning results
NN_tuning.csv	NN (Deep Learning) hyperparameter tuning results
RF_tuning.csv	RF (Random Forests) hyperparameter tuning results


