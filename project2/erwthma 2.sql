SELECT DISTINCT
    d.last_name, m.title
FROM
    actor a,
    role r,
    movie m,
    movie_has_director md,
    director d,
    movie_has_genre mg
WHERE
    a.last_name = 'Allen'
        AND a.actor_id = r.actor_id
        AND r.movie_id = m.movie_id
        AND m.movie_id = md.movie_id
        AND md.director_id = d.director_id
        AND m.movie_id IN (SELECT 
            mg.movie_id
        FROM
            movie_has_genre mg
        GROUP BY mg.movie_id
        HAVING COUNT(mg.genre_id) > 1);


#2. Βρείτε τα επώνυμα των σκηνοθετών και τους τίτλους των ταινιών που έχουν
#σκηνοθετήσει, στις οποίες παίζει ηθοποιός με επώνυμο “Allen”, με την
#προϋπόθεση ότι αυτός ο σκηνοθέτης έχει σκηνοθετήσει τουλάχιστον δύο
#διαφορετικά είδη ταινιών.