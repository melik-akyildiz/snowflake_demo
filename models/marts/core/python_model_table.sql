{{
    config(
        materialized = 'table',
        transient=false
    )
}}

with PYTHON_MODEL_TABLE as (

    select * from {{ ref('stg_tpch_customers') }}

),
nation as (

    select * from {{ ref('stg_tpch_nations') }}
),
region as (

    select * from {{ ref('stg_tpch_regions') }}

),
final as (
    select
        PYTHON_MODEL_TABLE.customer_key,
        PYTHON_MODEL_TABLE.name,
        PYTHON_MODEL_TABLE.address,
        {# nation.nation_key as nation_key, #}
        nation.name as nation,
        {# region.region_key as region_key, #}
        region.name as region,
        PYTHON_MODEL_TABLE.phone_number,
        PYTHON_MODEL_TABLE.account_balance,
        PYTHON_MODEL_TABLE.market_segment
    from
        PYTHON_MODEL_TABLE
        inner join nation
            on PYTHON_MODEL_TABLE.nation_key = nation.nation_key
        inner join region
            on nation.region_key = region.region_key
)
select
    *
from
    final
order by
    customer_key