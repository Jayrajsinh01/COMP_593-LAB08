import sqlite3
from random import randint, choice
from faker import Faker

# Connecting to  database
con = sqlite3.connect('social_network.db')
cur = con.cursor()

# table "relationships" created
create_relationship_query = """
    CREATE TABLE relationships (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people(id),
        FOREIGN KEY (person2_id) REFERENCES people(id)
    );
"""
cur.execute(create_relationship_query)
add_relation_query = """
INSERT INTO relationships
(
    person1_id,
    person2_id,
    type,
    start_date
)
VALUES (?, ?, ?, ?);
"""
# Insert 100 fake relationships
fake = Faker()

    # selecting random first person
person1_id = randint(1, 100)
    # selecting random second person
person2_id = randint(1, 100)
while person2_id == person1_id:
        person2_id = randint(1, 100)
    # selecting random relationship
relation = choice(('spouse', 'friend', 'relative','partner'))
    # selecting random start date 
start_date = fake.date_between(start_date='-50y', end_date='today')
    # Creating data for the new relationship
new_relationship = (person1_id, person2_id, relation, start_date)
    # Inserting the new relationship into the database
cur.execute(add_relation_query, new_relationship)

con.commit()
con.close()