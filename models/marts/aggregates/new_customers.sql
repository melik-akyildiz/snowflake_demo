select *
from {{ metrics.metric(
            metric_name='new_customers',
            grain='month',
            dimensions=['phone_number']
    ) }}

