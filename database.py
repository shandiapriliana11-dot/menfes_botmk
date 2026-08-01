import sqlite3

db = sqlite3.connect("menfess.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS menfess (
    group_msg_id INTEGER PRIMARY KEY,
    sender_id INTEGER
)
""")

db.commit()


def save(group_msg_id, sender_id):
    cursor.execute(
        "INSERT OR REPLACE INTO menfess VALUES (?, ?)",
        (group_msg_id, sender_id)
    )
    db.commit()


def get_sender(group_msg_id):
    cursor.execute(
        "SELECT sender_id FROM menfess WHERE group_msg_id=?",
        (group_msg_id,)
    )
    data = cursor.fetchone()
    return data[0] if data else None