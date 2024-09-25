{{ config(materialized='table') }}

select * 
from {{ ref('stg_activity_mobile_data_activity') }}