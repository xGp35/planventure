from app import create_app, db
from models.user import User

def init_db():
    try:
        app = create_app()
        with app.app_context():
            db.create_all()
            print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating database tables: {e}")

if __name__ == "__main__":
    init_db()
