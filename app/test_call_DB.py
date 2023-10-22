import subprocess
import mysql.connector
from mysql.connector import pooling
import TotalVirusAPI
import re

def call_the_db(input_query):
    # Necessary evil
    mysql_command = f"mysql -h 34.66.176.31 -u root -pAnalisa4! -e '{input_query}'"


    print(" ")
    
    print(" ")
    
    print(" ")
    
    print(input_query)
    
    print(" ")
    
    print(" ")
    
    print(" ")

    # Use subprocess to run the MySQL command
    subprocess.call(mysql_command, shell=True)

    # Connection pool
    db_config = {
        "host": "34.66.176.31",
        "user": "root",
        "password": "Analisa4!",
        "database": "moneyscamatters-db"
    }
    pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

    # Connect to the connection pool
    conn = pool.get_connection()

    # Execute a query and fetch results
    cursor = conn.cursor()
    cursor.execute(input_query)
    results = cursor.fetchall()

    url_pattern = r'https?://\S+'

    def extract_links(input_string):

        website_url = re.findall(url_pattern, input_string)
        return website_url

    website = extract_links(input_query)

    if results:
        print("There has been a match in our database. DO NOT CLICK ON THE LINK!")
    else:
        print("Layer one passed. Moving on to layer two.")
        # TotalVirusAPI.call_the_VT(website)


    # Show results
    #for row in results:
    #    print(row)

    # Cleanup
    cursor.close()
    conn.close()

# Call the function to execute the database operations
#call_the_db()