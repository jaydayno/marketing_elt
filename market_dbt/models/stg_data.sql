with stage_data as (

    select * from {{ ref('raw_data') }}

)

select 

    row_id as sale_id,

    customer_id,
    customer_name,
    region,
    country,
    state,
    city,
    postal_code,

    order_id,
    order_date,
    segment,
    ship_date,
    ship_mode

    product_id,
    product_name,
    
    {{ dbt_utils.generate_surrogate_key(['category', 'sub_category']) }} as category_id,
    category,
    sub_category,

    sales,
    quantity,
    discount,
    profit

from stage_data
    
