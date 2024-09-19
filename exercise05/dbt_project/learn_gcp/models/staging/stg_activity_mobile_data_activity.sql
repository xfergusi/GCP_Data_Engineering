{{ config(materialized='table') }}

select * from {{ source('learn_gcp', 'activity_mobile_data_activity') }}