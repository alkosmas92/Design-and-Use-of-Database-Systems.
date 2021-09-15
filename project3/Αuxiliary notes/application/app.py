# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import pymysql as db
import settings
import sys

def connection():
    ''' User this function to create your connections '''
    con = db.connect(
        settings.mysql_host, 
        settings.mysql_user, 
        settings.mysql_passwd, 
        settings.mysql_schema)
    
    return con

def updateRank(rank1, rank2, movieTitle):

    # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()

    try:
        float(rank1)
    except ValueError:
        return [("status",),("error",),]
    try:
        float(rank2)
    except ValueError:
        return [("status",),("error",),]

    print (rank1, rank2, movieTitle)
    
    return [("status",),("ok",),]


def colleaguesOfColleagues(actorId1, actorId2):

    # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
    print (actorId1, actorId2)
    
    return [("movieTitle", "colleagueOfActor1", "colleagueOfActor2", "actor1","actor2",),]

def actorPairs(actorId):

    # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
	
	
    print (actorId)
    
    return [("actor2Id",),]
	
def selectTopNactors(n):

    # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
    print (n)
    
    return [("genreName", "actorId", "numberOfMovies"),]

