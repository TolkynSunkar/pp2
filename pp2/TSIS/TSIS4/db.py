import psycopg2
from config import DB_CONFIG

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

def get_player_id(username):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    r = cur.fetchone()

    if r:
        pid = r[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    conn.close()
    return pid

def save_score(username, score, level):
    pid = get_player_id(username)
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO game_sessions(player_id, score, level_reached) VALUES (%s,%s,%s)",
        (pid, score, level)
    )

    conn.commit()
    conn.close()

def get_top10():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    rows = cur.fetchall()
    conn.close()
    return rows

def get_best(username):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT COALESCE(MAX(g.score),0)
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username=%s
    """, (username,))

    best = cur.fetchone()[0]
    conn.close()
    return best