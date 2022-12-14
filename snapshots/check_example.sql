{% snapshot orders_snapshot_check %}

    {{
        config(
          target_schema='PUBLIC',
          strategy='check',
          unique_key='id',
          check_cols=['status_code'],
        )
    }}

select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}