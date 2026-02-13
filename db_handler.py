import psycopg2
from datetime import datetime

# ✅ PostgreSQL connection (replace with your credentials if needed)
try:
    conn = psycopg2.connect(
        host="localhost",
        database="interview_db",
        user="postgres",
        password="admin123",
        port="5432"
    )
    print("✅ Connected to PostgreSQL")
except Exception as e:
    print("❌ Error connecting to PostgreSQL:", e)

# ✅ Save a single record to the DB
def save_record(name, transcript, feedback):
    try:
        print("⚙️ Saving to DB...")
        print("Name:", name)
        print("Transcript (short):", transcript[:50])
        print("Feedback (short):", feedback[:50])
        
        cur = conn.cursor()
        query = """
        INSERT INTO interview_records (name, transcript, feedback, created_at)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (name, transcript, feedback, datetime.now()))
        conn.commit()
        cur.close()
        print("✅ Record saved.")
    except Exception as e:
        print("❌ Error saving record:", e)



# ✅ Get all saved interview records
def get_all_records():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM interview_records ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        print("❌ Error fetching records:", e)
        return []
