{{ config(materialized='view') }}

select *
from marketingproj.store.raw_data_store