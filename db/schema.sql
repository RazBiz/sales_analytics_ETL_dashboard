CREATE TABLE IF NOT EXISTS stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    store_id INT REFERENCES stores(store_id),
    date DATE,
    product VARCHAR(100),
    quantity INT,
    unit_price NUMERIC,
    total_price NUMERIC
);