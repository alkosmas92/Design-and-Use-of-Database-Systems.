SELECT DISTINCT
    m.title
FROM
    actor a,
    role r,
    movie m,
    movie_has_genre mg,
    genre g
WHERE
    a.last_name = 'Allen'
        AND a.actor_id = r.actor_id
        AND r.movie_id = m.movie_id
        AND g.genre_name = 'Comedy'
        AND g.genre_id = mg.genre_id
        AND m.movie_id = mg.movie_id;


#1. Βρείτε τους τίτλους των ταινιών που παίζει ηθοποιος με επώνυμο “Allen” και το
#είδος της ταινίας είναι “Comedy”.