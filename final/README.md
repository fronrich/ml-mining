# Blanton Art Recommender

## Created By Fronrich Puno and Ana Williams

---

## Purpose

A python API used to consolidate udergraduate survey data of artworks at the Blanton museum and use them to generate art reccomendations.

> Although purposed for the Blanton Museum of Art, this API can be implimented with any backend architecture that takes in stores data in xlsx format.

## Installation

You can git clone this repo into your local directory for standalone use or use as an API

## Requirements

### Python

You will first need to make sure you have a python environment and Jupyter notebook. For help with setting up python environments, [click here](https://docs.python.org/3/using/index.html), for help with Jupyter Notebook, [click here](https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-for-python-3). PLease note that these steps were done on Linux

After setting up the environment go into the project directory and enter the command `pip install requirements.txt` into the terminal

> Make sure that you pip install the requirements.txt before trying to run anything, or else the missing dependancies will prevent the code from running

### Data formatting

While the API has data cleaning capabilites, it is advised to at least try to input data with the following column headers:

`['accession_#', 'artist_sort_name', 'artist_life_dates', 'artist_nationality', 'title', 'creation_date', 'medium', 'credit_line', 'dimensions', 'student_id', 'emotional_reaction', 'aesthetically_pleasing']`

> Note that the column `'accession_#'` should contain unqiue ids.

> `'emotional_reaction'` and `'aesthetically_pleasing'` should be binary feilds, meaning that for each row, they either contain a 0 or a 1

0 - disagrees with proposition stated by column title

1 - agrees with proposition stated by column title

## Running

The root directory of the API, type in the command `Jupyter Notebookblanton_final_project.ipynb`.

Jupyter Notebook should open up in the browser, run the code and you're done!

Alternatively, if you would like to use this code in a python file or python Lambda function, just copy and paste all the code, ommiting markdown and running as needed.
