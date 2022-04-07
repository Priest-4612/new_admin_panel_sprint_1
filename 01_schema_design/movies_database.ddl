CREATE SCHEMA IF NOT EXISTS content;
ALTER ROLE app SET search_path TO content, public;

CREATE TABLE IF NOT EXISTS "content"."film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "description" TEXT,
    "creation_date" DATE,
    "rating" FLOAT CHECK ("rating" >= 0),
    "type" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE,
    "modified" TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS "content"."genre" (
    "id" uuid NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "created" TIMESTAMP WITH TIME ZONE,
    "modified" TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS "content"."person" (
    "id" uuid NOT NULL PRIMARY KEY,
    "full_name" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE,
    "modified" TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS "content"."person_film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "person_id" uuid NOT NULL,
    "film_work_id" uuid NOT NULL,
    "role" TEXT NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS "content"."genre_film_work" (
    "id" uuid NOT NULL PRIMARY KEY,
    "film_work_id" uuid NOT NULL,
    "genre_id" uuid NOT NULL,
    "created" TIMESTAMP WITH TIME ZONE
);

-- Создаю связи между таблицами
ALTER TABLE "content"."person_film_work"
ADD CONSTRAINT "person_film_work_film_work_id"
FOREIGN KEY ("film_work_id")
REFERENCES "content"."film_work" ("id")
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "content"."person_film_work"
ADD CONSTRAINT "person_film_work_person_id"
FOREIGN KEY ("person_id")
REFERENCES "content"."person" ("id")
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "content"."genre_film_work"
ADD CONSTRAINT "genre_film_work_film_work_id"
FOREIGN KEY ("film_work_id")
REFERENCES "content"."film_work" ("id")
DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE "content"."genre_film_work"
ADD CONSTRAINT "genre_film_work_genre_id"
FOREIGN KEY ("genre_id")
REFERENCES "content"."genre" ("id")
DEFERRABLE INITIALLY DEFERRED;

-- Создаю ограничения для уникальных значений
ALTER TABLE "content"."genre"
ADD CONSTRAINT "uneque_genre_name"
UNIQUE ("name");

ALTER TABLE "content"."person_film_work"
ADD CONSTRAINT "unique_film_work_person"
UNIQUE ("film_work_id", "person_id");

ALTER TABLE "content"."genre_film_work"
ADD CONSTRAINT "unique_genre_film_work"
UNIQUE ("genre_id", "film_work_id");

-- Создаю индексы
CREATE INDEX "film_work_title" ON "content"."film_work" ("title");
CREATE INDEX "film_work_creation_date" ON "content"."film_work" ("creation_date");
CREATE INDEX "film_work_type" ON "content"."film_work" ("type");

CREATE INDEX "person_film_work_film_work_id" ON "content"."person_film_work" ("film_work_id");
CREATE INDEX "person_film_work_person_id" ON "content"."person_film_work" ("person_id");
CREATE INDEX "genre_film_work_film_work_id" ON "content"."genre_film_work" ("film_work_id");
CREATE INDEX "genre_film_work_genre_id" ON "content"."genre_film_work" ("genre_id");
