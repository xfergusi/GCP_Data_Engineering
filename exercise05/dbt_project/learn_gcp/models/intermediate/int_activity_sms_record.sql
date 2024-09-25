{{ config(materialized='table') }}

select * 
from {{ ref('stg_activity_sms_record') }}