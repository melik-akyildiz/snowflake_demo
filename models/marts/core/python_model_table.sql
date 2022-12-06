{{
    config(
        materialized = 'table'
    )
}}
with part as (

    select * from {{ref('dim_customers')}}

)select
     *
 from
     PYTHON_MODEL_TABLE
 order by
     customer_key