# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import pymysql as db
import settings
import sys

#####################################
# Definitions of Database functions #
#####################################

# -- Database Connection -- #
def connection():
    ''' User this function to create your connections '''
    print(settings.mysql_host, settings.mysql_user, settings.mysql_passwd, settings.mysql_schema)
    con = db.connect(
        settings.mysql_host, 
        settings.mysql_user, 
        settings.mysql_passwd, 
        settings.mysql_schema)
    
    return con

# -- Open connection, execute query and fetch results -- #
def connectToDBandGetMovieInformation(movieTitle):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()

    '% counter of fetched result lines %'
    counter = 0
    '% store ranking %'
    rankValue = 0.0
    '% rank is null %'
    isRanked = True
    '% store movie id %'
    movieID = 0
    query = "SELECT * FROM movie WHERE title = %s "

    cursor.execute(query, (movieTitle))

    '% count the result lines and keep the ranking %'
    for (movie_id, title, year, rank) in cursor:
        rankValue = rank
        movieID = movie_id
        if rankValue is None:
            isRanked = False
        counter = counter + 1

    cursor.close()
    con.close()

    '% return dictionary with the results %'
    return {'moviesFound':counter, 'rankValue':rankValue ,'isRanked':isRanked, 'movie_id': movieID }

# - post changed rank -- #
def postRank(rank, movieID):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()
    '% MySql session has the safe-updates option set. Thus, we resolve the row by movie-id %'
    query = "UPDATE movie SET movie.rank=%s WHERE movie.movie_id=%s"
    cursor.execute(query, (rank, movieID))
    cursor.close()
    con.commit()
    con.close()

# - connect to database and check for movies and actor colleagues -- #
def searchMoviesOfActorColleagues(actorId1, actorId2):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()
    '% define the query %'
    query = ("select distinct m.title, r3.actor_id as ACTOR_C, r4.actor_id ACTOR_D "
             "from movie m, role r1, role r2, role r3, role r4 "
             "where r1.actor_id=%s "
             "and r2.actor_id=%s "
             "and r3.movie_id=r4.movie_id "
             "and m.movie_id=r4.movie_id "
             "and r1.actor_id<>r3.actor_id "
             "and r1.actor_id<>r4.actor_id "
             "and r3.actor_id<>r4.actor_id "
             "and r2.actor_id<>r3.actor_id "
             "and r2.actor_id<>r4.actor_id "
             "and r3.actor_id in "
             "      (select r3.actor_id "
             "      from role r1, role r3 "
             "      where r1.actor_id=%s and r1.movie_id=r3.movie_id) "
             "and r4.actor_id in "
             "      (select r4.actor_id "
             "      from role r2, role r4 "
             "      where r2.actor_id=%s "
             "      and r2.movie_id=r4.movie_id) "
             "order by m.title, r3.actor_id, r4.actor_id;")

    cursor.execute(query, (actorId1, actorId2, actorId1, actorId2))

    queryList = [("movieTitle", "colleagueOfActor1", "colleagueOfActor2", "actor1","actor2",),]
    '% add result to list %'
    for (title, ACTOR_C, ACTOR_D) in cursor:
        queryList.append((title, ACTOR_C, ACTOR_D, actorId1 ,actorId2))

    cursor.close()
    con.close()

    '% return list of row objects %'
    return queryList

# - connect to database and check for actors that comply with third exercise -- #
def searchActorPairs(actorId):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()
    '% define the query %'

    query = ("select r2.actor_id "
             "from role r1, role r2, movie_has_genre mg1, movie_has_genre mg2 "
             "where r1.actor_id=%s "
             "and r2.actor_id<>r1.actor_id "
             "and r2.movie_id=mg2.movie_id "
             "and r1.movie_id=mg1.movie_id "
             "and r2.actor_id not in "
             "  (select r2.actor_id "
             "  from role r1, role r2, movie_has_genre mg1, movie_has_genre mg2 "
             "  where r1.actor_id=%s "
             "  and r2.actor_id<>r1.actor_id "
             "  and r1.movie_id=mg1.movie_id "
             "  and r2.movie_id=mg2.movie_id "
             "  and mg1.genre_id=mg2.genre_id) "
             "group by r2.actor_id having count(distinct mg1.genre_id)+count(distinct mg2.genre_id)>6")

    cursor.execute(query, (actorId, actorId))

    queryList = [("actor2Id",),]
    '% add result to list %'
    for (actor_id) in cursor:
        queryList.append((actor_id))

    cursor.close()
    con.close()

    '% return list of row objects %'
    return queryList

