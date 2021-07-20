from dagster import pipeline, solid, ModeDefinition, InputDefinition, Nothing
from dagster_dbt import dbt_cli_resource

my_dbt_resource = dbt_cli_resource.configured({"project_dir": "."})

@solid(required_resource_keys={"dbt"})
def run_all_models(context):
    context.resources.dbt.run()

@solid(required_resource_keys={"dbt"},input_defs=[InputDefinition("start", Nothing)])
def test_all_models(context):
    context.resources.dbt.test()

@pipeline(mode_defs=[ModeDefinition(resource_defs={"dbt": my_dbt_resource})])
def my_dbt_pipeline():
    test_all_models(start=run_all_models())
