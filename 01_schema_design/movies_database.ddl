 DROP TABLE IF EXISTS "content"."genre_film_work";
 DROP TABLE IF EXISTS "content"."person_film_work";
 DROP TABLE IF EXISTS "content"."person";
 DROP TABLE IF EXISTS "content"."film_work";
 DROP TABLE IF EXISTS "content"."genre";
 DROP SCHEMA IF EXISTS "content";

CREATE SCHEMA IF NOT EXISTS "content";
ALTER ROLE app SET search_path TO "content", "public";

CREATE TABLE IF NOT EXISTS "content"."genre" (
    "id" uuid NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "created" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    "modified" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX "genre_name_idx" ON "content"."genre"("name");
CREATE UNIQUE INDEX "uneque_genre_name_idx" ON "content"."genre"("name");

CREATE TABLE IF NOT EXISTS "content"."film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "description" TEXT,
    "creation_date" DATE,
    "rating" FLOAT CHECK ("rating" >= 0),
    "type" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    "modified" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX "film_work_creation_date_idx" ON "content"."film_work"("creation_date");
CREATE INDEX "filmwork_title_idx" ON "content"."film_work"("title");
CREATE INDEX "filmwork_type_idx" ON "content"."film_work"("type");


CREATE TABLE IF NOT EXISTS "content"."person" (
    "id" uuid NOT NULL PRIMARY KEY,
    "full_name" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    "modified" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS "content"."person_film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "person_id" uuid NOT NULL REFERENCES "content"."person"("id"),
    "film_work_id" uuid NOT NULL REFERENCES "content"."film_work"("id"),
    "role" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE UNIQUE INDEX "unique_film_work_person_role_idx" ON "content"."person_film_work"("film_work_id", "person_id", "role");
CREATE INDEX "film_work_person_idx" ON "content"."person_film_work"("film_work_id", "person_id");


CREATE TABLE IF NOT EXISTS "content"."genre_film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "film_work_id" uuid NOT NULL REFERENCES "content"."film_work"("id"),
    "genre_id" uuid NOT NULL REFERENCES "content"."genre"("id"),
    "created" TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE UNIQUE INDEX "unique_genre_film_work" ON "content"."genre_film_work"("genre_id", "film_work_id");
