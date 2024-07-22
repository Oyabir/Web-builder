import mysql.connector
import subprocess
import time

# Function to fetch websites to stop
def fetch_websites_to_stop():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",  # MySQL container hostname
        user="root",
        port=3307,
        password="password",
        database="websitesdb"
    )

    # Execute query to fetch websites with Statu_du_website = 0
    cursor = conn.cursor()
    query = "SELECT username, nameWebsite FROM Website_need_resiliation WHERE statut = 0"
    cursor.execute(query)

    # Parse query results and store information
    websites = []
    for username, nameWebsite in cursor:
        website_info = {
            "username": username,
            "nameWebsite": nameWebsite
        }
        websites.append(website_info)

    # Close cursor and connection
    cursor.close()
    conn.close()

    return websites

# Function to update Statu_du_website to 1 for a specific container
def update_website_status(username, nameWebsite):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",  # MySQL container hostname
        user="root",
        port=3307,
        password="password",
        database="websitesdb"
    )

    # Update Statu_du_website to 1
    cursor = conn.cursor()
    query = "UPDATE Website_need_resiliation SET statut = 1 WHERE username = %s AND nameWebsite = %s"
    cursor.execute(query, (username, nameWebsite))

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

# Function to stop Docker container
def stop_docker_container(nameWebsite):
    subprocess.run(["docker", "stop", nameWebsite])
    print(f"Docker container {nameWebsite} has been stopped.")

# Main function to stop websites
def stop_websites():
    # Fetch websites to stop
    websites = fetch_websites_to_stop()

    # Loop through each website
    for website in websites:
        username = website["username"]
        nameWebsite = website["nameWebsite"]

        # Stop Docker container
        stop_docker_container(nameWebsite)

        # Update website status
        update_website_status(username, nameWebsite)
        print(f"Website for user {username} with container {nameWebsite} has been stopped and status updated.")

# Run the script periodically
# while True:
#     stop_websites()
#     time.sleep(3600)  # Check every hour (3600 seconds)