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



select * from Movie_Info;
select * from Actors_Info;
select * from Cast_Info;
select * from Movie_Genre_Info;
select * from Genre_Info;