def searchForTopNactorsOnGenre(n, genre):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()
    '% define the query %'
    query = ("select g.genre_name, r.actor_id, count(mg.movie_id) "
             "from role r, movie_has_genre mg, genre g "
             "where g.genre_id=%s "
             "and g.genre_id=mg.genre_id "
             "and mg.movie_id=r.movie_id "
             "group by g.genre_id, r.actor_id "
             "order by g.genre_name, count(mg.movie_id) desc "
             "limit %s")

    cursor.execute(query, (genre, n))

    queryList = []
    '% add result to list %'
    for (genreName, actor_id, numberOfMovies) in cursor:
        queryList.append((genreName, actor_id, numberOfMovies))

    cursor.close()
    con.close()

    '% return list of row objects %'
    return queryList

# -- search for n top actors in movies -- #
def searchForTopNactors(n):

    '% Initialize the connection %'
    con = connection()
    '% Create a cursor on the connection %'
    cursor = con.cursor()
    '% define the query %'
    query = ("select genre_id from genre order by genre_name")

    cursor.execute(query)

    queryList = [("genreName", "actorId", "numberOfMovies"),]
    '% add result to list %'
    for (genre_id) in cursor:
        subQuery = searchForTopNactorsOnGenre(int(n), int(genre_id[0]))
        for element in subQuery:
            queryList.append(element)

    cursor.close()
    con.close()

    '% return list of row objects %'
    return queryList

# -- Check that rank lies between [0-10] -- #
def checkRankBounds(rank):
    rankLiesBetweenLimits = False
    if (float(rank) >= 0.0) and (float(rank) <= 10.0):
        rankLiesBetweenLimits = True

    return rankLiesBetweenLimits

# - method to calculate average in all cases -- #
def calculateRank(rank1, rank2, existingRank, isRanked):
    rank = 0.0
    if (isRanked == True):
        rank = (rank1 + rank2 + existingRank) / 3
    else:
        rank = (rank1 + rank2) / 2
    return rank

#######################
# main ranking method #
#######################
def updateRank(rank1, rank2, movieTitle):

    '% first check if user arguements are valid float %'
    try:
        float(rank1)
    except ValueError:
        return [("status",),("error",),]
    try:
        float(rank2)
    except ValueError:
        return [("status",),("error",),]

    '% global variables to keep status of execution %'
    success = False
    message = ""

    try:
        '% create connection and run query and get result object %'
        queryResult = connectToDBandGetMovieInformation(movieTitle)

        '% If movies count > 0 then check if count is 1 (one) and that rank1&2 do not violate the bounds 0-10, in any other case is error %'
        if (int(queryResult['moviesFound']) > 0):
            if (int(queryResult['moviesFound']) == 1):
                if (checkRankBounds(float(rank1)) and checkRankBounds(float(rank2))):
                    '% check if it is null to set correct rankValue %'
                    rankValue = 0.0
                    if (bool(queryResult['isRanked']) == True):
                        rankValue = float(queryResult['rankValue'])
                    calculatedRank = calculateRank(float(rank1), float(rank2), rankValue, bool(queryResult['isRanked']))
                    postRank(float(calculatedRank), int(queryResult['movie_id']))
                    success = True
                    message = "No error"
                else:
                    success = False
                    message = "Boundary errors"
            else:
                success = False
                message = "Multiple movies exist with the same name"
        else:
            success = False
            message = "No movies found"
    except:
        success = False
        message = "Unknown error"

    if (success == True):
        return [("status",), ("ok",), ]
    else:
        return [("status",), ("error",), ]

#############################
# Find movies of actor1 & 2 #
#############################
def colleaguesOfColleagues(actorId1, actorId2):

    try:
        int(actorId1)
        int(actorId2)
        queryList = searchMoviesOfActorColleagues(int(actorId1), int(actorId2))
    except:
        return [("ERROR", "Check argument values!"),]
    length = len(queryList) - 1
    queryList.append(("FOUND", length, "rows", "", ""))
    return queryList

#############################
# Find actor pairs          #
#############################
def actorPairs(actorId):

    try:
        int(actorId)
        queryList = searchActorPairs(int(actorId))
    except:
        return [("ERROR", "Check argument value!"),]
    return queryList
    
    return [("actor2Id",),]

###############################
# Find top n actors in movies #
###############################
def selectTopNactors(n):
    try:
        int(n)
        queryList = searchForTopNactors(int(n))
    except:
        return [("ERROR", "Check argument value!"), ]
    return queryList



