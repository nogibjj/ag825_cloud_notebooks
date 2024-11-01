

# Mini Project  9: Cloud Hosted Notebook Data Manipulation
Adil Keku Gazder <br>
ag825, adil.gazder@duke.edu <br>
IDS 706: Data Engineering Systems <br>
Duke University, Fall 2024 <br >
##

### About the project
[![Format](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/format.yml)
[![Format](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/ag825_cloud_notebooks/actions/workflows/test.yml)
<br>
The aim with this project was to read a .csv file and generate summary statistics and plots describing the data. The dataset used for this project was acquired from Kaggle (Olympic Summer Games - Paris 2024 -> medallists.csv)

The online .ipynb notebook can be accessed here: https://colab.research.google.com/drive/1bLn32NHoZpYl8hEkWrjCdg38u8LMrCsI#scrollTo=ecn3t85yiC12

The dataset used can be accessed here: https://www.kaggle.com/datasets/muhammadehsan02/olympic-summer-games-paris-2024?select=medallists.csv

##
### Repository Structure
The structure of this file is as follows:
- .gitignore file
- .github/workflows file
    - Used to define an automated process which will run the pipeline before publishing
    - Will be defined using a YAML file
- Makefile
    - Compilation and maintainence of code
    - Helps manage dependinces
    - Install / Format / Lint / Test
- Requirements file
    - Text file (.txt) detailing the required packages to be installed for this program to run
- notebook.ipynb
    - read_data(): Reads the datafile
    - about_data(): Descriptive satistics about the data
    - createplots(): Creates two plots describing the dataset
    - createsummary(): Creates a summary of this analysis and writes to a markdown file (summary_report.md)
- medallists.csv
    - Source data in .csv format
- summary_report.md
    - Final output in a markdown file

##
### Expected Output
This file generates the following on execution:
- Head of the data (top 5 rows of the entire dataset)
- Descriptive statistics about the dataset
    - Count
    - Mean
    - Standard Deviation
    - Minimum value
    - 25th percentile
    - 50th percentile
    - 75th percentile
    - Maximum value
- Bar graph detailing the number of total medals won per country
- Line chart detailing the total medals won per day for each day of the athletics
