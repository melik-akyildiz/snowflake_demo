def model(dbt, session):

    df = dbt.ref('python_model_table')
    target_df =dbt.this()

    target_df['customer_key'] = df['customer_key']

return target_df