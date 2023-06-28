robust-dataprojects-template
=============================

Template repository with Cookie Cutter Infrastructure that can be forked for every new Data Science project in your organization. It aims to provide a guideline on how to start your project with a more **robust infrastructure** than just using jupyter notebooks.

-------------
## How to Start a Data Project in a Somewhat More Robust Way?

Many people know how to do a good data project when it comes to using the most advanced machine learning techniques. However, not everyone knows how to use a robust and suitable structure to accommodate all this code that has been developed.

In an ideal world, it would be interesting to have every project structured using best practices and the minimum requirements of MLOps. However, it is neither easy nor cheap to have all this structure at your disposal, as it is something still emerging in the market (at least in our view), there is an enormous complexity of which tools to use to make up your MLOps stack that will support the entire lifecycle of your data project. In addition to specific skills for this, you will also need a good amount of time to get all this in practice and working well.

We believe that there is, however, a crucial first step in this direction (note that we are not talking about a stopgap solution) that would greatly improve the maturity level of projects. That is, in practice and in the short term, it is already possible to have a structure that is robust enough for data professionals to take a first step towards MLOps or at least in the direction of more robust code/project structure.

As the team starts to incorporate these concepts and practices into new projects, the work of a future machine learning engineer or person responsible for MLOps/model deployment will be infinitely easier.

In this regard, we have compiled here in this document the requirements and minimum necessary steps to:

- Improve the organizational structure of your data project's folders using the recommendations of the classic template provider cookiecutters, the [Cookie Cutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) (we HIGHLY recommend reading the content on the page)
- Improve the organizational level of your code in a practical way (using [Sonarlint](https://www.sonarsource.com/products/sonarlint/)) applying the best concepts (such as the [PEP-8](https://peps.python.org/pep-0008/) style)
- Version not only the codes, but also the data and experiments using [dvc](https://dvc.org/)

The main benefits would be:

- Minimization of knowledge loss when there is a need to transfer projects to new team hires
- Robust KT (knowledge transfer) base for team training and capacity building
- Maximization of the level of security, organization, and reliability of projects (even improving the delivery of value to your customer, whether internal or external)

## Prerequisites

What you need to have installed on your machine or start using to start having a more robust structure in your data projects

1. It is recommended that the entire process be carried out in a Linux environment. Windows users can easily create a virtualized Linux environment through WSL, a native Windows feature.
2. Tools:

| Type of tool | Tool name |
|------------ | ------------|
|Code file format (mostly)| .py instead of .ipynb |
|Programming IDE | VS Code|
|Code versioning system | git|
|VS Code extension to assist with PEP-8 | Sonarlint|
|System for versioning data, models, and experiments | dvc|

Notice that in the case of the programming IDE, we have agreed on the use of VS Code, for some reasons:

- The tool most widely used worldwide to produce code at a highly professional and robust level
- Facilitates the use of other conventions like PEP-8
- Integrable to git
- Allows the use of assistant programs for code creation
- Enables interaction very similar to the already popular Jupyter Notebook.

In addition to

 all the advantages mentioned above, we still have the following prerogative for the use of VS Code:

- The codes to be produced for a data project can already be generated in their final format *.py* without the need for *.ipynb* format migration
- The entire MLOps pipeline will work with *.py* format codes (a necessary requirement, including for MLOps)
- Constant version control of the codes that are being developed via git

##### Does this mean that the data scientist, for example, will no longer be able to work with Jupyter?

They can indeed! However, the person who opts to use it will have to at some point
migrate the codes in *.py* format to the project pipeline. This may result in more rework and inefficiency, but it is important to trust that each professional will make a good judgment of whether or not to use Jupyter (or use it at the right time, such as for good documentation with exploratory analysis code). Remember also that using Jupyter prevents observation of differences between .ipynb files, making code versioning difficult.

See in the figure below how easy it is to have the [interactivity of a jupyter in VS Code](https://code.visualstudio.com/docs/python/jupyter-support-py)
![interactive cells with vscode](/docs/images/interactive_cells_with_vscode.gif)

**Important**: if you do not feel comfortable going directly to the tutorial, we recommend this excellent course from the company that created dvc (data versioning control), iterative.ai. The link is in this short [Introductory course on the use of dvc and basic MLOps fundamentals in projects](https://learn.iterative.ai/)

## Step by step to set up a new data project using the proposed new structure

1. In your git tool (github, for example), create a new repository on the project you will work on (check if there is any taxonomy to be followed for creating this name). **Please do not include `README.md` neither `.gitignore` files at the creation of the repo.

2. Clone this **Template** project repository available [here at this link](https://github.com/Aignosi/robust-dataproject-template) or copy and paste the piece of code below:

```
git clone https://github.com/Aignosi/robust-dataproject-template.git
```

3. Rename the directory that was created locally using the same name of the remote repository (created in step 01)

```
mv <current directory name> <new directory name> 
```


4. Access the renamed directory and remove the ".git" files from the directory using the command 

 ```
rm -rf .git
 ```

this will serve to clean any previous git history, if any. Thus avoiding conflicts with the new repository you want to use.

5. Start versioning the project immediately afterwards, through the git initialization command

```
git init
```

6. If your git is not yet configured, adjust the default configuration for the "init" command whenever creating the first branch as main:       

 ```
 git config --global init.defaultBranch main
 ```

7. Create a virtual environment for python and activate the environment (if you don't know how to create, [follow this tutorial](https://klauslaube.com.br/2015/07/23/virtualenvwrapper-o-basico-para-um-bom-ambiente-de-desenvolvimento-python.html))

8. Add the directory of your environment, if it is present in the repository, to the general ".gitignore"

9. Check the status 

```
git status
```

If you are not on the Main branch, use the command to change to the Main branch (or whichever suits you best)

```
git branch -M main
```

10. Add all the files at once (from

 the Cookie Cutter structure) to commit to the local repo

```
git add .
```

11. Make the first commit

```
git commit -m 'first commit'
```

12. Add the remote repository ("remote") to your local repository, placing the address of the repository created in step 1 (this will establish the link between the local repository and the remote repository you use)

```
git remote add source <repo url>
```


13. Make the push (sending) of the local version of your code to the remote repository in the git tool of your choice on the `main` branch

```
git push -u source main
```


## Setting up and using the other tools: dvc, Sonarlint

We will soon include the rest of the tutorial on how to add dvc and the sonarlint extension to this more modern data project stack.

Robust Data Science Project Organization tree
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── data processing <- Scripts to process data
    │   │   └── processed_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    └── 


--------

<p><small>Project based and adapted from the original <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
