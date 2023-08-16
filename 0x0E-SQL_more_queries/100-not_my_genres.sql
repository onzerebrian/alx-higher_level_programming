-- list all genres not linked to the show Dexter
SELECT DISTINCT name FROM tv_genres g WHERE g.id NOT IN (SELECT genre_id FROM tv_show_genres sg LEFT JOIN tv_shows s ON s.id = sg.show_id WHERE s.title = 'Dexter') ORDER BY g.name ASC; 
