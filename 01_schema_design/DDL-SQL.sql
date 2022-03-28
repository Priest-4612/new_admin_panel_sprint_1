CREATE TABLE IF NOT Exists content.film_work ( 
    id uuid PRIMARY KEY, 
    title TEXT NOT NULL, 
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
)