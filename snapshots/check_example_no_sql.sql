{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='PUBLIC',
          strategy=['check','timestamp'],
          unique_key='O_ORDERKEY',
          check_cols=['O_ORDERSTATUS',all],
        )
    }}

select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}