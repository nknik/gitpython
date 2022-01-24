"""# DATABASE:

Q.30 Design and Implement any Database Application using Python"""


import sqlite3

conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute(
    """
CREATE TABLE Counts (org TEXT, count INTEGER)"""
)
list(cur.execute("""INSERT INTO Counts (org, count) VALUES (11, 1)"""))
list(cur.execute("""INSERT INTO Counts (org, count) VALUES (12, 21)"""))
list(cur.execute("""INSERT INTO Counts (org, count) VALUES (11, 123)"""))
cur.execute("SELECT * FROM Counts")
rows = cur.fetchall()
for i in rows:
    print(i)
# row = cur.fetchone()
conn.commit()
"""
==========================================OUTPUT===========================

('11', 1)
('12', 21)
('11', 123)
==========================================OUTPUT===========================

"""