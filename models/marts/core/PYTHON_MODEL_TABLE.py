def model(dbt, session):
    dbt.config(
        materialized='table',
        transient=false
    )

    temps_df = dbt.ref("PYTHON_MODEL_TABLE")

    return temps_df