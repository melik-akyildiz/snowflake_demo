{% snapshot orders_snapshot_check_2 %}

    {{
        config(
          target_schema='PUBLIC',
          strategy='check',
          unique_key='O_ORDERKEY',
          check_cols=['O_ORDERSTATUS'],
        )
    }}

select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}