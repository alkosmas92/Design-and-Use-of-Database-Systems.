SELECT 
    mg1.genre_id AS genre_1,
    mg2.genre_id AS genre_2,
    COUNT(DISTINCT md1.director_id) AS directors
FROM
    movie_has_genre mg1,
    movie_has_genre mg2,
    movie_has_director md1,
    movie_has_director md2
WHERE
    mg1.genre_id < mg2.genre_id
        AND md1.movie_id = mg1.movie_id
        AND md2.movie_id = mg2.movie_id
        AND md1.director_id = md2.director_id
GROUP BY mg1.genre_id , mg2.genre_id
ORDER BY mg1.genre_id , mg2.genre_id;




#9. Για κάθε ζεύγος ειδών (genre_id’s) ταινιών, βρείτε τον αριθμό των σκηνοθετών
#που έχουν σκηνοθετήσει ταινίες και των δύο ειδών.