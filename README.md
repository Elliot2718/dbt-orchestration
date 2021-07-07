# dbt-orchestration
Simple dbt project for testing out orchestration tools

# About
The purpose of this repository is to provide a simple dbt project that can be used for testing out data pipeline orchestration (workflow management) tools like airflow, prefect and dagster. These tools do not inherently have anything to do with dbt, but I am interested in how they work with it.

[dbt](https://www.getdbt.com/) is a (great) tool for managing transformations on data that has been loaded to a database. Here I use the command line version, which is open source.

dbt has adaptors for [most common databases](https://docs.getdbt.com/docs/available-adapters). For this project I use BigQuery and the public [Iowa Liquor Retail Sales](https://console.cloud.google.com/marketplace/product/iowa-department-of-commerce/iowa-liquor-sales) dataset.

## BigQuery Setup
This project uses BigQuery as the database that dbt deploys a view to, under a project name of `dbt-orchestration`.

# Tool selection and evaluation

## Tool Selection
- Text-based (code or configuration) data pipeline definitions
- Open source, "open core" or SAAS model
- Support for multiple types of databases

## Evaluation
Before I tested out different tools, I decided on some qualitative categories to evaluate the tools on. They are:

1. **Configuration**: How quickly and easily can I get something set up?
2. **Documentation**: What type of documentation and support for the product is available?
3. **Scalability**: I am testing a simple pipeline; would the tool be able to scale out to support an enterprise data platform?
4. **User experience**: Would I want to use it every day?
5. **Monitoring**: When something breaks is it easy to figure out what went wrong?

I will rate these on a scale of 1-5 stars.

Other considerations I didn't include in my primary list are: cost, data sources, destinations, scheduling, triggering, etc.

# Orchestration tests
I created a two step data pipeline:
1. Create a view in BigQuery off of the Iowa Liquor Sales dataset.
2. Run tests on that view.

What follow are demonstrations of different ways that this data pipeline can be run.

## Manual
The simplest way to orchestrate the dbt CLI is to do it manually! 😊 But even when using another tool, it is a good way to test things out.

### Setup
1. [Install python](https://www.python.org/downloads/): I used version 3.8.10 as there currently appears to be an issue with dbt installation when using 3.9.* versions.
2. Clone this repository.
3. Create and activate a python virtual environment and install requirements:

        python -m venv env
        .\env\Scripts\activate
        pip install -r requirements.txt
        dbt deps

4. Add a `profiles.yml` file to the `~/.dbt/` directory. This defines the database and authentication method for dbt. To help find this directory you can run the command `dbt debug --config-dir`. The profiles file should contain this:

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

5. Set up [local authentication using gcloud](https://docs.getdbt.com/reference/warehouse-profiles/bigquery-profile#local-oauth-gcloud-setup) so you can connect to BigQuery.

### Running the Pipeline
#### 1. Create a view
This is as simple as running the `dbt run` command. Check your project in BigQuery; under your project you should see a new dataset named `iowa-liquor-sales` and a view named `sales_by_year_month_product`.

#### 2. Run tests
Run `dbt test` to run the [schema tests](https://docs.getdbt.com/docs/building-a-dbt-project/tests) defined in the [iowa_liquor_sales.yml](./models/iowa_liquor_sales/iowa_liquor_sales.yml) file.

### Evaluation
| Category | Rating | Comments
-- | -- | --
Configuration | ⭐⭐ | Fairly quick to set up a simple pipeline; would not support a large solution.
Documentation | ⭐ | As good as you make it since you'd be writing it youself 😛.
Scalability | ⭐ | Would take much effort to scale.
User Experience | ⭐⭐ | Huge flexibility, but not a great experience for everyone.
Monitoring | ⭐⭐  | Since you run it manually, you literally have someone monitoring the pipeline, but not really scalable...

_**Takeaway**: Not a scalable solution, but a great way to test out commands._

## Github Actions
Github actions is a workflow automation tool. Since we are deploying a simple pipeline, we can run the same commands we did above

## Azure DevOps Pipelines

## Airflow

## Prefect

## Dagster
