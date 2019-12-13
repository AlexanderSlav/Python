
-- views
Create Or Replace View Movie_Info As
Select * From movies;

Create Or Replace View Actors_Info As
Select * From actors;

Create Or Replace View Cast_Info As
Select * From roles;

Create Or Replace View Movie_Genre_Info As
Select * From movie_genre;

Create Or Replace View Genre_Info As
Select * From genres;


-- drop and clear all tables
CREATE OR REPLACE PROCEDURE drop_all_Tables()
LANGUAGE plpgsql
AS $$
BEGIN
    DROP TABLE "movie_genre" CASCADE;
    DROP TABLE "roles" CASCADE;
    DROP TABLE "genres" CASCADE;
    DROP TABLE "actors" CASCADE;
    DROP TABLE "movies" CASCADE;

    RAISE NOTICE 'Were dropped tables: movie_genre, roles, genres, actors, movies';
END;
$$;

CREATE OR REPLACE PROCEDURE clear_all_Tables()
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM movie_genre CASCADE;
    ALTER SEQUENCE movie_genre_id_seq restart with 1;
    DELETE FROM roles CASCADE;
    ALTER SEQUENCE roles_id_seq restart with 1;
    DELETE FROM genres CASCADE;
    ALTER SEQUENCE genres_id_seq restart with 1;
    DELETE FROM actors CASCADE;
    ALTER SEQUENCE actors_id_seq restart with 1;
    DELETE FROM movies  CASCADE;
    ALTER SEQUENCE movies_id_seq restart with 1;

    RAISE NOTICE 'Were cleaned tables: movie_genre, roles, genres, mactors, movies';
END
$$;


-- delete by non primary key and primary key

CREATE OR REPLACE FUNCTION delete_data_by_name(tblname Varchar(50), object_name Varchar(80))
returns integer
AS
$func$
DECLARE
    DECLARE table1 VARCHAR     := 'movie_genre';
    DECLARE table2 VARCHAR     := 'roles';
    DECLARE table3 VARCHAR     := 'genres';
    DECLARE table4 VARCHAR     := 'actors';
    DECLARE table5 VARCHAR     := 'movies';
    DECLARE search_index integer := -1;
BEGIN
  IF tblName = table1 or  tblName = table2 or tblName = table3 THEN
    RAISE NOTICE 'Tables ( % % %) have no field name !' ,  table1, table2, table3;
    return 0;
  END IF;
  IF tblName = table4 THEN
    select getId_by_Name(tblname, object_name) into search_index;
    RAISE NOTICE 'Found  (%) this index', search_index;
    DELETE FROM roles WHERE roles.a_id = search_index;
    DELETE FROM actors WHERE actors.name = object_name;
    return 1;
  END IF;
  IF tblName = table5 THEN
    select getId_by_Name(tblname, object_name) into search_index;
    RAISE NOTICE 'Found  (%) this index', search_index;
    DELETE FROM roles WHERE roles.f_id = search_index;
    DELETE FROM movie_genre WHERE movie_genre.f_id = search_index;
    DELETE FROM movies WHERE movies.name = object_name;
    return 1;
  END IF;
  return 0;
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_data_by_ID(tblname Varchar(80), ID_to_delete Integer)
returns integer
AS
$func$
DECLARE
    DECLARE table1 VARCHAR     := 'movie_genre';
    DECLARE table2 VARCHAR     := 'roles';
    DECLARE table3 VARCHAR     := 'genres';
    DECLARE table4 VARCHAR     := 'actors';
    DECLARE table5 VARCHAR     := 'movies';
    DECLARE search_index integer := -1;
