import helpers.db_manage as db


inputs = ['email','password']
columns= (','.join(inputs))


with db.query as cur:

    cur.execute("SELECT "+ columns +" FROM users;")
    print(cur.fetchall())
