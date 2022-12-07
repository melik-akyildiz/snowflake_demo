def model(dbt, session):

               # these are DAG-aware, and return dataframes
               dim_all_learners = dbt.ref("python_model_table")
               source_users = dbt.source("tpch", "customer")

               sample_command = dim_all_learners.limit(1)
                                  # .filter(col("o_orderkey"=="1"))


               # your final 'select' statement
               df = sample_command.select("*")


               return df