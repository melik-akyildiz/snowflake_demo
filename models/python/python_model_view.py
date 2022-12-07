def model(dbt, session):

           dbt.config(
               materialized='table'
           )

           # these are DAG-aware, and return dataframes
           dim_all_learners = dbt.ref("orders")
           source_users = dbt.source("tpch", "customer")

           #sample_command = dim_all_learners.limit(1)
                              # .filter(col("o_orderkey"=="1"))


           # your final 'select' statement
           #df = dim_all_learners.select("*")

           target_df['o_orderkey'] = dim_all_learners['o_orderkey']

return target_df