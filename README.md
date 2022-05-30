# Prediction of antibiotic resistance in Escherichia coli from large-scale pan-genome data
Danesh Moradigaravand

# Machine Learning aided Prediction of Plasmid Permsiveness 

## Table of contents
1. [Citation](#citation)
2. [Introduction](#content)
3. [Installation](#installation)
4. [Manual](#manual)
5. [Supplemental files](#package)
6. [Contact](#contact)

----

### Citation <a name="citation"></a>

This package has been developed by the Moradigaravand lab as part of the following paper:

**Prediction of antibiotic resistance in Escherichia coli from large-scale pan-genome data**
***D Moradigaravand, M Palm, A Farewell, V Mustonen, J Warringer, L Parts***
*PLoS computational biology 14 (12), e1006258*

----

### Introduction <a name="content"></a>
The emergence of microbial antibiotic resistance is a global health threat. In clinical settings, the key to controlling spread of resistant strains is accurate and rapid detection. As traditional culture-based methods are time consuming, genetic approaches have recently been developed for this task. The detection of antibiotic resistance is typically made by measuring a few known determinants previously identified from genome sequencing, and thus requires the prior knowledge of its biological mechanisms. To overcome this limitation, we employed machine learning models to predict resistance to 11 compounds across four classes of antibiotics from existing and novel whole genome sequences of 1936 E. coli strains. We considered a range of methods, and examined population structure, isolation year, gene content, and polymorphism information as predictors. Gradient boosted decision trees consistently outperformed alternative models with an average accuracy of 0.91 on held-out data (range 0.81-0.97). While the best models most frequently employed gene content, an average accuracy score of 0.90 could be obtained using population structure information alone. Single nucleotide variation data were less useful, and significantly improved prediction only for two antibiotics, including ciprofloxacin. These results demonstrate that antibiotic resistance in E. coli can be accurately predicted from whole genome sequences without a priori knowledge of mechanisms, and that both genomic and epidemiological data can be informative. This paves way to integrating machine learning approaches into diagnostic tools in the clinic.

This package includes machine learning toolkit used for prediction. The models include a regularized logistic regression, random forests, gradient boosted decision tree and deep learning. 

----
### Installation <a name="installation"></a>

There are three ways to run the tool:

- The package may be downloaded and run as a binary file, **./PlasmidPred.bin**. 

- The tool is available on DockerHub and may be fetched and run using the following commmands:

```
docker pull daneshmoradigaravand/panpred:latest
docker run -v $PWD:/data --rm -it panpred ./PanPred.py -h
```

- The python file may be executed directly, using the following command:

```
python3 PanPred.py
```

----
### Manual <a name="manual"></a>

The tools is initiated using the binary command. The help instruction is called using -h option. The tool has two functionalities: preprocesssing and modelling.  

```
Usage: PanPred <command> [options]

Command:
		    preprocess	    preprocess and creates the NGS input data for Machine Learning tools
		    predict_LR _RF _GB _DL	    Calls a Machine Learning model, i.e. Logistic regression, RandomForests, GradientBoosted and Deep Learning, to predict resistance from input
```

#### Preprocessing
The preprocess step prodduces the input file for the modeling part. 

```
Usage:
PanPred preprocess [options]

Options:
        -p STR   path to csv and Rtab files (Roary output files), default value: current path
        -c STR   create: create input file,  encode: label encoder for population structure, dedup: prepare Roary output
        -d STR   drug id number in the metadata file
        -i STR   input model ['GY', 'GYS', 'G','GS', 'S', 'SY']
        
        -m STR   name of the metadata file 
        -g STR   name of the accessory gene file
        -s STR   name of the population strcuture file
        
        -r STR   name of Rtab file from Roary output (.Rtab)
        -a STR   name of gene presence absence file from Roary output (.csv)

```

The ***G***, ***Y*** and ***S*** options stand for gene presence and absence pattern, year and population strcture. The input for pangenoe should be in the format of the Rtab file from Roary. 


#### Modelling

The modelling toolkit comprises four models, callable using the perdicts options.


##### Logistic regression based prediction

```
python PanPred.py predict_LR
0.0
Calls a Machine Learning modelLogistic regression
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -g FLT    L2 penalty
        -r FLT    train/test ratio
```

##### Random forest based prediction

```
python PanPred.py predict_RF
None
Calls a Machine Learning model RandomForests
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio

```
##### Gradient boosted decision trees based prediction

```
python PanPred.py predict_GB
None
Calls a Machine Learning model GradientBossting 
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio
```

##### Deep Learning based prediction

```
python PanPred.py predict_DL
Calls a Machine Learning model Deep Learning
Usage:
PanPred predict [options]

Options:
        -p STR    path to input file and destination for output file 
        -i STR    input file name
        -r FLT    train/test ratio
        
        -d FLT    drop_out
        -n INT   number of nodes in the first layer
        -m INT   number of nodes in intermediate layers
        -l INT    number of layers
```

Note for random forests and gradient boosted decision trees optimal parameters reported in the paper are used. 


----
### Supplemental files <a name="package"></a>

The test_data directory contains input files and basic ML commands.

- **/test_data**: input data used in the manuscript
- **/Rcode**: R code for population structure matrix generator.

- **CARD_resistance**	CARD resistance results

- **ResFinder_resistance** Resfinder resistance results

- **GB_tuning.csv**	GB (Gradient boosted decision trees) hyperparameter tuning results 

- **LG_tuning.csv**	LG (Logistic Regression) hyperparameter tuning results

- **NN_tuning.csv**	NN (Deep Learning) hyperparameter tuning results

- **RF_tuning.csv**	RF (Random Forests) hyperparameter tuning results

Esternal files are found 

- [Pan genome sequences](https://data.mendeley.com/datasets/t2pzcb37y8/1)
- [Assembly files for newly sequenced genomes] (https://data.mendeley.com/datasets/fhmbdc496y/1)

----
### Contact <a name="contact"></a>
For queries, please contact [Danesh Moradigaravand](mailto:d.moradigaravand@bham.ac.uk?subject=[GitHub]), Data-Driven Microbiology lab, Center for Computational Biology, University of Birmingham. 
 






