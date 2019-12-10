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

CREATE OR REPLACE PROCEDURE drop_all_Tables()
LANGUAGE plpgsql
AS $$
BEGIN
    DROP TABLE "movie_genre" CASCADE;
    DROP TABLE "roles" CASCADE;
    DROP TABLE "genres" CASCADE;
    DROP TABLE "actors" CASCADE;
    DROP TABLE "movies" CASCADE;

    RAISE NOTICE 'Were dropped tables: movie_genre, roles, genres, mactors, movies';
END;
$$;

CREATE OR REPLACE PROCEDURE clear_all_Tables()
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM "movie_genre" CASCADE;
    ALTER SEQUENCE "movie_genre_id_seq" restart with 1;
    DELETE FROM "roles" CASCADE;
    ALTER SEQUENCE "roles_id_seq" restart with 1;
    DELETE FROM "genres" CASCADE;
    ALTER SEQUENCE "genres_id_seq" restart with 1;
    DELETE FROM "actors" CASCADE;
    ALTER SEQUENCE "actors_id_seq" restart with 1;
    DELETE FROM "movies" CASCADE;
    ALTER SEQUENCE "movie_id_seq" restart with 1;

    RAISE NOTICE 'Were cleaned tables: movie_genre, roles, genres, mactors, movies';
END
$$;

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
    RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table1;
    DELETE FROM genres WHERE genres.id = ID_to_delete;
    RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table3;
    return 1;
  END IF;
  IF tblName = table4 THEN
      DELETE FROM roles WHERE roles.a_id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table2;
      DELETE FROM actors WHERE actors.id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table4;
      return 1;
  END IF;
  IF tblName = table5 THEN
      DELETE FROM roles WHERE roles.f_id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table2;
      DELETE FROM movies WHERE movies.id = ID_to_delete;
      RAISE NOTICE 'The (%) row was removed from ( %) !' , ID_to_delete, table5;
      return 1;
  END IF;
  return 0;
END
$func$ LANGUAGE plpgsql;


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
