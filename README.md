# dbt-orchestration
Simple dbt project for testing out orchestration tools

# About
The purpose of this repository is to provide a simplistic dbt project that can be used for testing out orchestration tools like airflow, prefect and dagster. These orchestration tools do not inherently have anything to do with dbt, but I am interested in how they work with it.

[dbt](https://www.getdbt.com/) is a (great) tool for transforming data that has been loaded to a database. Here I use the command line version, which is open source.

# Setup
1. [Install python](https://www.python.org/downloads/): I used version 3.8.10 as there currently appears to be an issue with dbt installation when using 3.9.* versions.
2. Clone this repository
3. Create and activate a python virtual environment
    
        python -m venv env
        .\env\Scripts\activate

4. Install requirements

        pip install -r requirements.txt

5. Install postgres

    dbt needs a database to deploy to. I decided to use a local installation of postgres.

# References
These are resources I used while creating this repository:
- [dbt CLI setup with pip](https://docs.getdbt.com/dbt-cli/installation#pip)
