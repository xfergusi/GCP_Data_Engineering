{{ config(materialized='table') }}

select 
subscription_id,
first_name,
last_name,
salutation,
age,
gender,
mobile,
email,
address_id

from {{ ref('stg_subscriber') }}

