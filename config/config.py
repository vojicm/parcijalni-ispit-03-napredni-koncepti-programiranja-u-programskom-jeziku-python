class Config:
    """
    Class for application configuration.
    Allows choosing between sqlite3 and SQLAlchemy for database operations
    and setting up external API URLs.
    """

    def __init__(self):
        # Choose database type: "sqlite3" or "sqlalchemy"
        self.database_type = "sqlite3"  # Change to "sqlalchemy" if needed

        # API configuration for fetching user data
        self.user_api_url = "https://jsonplaceholder.typicode.com/users"
