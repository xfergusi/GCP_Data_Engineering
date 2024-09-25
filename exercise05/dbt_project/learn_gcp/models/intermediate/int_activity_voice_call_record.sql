{{ config(materialized='table') }}

select * 
from {{ ref('stg_activity_voice_call_record') }}
