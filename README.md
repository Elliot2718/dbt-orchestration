# dbt-orchestration
Simple dbt project for testing out orchestration tools

# About
The purpose of this repository is to provide a simple dbt project that can be used for testing out data pipeline orchestration tools like airflow, prefect and dagster. These tools do not inherently have anything to do with dbt, but I am interested in how they work with it.

[dbt](https://www.getdbt.com/) is a (great) tool for managing transformations on data that has been loaded to a database. Here I use the command line version, which is open source.

dbt has adaptors for [most common databases](https://docs.getdbt.com/docs/available-adapters). For this project I use BigQuery and the public [Iowa Liquor Retail Sales](https://console.cloud.google.com/marketplace/product/iowa-department-of-commerce/iowa-liquor-sales) dataset.

## Setup

### BigQuery
1. If you don't already have a Google Cloud Platform account, [create one for free](https://cloud.google.com/).
1. Log onto the [Google Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager) and create a project named `dbt-orchestration`.
3. Set up [local authentication using gcloud](https://docs.getdbt.com/reference/warehouse-profiles/bigquery-profile#local-oauth-gcloud-setup).

### Local 
1. [Install python](https://www.python.org/downloads/): I used version 3.8.10 as there currently appears to be an issue with dbt installation when using 3.9.* versions.
2. Clone this repository.
3. Create and activate a python virtual environment and install requirements:

        python -m venv env
        .\env\Scripts\activate
        pip install -r requirements.txt
        dbt deps

4. Add a `profiles.yml` file to the `~/.dbt/` directory. To help find this directory you can run the command `dbt debug --config-dir`. The profiles file should contain this:

    ```yml
    bigquery:
      target: development
      outputs:
        development:
          type: bigquery
          method: oauth
          project: dbt-orchestration #Use the project-id here
          dataset: iowa_liquor_sales
          threads: 1
          timeout_seconds: 300
          location: US
          priority: interactive
          retries: 1
    ```

    Update the `project` to match your Google Cloud Platform project id.

# Orchestration tests
I created a two step data pipeline:
1. Create a view in BigQuery off of the Iowa Liquor Sales dataset.
2. Run tests on that view.

What follow are demonstrations of different ways that this data pipeline can be run.

## Manual
The simplest way to orchestrate the dbt CLI is to do it manually! 😊 But even when using another tool, it is  a good way to test things out.

### 1. Create a view
This is as simple as running the `dbt run` command. Check your project in BigQuery; under your project you should see a new dataset named `iowa-liquor-sales` and a view named `sales_by_year_month_product`.

### 2. Run tests
Run `dbt test` to run the [schema tests](https://docs.getdbt.com/docs/building-a-dbt-project/tests) defined in the [iowa_liquor_sales.yml](./models/iowa_liquor_sales/iowa_liquor_sales.yml) file.