BEGIN
  IF tblName = table1  THEN
    DELETE FROM movie_genre WHERE movie_genre.id = ID_to_delete;
    RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table1;
    return 1;
  END IF;
  IF tblName = table2  THEN
    DELETE FROM roles WHERE roles.id = ID_to_delete;
    RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table2;
    return 1;
  END IF;
  IF tblName = table3 THEN
    DELETE FROM movie_genre WHERE movie_genre.g_id = ID_to_delete;
    RAISE NOTICE 'The dependence (%) row was removed from ( %) !' , ID_to_delete, table1;
    DELETE FROM genres WHERE genres.id = ID_to_delete;
    RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table3;
    return 1;
  END IF;
  IF tblName = table4 THEN
      DELETE FROM roles WHERE roles.a_id = ID_to_delete;
      RAISE NOTICE 'The dependence (%) row was removed from ( %) !' , ID_to_delete, table2;
      DELETE FROM actors WHERE actors.id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table4;
      return 1;
  END IF;
  IF tblName = table5 THEN
      DELETE FROM roles WHERE roles.f_id = ID_to_delete;
      RAISE NOTICE 'The dependence (%) row was removed from ( %) !' , ID_to_delete, table2;
      DELETE FROM movies WHERE movies.id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table5;
      return 1;
  END IF;
  return 0;
END
$func$ LANGUAGE plpgsql;

 -- help function
CREATE OR REPLACE FUNCTION getId_by_Name(table_name Varchar(80), object_name Varchar(80))
returns integer
AS
$func$
DECLARE
id integer;
actors_table VARCHAR  := 'actors';
movies_table VARCHAR  := 'movies';
BEGIN
  if table_name = actors_table THEN
    RAISE NOTICE 'Start searching in (%)', table_name;
    SELECT actors.id INTO id FROM actors WHERE actors.name = object_name;
  END IF;
  if table_name = movies_table THEN
      RAISE NOTICE 'Start searching in (%)', table_name;
      SELECT movies.id INTO id FROM movies WHERE movies.name = object_name;
  END IF;
  return id;
END
$func$ LANGUAGE plpgsql;

--Inser into tables

CREATE OR REPLACE function insertIntoMovie( Movie_Name varchar(35), year integer,budget float,
                                            fees float, country varchar(35), rate float, duration integer,
                                            plot_description varchar(80))
returns integer
AS
$func$
BEGIN
    INSERT INTO movies(name,year,budget,fees,country,rate,duration,plot_description)
     VALUES (Movie_Name,year,budget,fees,country,rate,duration,plot_description);
     return 1;
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE function insertIntoCast(f_id integer, a_id integer, role varchar(50))
returns integer
AS
$func$
BEGIN
    INSERT INTO roles(f_id, a_id, role)
     VALUES (f_id,a_id,role);
     return 1;
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE function insertIntoGenre(genre varchar(50))
returns integer
AS
$func$
BEGIN
    INSERT INTO genres(genre)
     VALUES (genre);
     return 1;
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE function insertIntoActors(name varchar(50),birth_date varchar,nationality varchar(50),gender varchar(50),age integer)
returns integer
AS
$func$
BEGIN
    INSERT INTO actors(name,birth_date,nationality,gender,age)
     VALUES (name,birth_date,nationality,gender,age);
     return 1;
END
$func$ LANGUAGE plpgsql;

CREATE OR REPLACE function insertIntoMovie_Genre(f_id integer,g_id integer)
returns integer
AS
$func$
BEGIN
    INSERT INTO movie_genre(f_id, g_id)
     VALUES (f_id,g_id);
     return 1;
END
$func$ LANGUAGE plpgsql;

-- Search by non primary key

CREATE OR REPLACE function Search_Actor_By_Name(object_name varchar)
returns table(
    id integer,
    name varchar,
    birth_date varchar,
    nationality varchar,
    gender varchar,
    age integer
)
AS $$
BEGIN
    return query select  actors.id, actors.name, actors.birth_date,
    actors.nationality, actors.gender, actors.age
    from actors where
    actors.name ILIKE object_name;
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE function Search_Actor_By_Nationality(input_nationality varchar)
returns table(
    id integer,
    name varchar,
    birth_date varchar,
    nationality varchar,
    gender varchar,
    age integer
)
AS $$
BEGIN
    return query select  actors.id, actors.name, actors.birth_date,
    actors.nationality, actors.gender, actors.age
    from actors where
    actors.nationality ILIKE input_nationality;
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE function Search_Actor_By_Age(input_age integer, comparison_type varchar)
returns table(
    id integer,
    name varchar,
    birth_date varchar,
    nationality varchar,
    gender varchar,
    age integer
)
AS $$
BEGIN
if comparison_type = 'equal' then
    return query select  actors.id, actors.name, actors.birth_date,
    actors.nationality, actors.gender, actors.age
    from actors where
    actors.age = input_age;
