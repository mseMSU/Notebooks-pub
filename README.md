# MSE Python Notebooks

Public, executable instructional notebooks for Python fundamentals, scientific
data analysis, visualization, and materials science laboratory work at Michigan
State University.

This repository is a public execution mirror of a private authoring repository.
It contains only the notebooks, their required data, and the reproducible Python
environment. It intentionally does not contain the private repository's Git
history or GitBook publishing configuration.

## Notebooks

| Topic | Notebook | Run online |
| --- | --- | --- |
| Python basics | [A crashcourse in Python](notebooks/General/Basics_Python.ipynb) | [Open in Colab](https://colab.research.google.com/github/mseMSU/Notebooks-pub/blob/main/notebooks/General/Basics_Python.ipynb) · [Launch Binder](https://mybinder.org/v2/gh/mseMSU/Notebooks-pub/main?urlpath=lab/tree/notebooks/General/Basics_Python.ipynb) |
| Scientific data analysis | [Data Analysis in Python with pandas](notebooks/General/Basics_DataAnalysis.ipynb) | [Open in Colab](https://colab.research.google.com/github/mseMSU/Notebooks-pub/blob/main/notebooks/General/Basics_DataAnalysis.ipynb) · [Launch Binder](https://mybinder.org/v2/gh/mseMSU/Notebooks-pub/main?urlpath=lab/tree/notebooks/General/Basics_DataAnalysis.ipynb) |
| Data visualization | [Data Visualization in Python](notebooks/General/Basics_Plotting.ipynb) | [Open in Colab](https://colab.research.google.com/github/mseMSU/Notebooks-pub/blob/main/notebooks/General/Basics_Plotting.ipynb) · [Launch Binder](https://mybinder.org/v2/gh/mseMSU/Notebooks-pub/main?urlpath=lab/tree/notebooks/General/Basics_Plotting.ipynb) |
| MSE 250 laboratory | [Lab 2: Tensile Testing](notebooks/MSE/250/Lab_2_TensileTesting/Lab_2_TensileTesting.ipynb) | [Open in Colab](https://colab.research.google.com/github/mseMSU/Notebooks-pub/blob/main/notebooks/MSE/250/Lab_2_TensileTesting/Lab_2_TensileTesting.ipynb) · [Launch Binder](https://mybinder.org/v2/gh/mseMSU/Notebooks-pub/main?urlpath=lab/tree/notebooks/MSE/250/Lab_2_TensileTesting/Lab_2_TensileTesting.ipynb) |

Colab is generally the fastest way to begin. Binder builds the environment from
`environment.yml`, so its first launch after an environment change can take a
few minutes.

## Local use

```bash
conda env create -f environment.yml
conda activate mse-notebooks
jupyter lab
```

Start JupyterLab from the repository root. The general analysis and plotting
notebooks use the shared `notebooks/nbkit.py` module to find files under
`notebooks/Data/`. The same helper retrieves those files from this repository
when a notebook is opened independently in Colab.

## License

Unless otherwise noted:

- Instructional text, documentation, figures, and other non-code content are
  licensed under the [Creative Commons Attribution 4.0 International License](LICENSE-CONTENT.md).
- Source code, including Python code in notebook cells, is licensed under the
  [BSD 3-Clause License](LICENSE-CODE.md).

Third-party materials remain subject to their respective licenses. Michigan
State University names, logos, and trademarks are not licensed under these
terms. Use of this material does not imply endorsement by Michigan State
University.
