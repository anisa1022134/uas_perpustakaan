-- Aktifkan ekstensi Citus
CREATE EXTENSION IF NOT EXISTS citus;

-- Tambahkan node worker
SELECT * FROM master_add_node('worker1', 5432);
SELECT * FROM master_add_node('worker2', 5432);

-- Distribusi tabel
SELECT create_distributed_table('users', 'user_id');
SELECT create_distributed_table('books', 'book_id');
SELECT create_distributed_table('borrow_records', 'user_id');
