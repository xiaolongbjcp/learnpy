

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')

if os.path.isfile(db_file):
	os.remove(db_file)

conn = sqlite3.connect(db_file)

cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')

cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")

cursor.close()

conn.commit()
conn.close()


def get_score_in(low, high):
	
	conn = sqlite3.connect(db_file)

	cursor = conn.cursor()
	cursor.execute(r"select name from user where score between ? and ?", (low, high))

	result = cursor.fetchall()

	cursor.close()

	conn.close()

	print (result)

	result = list(map(lambda x: x[0], result))
	
	print (result)

	return result

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Adam', 'Bart', 'Lisa'], get_score_in(60, 100)

print('Pass')
