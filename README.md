# Probabilistic Reduction and the Mental Lexicon

by [**Anna Stein**](https://ansost.github.io) 

[2-3 sentence description of thesis]
[figure of main results]

## Software implementation
All source code used to generate the results and figures in this thesis are in the `code/` folder. 
The calculations and figure generation are all run inside [Jupyter notebooks](http://jupyter.org/) for the Python code, and [R Markdown](https://rmarkdown.rstudio.com/) for the R code. 

### Data
Since the Buckeye corpus licence does not permit derivatives of the corpus to be uploaded, I cannot upload the data that I used. 
However, a copy of the Buckeye corpus is easily available for free on their [website](https://buckeyecorpus.osu.edu/php/speech.php).
> Note that you need the zipped version of the corpus (that is the default) in order to use the [Buckeye package](https://github.com/scjs/buckeye) with the corpus.

## Getting the code

Either clone the [git](https://git-scm.com/) repository:
```sh
git clone git@github.com:ansost/informativity_pilot.git
```
or [download a zip archive](https://github.com/ansost/informativity_pilot/archive/refs/heads/main.zip).

## Install dependencies
In the root folder of the repository, install the Python requirements with pip:
```sh
pip install -r requirements.txt
```
Dependencies for the R code are handled within the R-Markdown file. You have to install [pacman](https://www.rdocumentation.org/packages/pacman/versions/0.5.1) (code is provided) which automatically loads libraries or installs them if you dont have them already. 

## Reproducing the results
You need to install both [Jupyter Notebook](https://jupyter.org/install) and [R Studio](https://posit.co/downloads/) in order to reproduce this analysis. Both softwares are available for free for all platforms. 
You can start the jupyter notebook server by going into therepository top level and running:
```sh
jupyter notebook
```
This will start the server and open your default web browser to the Jupyter interface. In the page, go into the `code` folder and select the notebook that you wish to view/run. The notebook is divided into cells (some have text while other have code). Each cell can be executed using `Shift + Enter`. Executing text cells does nothing and executing code cells runs the code and produces it's output. To execute the whole notebook, run all cells in order.

## Workflow

Below is a short version of what you ened to do in order to recreate my workflow. All of these files are in the `/code`folder. A longer, more thourough version of the worklofw can be found in `docs/workflow.txt`. 

The code for this thesis, especially the Python code, is by no means the most efficient way to do things. However, it represents my coding journey and what I was able to do at the time. In the future I hope to add a more concise and faster version of the current code. 

1. Create a **word list** for every speaker in the Buckeye corpus with `text-perspeaker.ipynb`.
2. Create table with **data** from the Buckeye corpus **for the regression analysis** with `regression_data.ipynb`.
3. Create individual **speaker event files** with `eventfilesV1.ipynb`.
4. Correct the previous event files with `correctingV1eventfiles.ipynb`.
5. **Train** the NDL model with the input from 4. with `trainNDL.ipynb`.
6. Compute **NDL predictors** for the regression analysis with `prior_activation.ipynb`.
7. Compute **speech rate** per utterance with `speech_rate.ipynb`.
8. Do the **statistical analysis** with `regression_analysis.Rmd`

## License

All source code is made available under a BSD 3-clause license. You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors. See `LICENSE.md` for the full license text.

The manuscript text is not open source. The author reserves the rights to the
thesis content.

## Author
**Anna Stein**

Website: [https://ansost.github.io](https://ansost.github.io)

If you are having problems with anything regarding this repository, please write me email: [anna.stein@hhu.de](mailto:anna.stein@hhu.de)
