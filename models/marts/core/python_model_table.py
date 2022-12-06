def model(dbt, session):
    dbt.config(
        materialized='table',
        transient=false
    )

    temps_df = dbt.ref("dim_customers")

    return temps_df