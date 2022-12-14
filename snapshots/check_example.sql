{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='PUBLIC',
          strategy='check',
          unique_key='ORDERKEY',
          check_cols=['ORDERSTATUS'],
        )
    }}

select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}