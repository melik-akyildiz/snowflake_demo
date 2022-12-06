def model(dbt, session):
    df = dbt.ref("dim_customers")
    target_df =dbt.this()

    target_df['customer_key'] = df['customer_key']

    return target_df