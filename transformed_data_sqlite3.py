import sqlite3

# Connect to the database
with sqlite3.connect("flights.db") as conn:
    # Create a temporary table
    query = """
    SELECT team, SUM(points) AS points FROM (
        SELECT HomeTeam AS team, 
        CASE FTR
            WHEN 'H' THEN 3
            WHEN 'D' THEN 1
            ELSE 0
        END AS points
        FROM soccer
        UNION ALL
        SELECT AwayTeam AS team, 
        CASE FTR
            WHEN 'A' THEN 3
            WHEN 'D' THEN 1
            ELSE 0
        END AS points
        FROM soccer
    ) GROUP BY team ORDER BY points DESC
    """
    
    # Execute the query and fetch the results
    result = conn.execute(query).fetchall()

    # Display the results ordered by points per team
    print("Points per team (ordered):")
    for team, points in result:
        print(f"{team}: {points}")
