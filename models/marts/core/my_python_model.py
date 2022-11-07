import snowflake.snowpark.types as T
import snowflake.snowpark.functions as F
import numpy
def register_udf_add_random():
    add_random = F.udf(
        # use 'lambda' syntax, for simple functional behavior
        lambda x: x + numpy.random.normal(),
        return_type=T.FloatType(),
        input_types=[T.FloatType()]
    )
    return add_random

def model(dbt, session):
    dbt.config(
        materialized = "table",
        packages = ["numpy"]
    )

temps_df = dbt.ref("fct_orders")

add_random = register_udf_add_random()

# warm things up, who knows by how much
df = temps_df.withColumn("order_key", add_random("degree"))

return df