END IF;
if comparison_type = 'less' then
    return query select  actors.id, actors.name, actors.birth_date,
    actors.nationality, actors.gender, actors.age
    from actors where
    actors.age <= input_age;
END IF;
if comparison_type = 'greater' then
    return query select actors.id, actors.name, actors.birth_date,
    actors.nationality, actors.gender, actors.age
    from actors where
    actors.age >= input_age;
END IF;
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE function Search_Movie_By_Name(object_name varchar)
returns table(
    id integer,
    name varchar,
    year integer,
    budget float,
    fees float,
    country varchar,
    rate float,
    duration integer,
    plot_description varchar
)
AS $$
BEGIN
    return query select movies.id, movies.name, movies.year, movies.budget, movies.fees,
    movies.country, movies.rate, movies.duration, movies.plot_description
    from movies where
    movies.name ILIKE object_name;
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE function Search_Movie_By_Plot( input_plot_description varchar)
returns table(
    id integer,
    name varchar,
    year integer,
    budget float,
    fees float,
    country varchar,
    rate float,
    duration integer,
    plot_description varchar
)
AS $$
BEGIN
    return query select movies.id, movies.name, movies.year, movies.budget, movies.fees,
    movies.country, movies.rate, movies.duration, movies.plot_description
    from movies where movies.plot_description ILIKE input_plot_description;
END; $$
LANGUAGE plpgsql;

CREATE OR REPLACE function Search_Movie_By_Year(input_year integer, comparison_type varchar)
returns table(
    id integer,
    name varchar,
    year integer,
    budget float,
    fees float,
    country varchar,
    rate float,
    duration integer,
    plot_description varchar
)
AS $$
BEGIN
if comparison_type = 'equal' then
    return query select movies.id, movies.name, movies.year, movies.budget, movies.fees,
    movies.country, movies.rate, movies.duration, movies.plot_description
    from movies where movies.year = input_year;
END IF;
if comparison_type = 'less' then
    return query select movies.id, movies.name, movies.year, movies.budget, movies.fees,
    movies.country, movies.rate, movies.duration, movies.plot_description
    from movies where movies.year <= input_year;
END IF;
if comparison_type = 'greater' then
    return query select  movies.id, movies.name, movies.year, movies.budget, movies.fees,
    movies.country, movies.rate, movies.duration, movies.plot_description
    from movies where movies.year >= input_year;
END IF;
END; $$
LANGUAGE plpgsql;

-- Update row


CREATE OR REPLACE function Update_Fees(target_id integer, add_sum float)
returns void
AS $$
BEGIN
        UPDATE movies SET fees = movies.fees + add_sum
          WHERE movies.id = id;
END; $$
LANGUAGE plpgsql;


CREATE OR REPLACE function Update_Rate(target_id integer, change_value float, change_type varchar)
returns void
AS $$
declare
current_rate float;
BEGIN
select movies.rate into current_rate from movies where movies.id = target_id;
raise notice 'The current rate before %' , current_rate;
if change_type = '+' and ((current_rate + change_value) <= 10.0)
then
        UPDATE movies SET rate = rate + change_value
          WHERE  id = target_id;
end if;
if change_type = '-' and (current_rate - change_value >= 0.0)
then
        UPDATE movies SET rate = rate - change_value
          WHERE id = target_id ;
end if;
select movies.rate into current_rate from movies where movies.id = target_id;
raise notice 'The current  rate after %' , current_rate;

END; $$
LANGUAGE plpgsql;
