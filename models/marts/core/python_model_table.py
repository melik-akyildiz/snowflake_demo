def model(dbt, session):
    df = dbt.ref('dim_customers')
    return df