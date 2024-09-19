{{ config(materialized='table') }}

select * from {{ source('learn_gcp', 'activity_voice_call_record') }}