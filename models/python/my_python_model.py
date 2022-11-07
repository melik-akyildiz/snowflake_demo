def model(dbt, session):
    dbt.config(
        materialized = "table"
    )

    temps_df = dbt.ref("fct_orders")

    return temps_df