def model(dbt, session):
    df = dbt.ref("fct_orders")
    target_df =dbt.this()

    target_df['order_key'] = df['order_key']

    return target_df