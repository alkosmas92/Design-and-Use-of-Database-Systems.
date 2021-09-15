SELECT DISTINCT
    m.year, g.genre_name
FROM
    movie m,
    genre g
WHERE
    EXISTS( SELECT 
            *
        FROM
            movie_has_genre mg
        WHERE
            m.movie_id = mg.movie_id
                AND mg.genre_id = g.genre_id
                AND m.year = '1995'
                AND g.genre_name = 'Drama');


#4. Ελέγξτε αν υπάρχει ταινία είδους “Drama” που έχει γυριστεί το 1995. (Το
#ερώτημα θα πρέπει να επιστρέφει ως απάντηση μια σχέση με μια πλειάδα και μια
#στήλη με τιμή “yes” ή “no”.). Απαγορεύεται η χρήση Flow Control Operators
#(δηλαδή if, case, κλπ).