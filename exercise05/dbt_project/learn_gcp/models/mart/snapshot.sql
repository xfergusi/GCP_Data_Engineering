{{ config(materialized='table') }}

with subscribers as (

select distinct subscription_id from {{ ref('int_subscriber') }} 

),


voice_data as (

select subscription_id
, MIN(actual_duration) as min_voice_duration
, MAX(actual_duration) as max_voice_duration
from {{ ref('int_activity_voice_call_record') }}
group by subscription_id 

),

sms_data as (

select subscription_id
, COUNT(*) as sms_counts
from {{ ref('int_activity_sms_record') }}
group by subscription_id 

),


mobile_data as (

select subscription_id
, SUM(safe_cast( uplink_volume AS INT64 ) ) as total_upload_volume
, SUM(safe_cast( downlink_volume AS INT64 ) ) as total_download_volume
from {{ ref('int_activity_mobile_data_activity')}}
group by subscription_id 

)



select 
sub.subscription_id
, voi.min_voice_duration
, voi.max_voice_duration
, sms.sms_counts
, mob.total_upload_volume
, mob.total_download_volume
from subscribers sub
left outer join voice_data voi on sub.subscription_id = voi.subscription_id
left outer join sms_data sms on sub.subscription_id = sms.subscription_id
left outer join mobile_data mob on sub.subscription_id = mob.subscription_id