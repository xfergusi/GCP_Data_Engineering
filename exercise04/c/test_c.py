import pytest
import bqcreate
from google.cloud import bigquery

# @pytest.fixture
def test_setup():
    client = bigquery.Client()
    table_id = "ferg-sandbox-gcp.learndata.locations"
    # If the table does not exist, delete_table raises
    client.delete_table(table_id, not_found_ok=True)  # Make an API request.
    print("Deleted table '{}'.".format(table_id))
    

def test_creating():
    bool = bqcreate.create_external_table("ferg-sandbox-gcp.learndata.locations", "gs://location-ferg/location.csv", "CSV" )
    assert bool is True
    print("truth")