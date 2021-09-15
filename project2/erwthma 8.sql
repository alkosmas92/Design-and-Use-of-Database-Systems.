SELECT 
    a.actor_id
FROM
    actor a,
    role r,
    movie m,
    movie_has_genre mg,
    genre g
WHERE
    a.actor_id = r.actor_id
        AND r.movie_id = m.movie_id
        AND m.movie_id = mg.movie_id
        AND g.genre_id = mg.genre_id
GROUP BY a.actor_id
HAVING COUNT(g.genre_id) > 20;



#8. Βρείτε τους κωδικούς των ηθοποιών που έχουν παίξει σε όλα τα είδη ταινιών
#(ηθοποιοί-χαμαιλέοντες!).