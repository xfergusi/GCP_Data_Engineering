from google.cloud import bigquery


def create_external_table(full_table_id, source_uri, source_format):
    try:
        # Construct a BigQuery client object.
        client = bigquery.Client()

        # table_id = "ferg-sandbox-gcp.learndata.locations"
        table_id = full_table_id

        # external_source_format = "CSV"
        external_source_format = source_format

        source_uris = [
            # "gs://location-ferg/location.csv"
            source_uri
        ]

        external_config = bigquery.ExternalConfig(external_source_format)
        external_config.source_uris = source_uris
        external_config.autodetect = True

        table = bigquery.Table(table_id)
        # Set the external data configuration of the table
        table.external_data_configuration = external_config
        table = client.create_table(table)  # Make an API request.

        print(
            f"Created table with external source format {table.external_data_configuration.source_format}"
        )
        return True
    except Exception as e:
        print(e)
        return False


def main():
    if create_external_table("ferg-sandbox-gcp.learndata.locations", "gs://location-ferg/location.csv", "CSV" ):
        print("we did it")
    else:
        print("failure")


if __name__ == '__main__':
    main()