def model(dbt,session):

           dbt.config(
               materialized='table'
           )

           # these are DAG-aware, and return dataframes
           dim_all_learners = dbt.ref("orders")
           source_users = dbt.source("tpch", "customer")

           sample_command = dim_all_learners.limit(1)
                              # .filter(col("o_orderkey"=="1"))


           # your final 'select' statement
           df = sample_command.select("*")

            df = df.filter(df.updated_at >= session.sql(max_from_this).collect()[0][0])

                   # or only rows from the past 3 days
                   df = df.filter(df.updated_at >= F.dateadd("day", F.lit(-3), F.current_timestamp()))

return df