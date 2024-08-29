from google.cloud import firestore
import csv

def csv_to_dic(file):
    # read csv file to a list of dictionaries
    with open(file, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def main():
    data = csv_to_dic("b/location.csv")
        
    # Right now, this runs slowly as it is doing it row by row
    # If I had more time, I would look into doing this as a batch process 
    db = firestore.Client(project="ferg-sandbox-gcp")
    for item in data:
        db.collection("location").document(item["country"]).set(item)
        print(item)


if __name__ == '__main__':
    main()