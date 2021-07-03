with sales as (
    select * from {{ source('iowa_liquor_retail_sales', 'sales') }}
),

totals as (
    select
        extract(year from date) as year_of_purchase,
        extract(month from date) as month_of_purchase,
        item_description,
        round(sum(volume_sold_gallons), 2) as gallons_purchased
    from sales
    group by 1, 2, 3
)

select * from totals
