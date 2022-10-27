import ...

def model(dbt, session):

    my_sql_model_df = dbt.ref("dim_customers")

    final_df = my_sql_model_df  # stuff you can't write in SQL!

    return final_df