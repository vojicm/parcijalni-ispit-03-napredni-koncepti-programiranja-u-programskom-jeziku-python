from app_features.commons.menu import main_menu
from config.config import Config
from data.database_setup import setup_database_alchemy, setup_database_sqlite

def main():
    # Initialize configuration
    config = Config()

    # Set up the database based on configuration (you can switch to SQLite3 or SQLAlchemy setup if needed)
    setup_database_alchemy()
    # setup_database_sqlite()

    # Display the main menu and start the application
    main_menu(config)

if __name__ == "__main__":
    main()
