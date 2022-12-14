{% snapshot orders_snapshot_check %}


select * from {{ source('tpch', 'orders') }}

    {% endsnapshot %}