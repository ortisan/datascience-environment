import uuid
import random
from faker import Faker
fake = Faker()


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="persondb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")


ROWS = int(10000)

if __name__ == "__main__":
  for i in range(0, ROWS):
      person_id = str(uuid.uuid4())
      sql = "INSERT INTO person (id, first_name, last_name) VALUES (%s, %s, %s);"
      val = (person_id, fake.first_name().replace("'", ''), fake.last_name().replace("'", ''))
      mycursor.execute(sql, val)
      
      phone_id = str(uuid.uuid4())
      sql = "INSERT INTO phone (id, person_id, phone_number) VALUES (%s, %s, %s);"
      val = (phone_id, person_id, fake.random_int(min=10000000, max=90000000))
      mycursor.execute(sql, val)

      address_id = str(uuid.uuid4())
      line1 = fake.street_name().replace("'", '')
      line2 = fake.secondary_address().replace("'", '')
      zip = fake.zipcode()
      city = fake.city().replace("'", '')
      country = fake.country().replace("'", '')
      sql = "INSERT INTO address (id, person_id, line1, line2, zipcode, city, country) VALUES (%s, %s, %s, %s, %s, %s, %s);"
      val = (address_id, person_id, line1, line2, zip, city, country)
      mycursor.execute(sql, val)
      
      # Randomize equal values
      insert_equal_value = random.randint(0, 100)
      if insert_equal_value < 50:
          for i in range(5):
            address_id2 = str(uuid.uuid4())
            sql = "INSERT INTO address (id, person_id, line1, line2, zipcode, city, country) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            val = (address_id2, person_id, line1, line2, zip, city, country)
            mycursor.execute(sql, val)
  mydb.commit()

