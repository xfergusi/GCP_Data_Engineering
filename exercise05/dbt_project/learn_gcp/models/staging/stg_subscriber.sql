{{ config(materialized='table') }}

select * from {{ ref('subscriber') }}

