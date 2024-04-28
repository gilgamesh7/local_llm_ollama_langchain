from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
artist_list = db.run("SELECT * FROM Artist LIMIT 10;")
print(artist_list)