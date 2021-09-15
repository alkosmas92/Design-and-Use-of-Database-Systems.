SELECT 
    mg1.genre_id, r.actor_id, COUNT(DISTINCT r.movie_id)
FROM
    role r,
    movie_has_genre mg1,
    movie_has_genre mg2,
    movie_has_director md
WHERE
    r.movie_id = mg1.movie_id
        AND mg1.movie_id = md.movie_id
        AND md.movie_id = mg2.movie_id
GROUP BY md.director_id
HAVING COUNT(DISTINCT mg2.genre_id)
ORDER BY mg1.genre_id , r.actor_id;

#10. Για κάθε είδος και ηθοποιό, βρείτε τον αριθμό των ταινιών του είδους που έχει
#παίξει ο ηθοποιός, εφόσον οι ταινίες αυτές συνολικά δεν έχουν σκηνοθέτη που
#έχει σκηνοθετήσει και κάποιο άλλο είδος εκτός από αυτό.

#"Έστω ο ηθοποιός a, και το είδος της ταινίας g και ο a παίζει σε Ν ταινίες είδους g. Αυτό που ζητείται είναι ο
#αριθμός των ταινιών Μ από τις Ν (όπου Μ<=Ν) οι οποίες έχουν σκηνοθέτη που 
#εχει σκηνοθετήσει μόνο ταινίες είδους g.