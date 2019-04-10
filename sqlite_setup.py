import sqlite3

conn = sqlite3.connect('goldengators.db')

c = conn.cursor()

# c.execute("""CREATE TABLE strategies(
#             townhall INTEGER,
#             name TEXT,
#             description TEXT,
#             reference TEXT
#     )""")

# c.execute("""INSERT INTO strategies VALUES (
#             9,
#             'gobolaloon',
#             'GobolavaLoon is a variant of laloon using golems, bowlers, lavahound and loons.',
#             'https://www.youtube.com/watch?v=3ZnuDmeu-vY'
#         )""")
# somename = "laloon"
# c.execute("SELECT * FROM strategies WHERE name='"+somename+"'")
#
# data = c.fetchone()  # list
# print(data)
# c.execute("SELECT * FROM strategies")
# print(c.fetchall())
# c.execute("DROP TABLE strategies")

# c.execute("""CREATE TABLE coclinks(
#             discordID INTEGER,
#             coctag TEXT
#     )""")
# c.execute("""CREATE TABLE notes(
#             title TEXT,
#             description TEXT
#     )""")
conn.commit()

conn.close()

