# Probabilistic Reduction and the Mental Lexicon

by [**Anna Stein**](https://ansost.github.io) 

[2-3 sentence description of thesis]
[figure of main results]

## Software implementation
All source code used to generate the results and figures in this thesis are in the `code/` folder. 
The calculations and figure generation are all run inside [Jupyter notebooks](http://jupyter.org/). 
Since the Buckeye corpus licence does not permit derivatives of the corpus to be uploaded, I cannot upload the data that I used. 
However, a copy of the Buckeye corpus is easily attainable on their [website](https://buckeyecorpus.osu.edu/php/speech.php).
> Note that you need the zipped version of the corpus (that is the default) in order to use the [Buckeye package](https://github.com/scjs/buckeye) with the corpus.

The code for this thesis is by no means the most efficient way to do things. However, it represents my coding journey and what I was able to do at the time. In the future I hope to add a 
more concise and faster version of the current code. 

## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:
```sh
git clone git@github.com:ansost/BAthesis2023.git
```
or [download a zip archive](https://github.com/ansost/BAthesis2023/archive/refs/heads/main.zip).

## Dependencies

The required dependencies are specified in the file `requirements.txt`. 
You can install them using [`pip`](https://www.w3schools.com/python/python_pip.asp) the package manager of [Python](https://www.python.org/). 
Navigate into the the repository and in your command line, type:
```sh
pip install -r requirements.txt
```

## Reproducing the results

One way of exploring the code results is to execute the Jupyter notebooks individually. To do this, you must first start the notebook server by going into the
repository top level and running:
```sh
jupyter notebook
```

Provided you have installed [Jupyter notebook](https://jupyter.org/install), this will start the server and open your default web browser to the Jupyter interface. In the page, go into the `code` folder and select the
notebook that you wish to view/run.

The notebook is divided into cells (some have text while other have code). Each cell can be executed using `Shift + Enter`. Executing text cells does nothing and executing code cells runs the code
and produces it's output. To execute the whole notebook, run all cells in order.

### Workflow

**1. Create a word list for every speaker  with `text-perspeaker.ipynb`.** 
      
- Creates one '.csv' file for each of the 40 speakers with the columns 'speaker', 'token' and 'token_duration'.  
      
    *Input:* Buckeye corpus
    
    *Output:* 40 .csv files

---

**2. Create table with data for regression analysis with `regression_data.ipynb`**
- Columns: speakerID, speakerGender, interviewerGender, wordID, wordDur, wordPOS, n_segments, n_syllables, (empty) speech rate column
	 
	*Input:* 'en_us_cmudict_forward.pt' &  Buckeye corpus
  
  *Output:* regression_data dataframe

---

**3. Create one event file for all speakers to use as model input.**
    
    
3.1 Create individual speaker event files with `eventfilesV1.ipynb`
    
- Creates 40 individual event files and then concatenates them into on event file
- The files are comma delimited and the index column is saved 
    
    *Input:* 'en_us_cmudict_forward.pt' & speaker word lists
    
    *Output:* 40 speaker event files, One big event file  
    
	
3.2 Correct the previous event files with `correctingV1eventfiles.ipynb` 
- Tab-delimits the old event files and removes the index column
- Merges them into one big event file
- Sanity checks for missing words with the 'regression_data' dataframe
	
    *Input:* 'regression_data.csv' & old eventfiles
    
    *Output:* correct event file

---

**4. Train the NDL model with `trainNDL.ipynb`**
- Trains an [NDL](https://pyndl.readthedocs.io/en/latest/ndl.html) model using the [`pyndl`](https://pyndl.readthedocs.io/en/latest/) package
	
    *Input:* correct event file
    
    *Output:* weight matrix
    
---  
  
**5. Compute NDL measures with `prior_activation.ipynb`**
- Computes Activation and Prior for the buckeye weights
- Activation and prior are split by domain (Segment, Syllable, Context)
- Appends values to the regression_data dataframe
  
*Input:* 'variablesOtherPrior' python script & correct event file & weight matrix & regression_data
   
*Output:* updated regression_data dataframe 
    
---    
    
**6. Compute speech rate per utterance with `speech_rate.ipynb`**
    
    *Input:* Buckeye corpus
    
    *Output:* updated regression_data dataframe 
  
---  
  
**7. Statistical analysis**
[...Yet to be uploaded] 
   
## License

All source code is made available under a BSD 3-clause license. You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors. See `LICENSE.md` for the full license text.

The manuscript text is not open source. The author reserves the rights to the
thesis content.


**This README is heavily inspired by the README template for papers from the pings lab: https://github.com/pinga-lab/paper-template**


## Author
[**Anna Stein**](https://ansost.github.io)
