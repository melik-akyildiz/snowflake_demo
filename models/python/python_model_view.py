def model(dbt, session):
    target_name = dbt.config.get("PYTHON_MODEL_TABLE")
    target_df =dbt.this()


    return target_df