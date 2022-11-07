def model(dbt, session):
    dbt.config.set(materialized="table")
    df = dbt.ref("dim_customers")
    df["customer_key"] = 1

    return df