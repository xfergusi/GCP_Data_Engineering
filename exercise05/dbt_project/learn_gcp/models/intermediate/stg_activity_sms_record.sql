{{ config(materialized='table') }}

select * from {{ source('learn_gcp', 'activity_sms_record') }}