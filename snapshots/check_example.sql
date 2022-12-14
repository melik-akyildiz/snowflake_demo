{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='PUBLIC',
          strategy='check',
          unique_key='order_item_key',
          check_cols=['order_item_status_code'],
        )
    }}

select * from {{ source('tpch', 'fct_order_items') }}

    {% endsnapshot %}