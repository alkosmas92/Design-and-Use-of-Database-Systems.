SELECT DISTINCT
    d1.last_name, d2.last_name
FROM
    director d1,
    director d2,
    movie_has_director md1,
    movie_has_director md2,
    movie m,
    movie_has_genre mg
WHERE
    m.year < '2006' AND m.year > '2000'
        AND m.movie_id = md1.movie_id
        AND m.movie_id = md2.movie_id
        AND md1.director_id = d1.director_id
        AND md2.director_id = d2.director_id
        AND d1.director_id < d2.director_id
        AND m.movie_id = mg.movie_id
GROUP BY d1.last_name,d2.last_name
HAVING COUNT(mg.genre_id) > 5;


#5. Βρείτε τα επώνυμα των ζευγών σκηνοθετών που έχουν συνσκηνοθετήσει την ίδια
#ταινία μεταξύ του 2000 και του 2006, εφόσον οι δύο σκηνοθέτες σχετίζονται με
#τουλάχιστον έξι διαφορετικά είδη ταινιών. Βεβαιωθείτε ότι κάθε ζευγάρι
#τυπώνεται μία φορά (δηλαδή για παράδειγμα, μόνο ένα από τα (β1,β2) και
#(β2,β1)) και ότι κάθε σκηνοθέτης δεν συνδυάζεται με τον εαυτό του.