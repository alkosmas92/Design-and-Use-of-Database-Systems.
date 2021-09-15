SELECT 
    m.title,
    g.genre_name AS genre,
    COUNT(DISTINCT md.director_id) AS directors
FROM
    movie m,
    movie_has_genre mg1,
    movie_has_genre mg2,
    genre g,
    movie_has_director md
WHERE
    m.movie_id = mg1.movie_id
        AND mg1.genre_id = g.genre_id
        AND mg2.movie_id = md.movie_id
        AND mg1.genre_id = mg2.genre_id
GROUP BY m.title
HAVING COUNT(DISTINCT mg1.genre_id) = 1
ORDER BY m.title;

#7. Για κάθε ταινία που έχει ακριβώς ένα είδος, βρείτε το είδος καθώς και τον αριθμό
#των σκηνοθετών που έχουν σκηνοθετήσει αυτό το είδος.