{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='PUBLIC',
          strategy='check',
          unique_key='order_key',
          check_cols=['status_code'],
        )
    }}

select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}