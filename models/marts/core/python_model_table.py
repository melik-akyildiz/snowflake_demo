def model(dbt, session):
    dbt.config(
        materialized='table',
        transient=false
    )

    temps_df = dbt.ref("python_model_table")

    return temps_df