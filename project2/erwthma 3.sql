SELECT DISTINCT
    a.last_name
FROM
    actor a,
    role r,
    movie m,
    movie_has_director md1,
    movie_has_director md2,
    movie_has_director md3,
    director d1,
    director d2,
    movie_has_genre mg2,
    movie_has_genre mg3
WHERE
    a.last_name = d1.last_name
        AND a.actor_id = r.actor_id
        AND r.movie_id = md1.movie_id
        AND md1.director_id = d1.director_id
        AND a.last_name <> d2.last_name
        AND r.movie_id = md2.movie_id
        AND md2.director_id = d2.director_id
        AND md2.movie_id = mg2.movie_id
        AND mg2.genre_id = mg3.genre_id
        AND mg3.movie_id = md3.movie_id
        AND md3.movie_id <> r.movie_id
        AND md3.director_id = d1.director_id;



#3. Βρείτε τα επώνυμα των ηθοποιών που, κατ αρχάς, παίζουν σε τουλάχιστον μια
#ταινία που έχει σκηνοθετηθεί από σκηνοθέτη με το ίδιο επώνυμο, και κατά
#δεύτερον, έχουν παίξει σε τουλάχιστον μια ταινία με σκηνοθέτη με διαφορετικό
#επώνυμο που έχει ίδιο είδος με αυτό άλλης ταινίας που δεν παίζουν αλλά έχει
#σκηνοθετήσει ο σκηνοθέτης με το ίδιο επώνυμο.