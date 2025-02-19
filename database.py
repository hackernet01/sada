import sqlite3

conn = sqlite3.connect("keys.db")
cursor = conn.cursor()

# Create table for 24-digit keys
cursor.execute("""
CREATE TABLE IF NOT EXISTS premium_keys (
    key TEXT PRIMARY KEY,
    status TEXT DEFAULT 'unused'
)
""")
conn.commit()
conn.close()

print("✅ Database setup completed!")
