CREATE VIEW actors AS
    SELECT 
        a.first_name,
        a.last_name,
        COUNT(DISTINCT md.director_id) AS directors
    FROM
        actor a,
        role r,
        movie_has_director md
    WHERE
        a.actor_id = r.actor_id
            AND r.movie_id = md.movie_id
    GROUP BY a.first_name , a.last_name
    HAVING COUNT(DISTINCT r.movie_id) = 3;
    SELECT * FROM actors;


#6. Για κάθε ηθοποιό που έχει παίξει σε ακριβώς 3 ταινίες, βρείτε το όνομα και το
#επώνυμο του καθώς και τον αριθμό των διαφορετικών σκηνοθετών που έχουν οι
#ταινίες του.