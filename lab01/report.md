\# Lab 01 — Environment Setup



\## 1. Environment Setup



The Lab 01 environment was created using Anaconda.



\* Environment name: `ai-lab`

\* Python version: 3.11

\* Jupyter Notebook was installed and configured.

\* The project repository was created as `ai-lab-portfolio`.

\* Git was initialized and connected to the GitHub repository.



The required Python packages were captured using:



```bash

pip freeze > requirements.txt

```



The `requirements.txt` file is included in the project repository.



\---



\## 2. Repository Structure



The main Lab 01 files are:



```text

ai-lab-portfolio/

│

├── .gitignore

├── requirements.txt

│

└── lab01/

&#x20;   ├── lab01\_setup.ipynb

&#x20;   ├── inspect.py

&#x20;   ├── report.md

&#x20;   └── exercises.txt

```



The `.gitignore` file is used to prevent unnecessary files such as environments, data files and secrets from being committed.



\---



\## 3. Dataset Inspection Script



The file `lab01/inspect.py` contains an `inspect(path\_or\_url)` function.



The function:



1\. Loads a CSV dataset using pandas.

2\. Prints the dataset shape.

3\. Prints the data types of all columns.

4\. Prints missing-value counts.

5\. Prints missing-value percentages.

6\. Prints a numeric summary using `describe()`.



The script was tested using public CSV datasets.



\---



\# 4. Inspection Output 1 — Titanic Dataset



Dataset:



```text

https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv

```



The inspection produced the following results:



\### Shape



```text

(891, 15)

```



\### Data Types



```text

survived         int64

pclass           int64

sex                str

age            float64

sibsp            int64

parch            int64

fare           float64

embarked           str

class              str

who                str

adult\_male       bool

deck               str

embark\_town        str

alive              str

alone             bool

dtype: object

```



\### Missing Values



```text

survived          0

pclass             0

sex                0

age              177

sibsp              0

parch              0

fare               0

embarked           2

class              0

who                0

adult\_male         0

deck             688

embark\_town        2

alive              0

alone              0

dtype: int64

```



\### Missing Percentages



```text

survived         0.00

pclass            0.00

sex               0.00

age              19.87

sibsp             0.00

parch             0.00

fare              0.00

embarked          0.22

class             0.00

who               0.00

adult\_male        0.00

deck             77.22

embark\_town       0.22

alive             0.00

alone             0.00

dtype: float64

```



\### Numeric Summary



```text

&#x20;         survived      pclass         age       sibsp       parch        fare

count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000

mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208

std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429

min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000

25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400

50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200

75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000

max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

```



\### Interpretation



The Titanic dataset contains 891 rows and 15 columns. The largest missing-value problem is the `deck` column, with 688 missing values (77.22%). The `age` column also contains substantial missing data, with 177 missing values (19.87%). The `embarked` and `embark\_town` columns have only two missing values each.



The numeric summary shows that the average survival value is approximately 0.384, meaning that the survival indicator is 1 for approximately 38.4% of the observations.



\---



\# 5. Inspection Output 2 — Second Public Dataset



Dataset:



```text

PASTE THE SECOND DATASET URL HERE

```



Command used:



```bash

python -m lab01.inspect "SECOND\_DATASET\_URL"

```



Output:



```text

PASTE THE COMPLETE OUTPUT FROM THE TERMINAL HERE

```



\### Interpretation



The second dataset was inspected using the same reusable `inspect.py` function. The output provides the dataset dimensions, column data types, missing-value counts, missing-value percentages and numeric descriptive statistics.



\---



\# 6. Inspection Output 3



Dataset:



```text

PASTE THE THIRD DATASET URL HERE

```



Command used:



```bash

python -m lab01.inspect "THIRD\_DATASET\_URL"

```



Output:



```text

PASTE THE COMPLETE OUTPUT FROM THE TERMINAL HERE

```



\### Interpretation



The third inspection demonstrates that the same inspection function can be reused with another CSV dataset without changing the source code.



\---



\# 7. Git History



The project was managed using Git throughout the Lab 01 workflow.



The Git history includes the environment setup, notebook work, requirements file and dataset inspection script.



Current Git history:



```text

\* a92b369 (HEAD -> main, origin/main) Complete dataset inspection script

\* 846a05e Add dataset inspection script

\* 10ff9ce Add requirements file

\* 2db2d73 Add lab01 exercises

\* 12c7b97 Complete Exercise 3 analysis

\* a5250ec Add Lab 01 report

\* 1826df7 Add gitignore

\* bce2103 Add Lab 01 setup notebook

```



The final working tree was clean and the `main` branch was synchronized with `origin/main`.



\---



\# 8. Home Assignment



For the home assignment, `inspect.py` was implemented as a reusable CSV inspection function.



The function was designed to work with both local CSV files and public CSV URLs.



The assignment requires testing the function on two different public datasets. The inspection outputs are documented in this report.



The script was committed to Git and merged into the `main` branch.



\---



\# 9. Conclusion



Lab 01 established the Python/Anaconda environment, Jupyter workflow, Git repository and reproducible dependency setup.



The `inspect.py` utility provides a simple and reusable first-pass dataset inspection workflow. It reports dataset shape, data types, missing values, missing percentages and numeric summaries.



The Titanic inspection demonstrated that the utility can quickly identify important data-quality issues such as missing values. In particular, the `deck` and `age` columns contain substantial missing data.



The Git history documents the development of the Lab 01 work and provides a reproducible record of the project.



