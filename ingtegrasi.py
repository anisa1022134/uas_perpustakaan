import psycopg2
from pymongo import MongoClient
from redis import Redis

# Koneksi PostgreSQL
pg_conn = psycopg2.connect(
    host="master",
    port=5432,
    dbname="campus_library",
    user="postgres",
    password="postgres"
)
pg_cursor = pg_conn.cursor()

# Koneksi MongoDB
mongo_client = MongoClient("mongodb://mongo1:27017/")
mongo_db = mongo_client["campus_perpustakaan"]
book_reviews = mongo_db["book_reviews"]

# Koneksi Redis
redis_client = Redis(host="campus_redis", port=6379, decode_responses=True)

# Ambil data dari PostgreSQL
pg_cursor.execute("SELECT user_id, name FROM users;")
user_map = {uid: name for uid, name in pg_cursor.fetchall()}

pg_cursor.execute("SELECT book_id, title FROM books;")
book_map = {bid: title for bid, title in pg_cursor.fetchall()}

pg_cursor.execute("SELECT * FROM borrow_records;")
borrow_data = pg_cursor.fetchall()

# Gabungkan dan tampilkan
print("📚 HASIL GABUNGAN BORROW + REVIEW:\n")
for record in borrow_data:
    record_id, user_id, book_id, borrow_date, return_date = record
    user_name = user_map.get(user_id, f"User {user_id}")
    book_title = book_map.get(book_id, f"Buku {book_id}")

    print(f"{user_name} meminjam '{book_title}' pada {borrow_date}")

    # Cek review dari MongoDB
    review_doc = book_reviews.find_one({"book_id": book_id})
    if review_doc:
        print(f"  📝 Ringkasan: {review_doc.get('summary')}")
        for r in review_doc.get("reviews", []):
            reviewer_name = user_map.get(r['user_id'], f"User {r['user_id']}")
            print(f"    • {reviewer_name} beri rating {r['rating']} - \"{r['comment']}\"")
    else:
        print("  ⚠  Tidak ada review.")

    # Cek Redis (ketersediaan buku)
    availability = redis_client.get(f"book_availability:{book_id}")
    if availability is not None:
        print(f"  📦 Tersedia: {availability} buku")
    else:
       print("  ⚠️  Data ketersediaan tidak ditemukan di Redis.")
