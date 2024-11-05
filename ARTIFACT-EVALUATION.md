# Artifact Appendix

Paper title: Real-World Deniability in Messaging

Artifacts HotCRP Id: 18

Requested Badge: Available, Functional, Reproduced

## Description
**Warning**: The court cases under analysis are in 
French and Italian.

This artifact includes the Python script used to query 
[https://entscheidsuche.ch/](https://entscheidsuche.ch) 
to obtain an initial list of court cases in Switzerland. 
We manually prune and analyze this list as explained in 
Section 5.1 of the paper. 
The complete dataset, 
including our detailed manual analysis of the cases, 
is provided to support 
the conclusions presented in our results.
Note that the script 
does not return the exact list of court cases used for 
our analysis; 
see [Limitations](#limitations-only-for-functional-and-reproduced-badges)
for more details.

The analysis of court cases contains 
comments and excerpts from the legal
decisions in English, Italian, and French, 
since the cases under analysis are
originally in French and Italian. 
We provide a translation of our comments along
with the original comments that we used 
for our analysis, which are in English, French and Italian.
We translated the comments with the help of ChatGPT, but
we manually verified all the translations.

Given the simplicity of our artifacts, 
we do not use one of the provided VMs for
the evaluation. 
However, we are happy to do so if required by the reviewers.

### Security/Privacy Issues and Ethical Concerns (All badges)
There are no security or privacy issues. However, the dataset 
contains excerpts and comments from court cases, which may be 
disturbing to some readers (mentions of cases involving child 
abuse, CSAM material, and drug trafficking).

## Basic Requirements (Only for Functional and Reproduced badges)
Evaluating this artifact requires only a commodity laptop, 
negligible storage, and less than one minute of compute time.

### Hardware Requirements
No specific hardware requirements.

### Software Requirements
This artifact requires Python (tested with Python 3.12.6) and 
the [requests package](https://pypi.org/project/requests/) 
(tested with requests 2.32.3).

### Estimated Time and Storage Consumption
Negligible storage and less than one minute to execute the 
Python script.

## Environment 
Our artifacts consist of: 
1) A Python script to retrieve relevant court cases. 
2) The results of our legal analysis.

### Accessibility (All badges)
Our artifact's repository is available at: 
[https://github.com/si-co/rwdm](https://github.com/si-co/rwdm).
Reviewers can use 
[commit
cc10c7071f2ee792c73d1e7630ee0bf252087308](https://github.com/si-co/rwdm/tree/cc10c7071f2ee792c73d1e7630ee0bf252087308).

### Set Up the Environment (Only for Functional and Reproduced badges)
Reviewers need to install Python (tested with Python 3.12.6) and 
the requests package (tested with requests 2.32.3). To install 
the package, use the OS package manager or run:

```
pip install --user requests
```

Then, clone the repository:

```
git clone git@github.com:si-co/rwdm.git
```

### Testing the Environment (Only for Functional and Reproduced badges)
No functionality tests are required.

## Artifact Evaluation (Only for Functional and Reproduced badges)
Our artifact includes a Python script used to fetch the initial 
list of court cases from [https://entscheidsuche.ch/](https://entscheidsuche.ch) 
and the complete dataset from our legal analysis.

### Main Results and Claims
List all your paper's results and claims supported by your 
submitted artifacts.

#### Main Result 1: Results of Legal Analysis 
The results of our legal analysis are summarized in Table 1 
(Section 5.2, page 10). The complete legal analysis is stored 
in a CSV file in our repository ([court_cases.csv](court_cases.csv)) and on 
Google Docs ([link to Google Sheet](https://docs.google.com/spreadsheets/d/1jbrGybF6xHQECzPDFgT4IZRxp6C0MYVYRhkfAuYwMH0/edit?usp=sharing)).
The results summarized in Table 1 are available in our repository on [line 343 of the court_cases.csv file](https://github.com/si-co/rwdm/blob/main/court_cases.csv#L343) and reported below:

| VISITED | N/A       | PROOF     | CONTESTED | REJECTED |
|---------|-----------|-----------|-----------|----------|
| 341     | 201 (59%) | 140 (41%) | 2 (1%)    | 0        |

### Experiments 
To run the Python script that retrieves the URLs of the legal 
cases from [https://entscheidsuche.ch/](https://entscheidsuche.ch), 
run `python search.py` from the root of the repository.

## Limitations (Only for Functional and Reproduced badges)
The `search.py` script returns a list of court cases that does 
not exactly match the list used for our legal analysis. Some 
cases returned by the script were added after our analysis, 
while approximately 15 cases have been removed since. We are 
unaware of the reasons for their removal from the 
[https://entscheidsuche.ch/](https://entscheidsuche.ch) database, 
but analyzing these additional cases (not present in the current 
results returned by our script) only strengthens our analysis.
