from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize db without app context
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///planventure.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Base model for other database tables to inherit
    class BaseModel(db.Model):
        __abstract__ = True
        created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
        updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to PlanVenture API"})

    @app.route('/health')
    def health_check():
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat()
        })

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
