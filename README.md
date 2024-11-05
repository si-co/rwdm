# Artifacts for "Real-World Deniability in Messaging"
This repository contains the artifacts
for the paper "Real-World Deniability in Messaging".
The artifacts consist in a Python 
script that 
we use to query 
[https://entscheidsuche.ch/](https://entscheidsuche.ch) 
and the complete results of our legal analysis 
(Section 5 in the paper).
This repository contains the following files:
* The description of the artifact is provided in 
[ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md).
* The script that we use to query 
[https://entscheidsuche.ch/](https://entscheidsuche.ch) 
is provided in [search.py](search.py). Instructions to run this script
and analyze its output are given in 
[ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md).
* The complete results of our legal analysis with English translations
for comments in French and Italian is provided in 
[court_cases.csv](court_cases.csv).
* The license under which we publish the content of this repository
is given in [LICENSE](LICENSE).
* We provide an additional script in [download_cases.py](download_cases.py)
to download the court cases listed in the first column
of [court_cases.csv](court_cases.csv). The script
creates a folder `court_cases` with 341 HTML or PDF files. See
[ARTIFACT-EVALUATION.md](ARTIFACT-EVALUATION.md) for instructions
on how to run this script.
* We provide also a ZIP file [court_cases.zip](court_cases.zip)
that contains all the files that the 
[download_cases.py](download_cases.py) script downloads (as
of 5th of November 2024).

**Warning**: The court cases under analysis are in 
French and Italian.

The content of this repository is distributed under GNU GPLv3 license.
