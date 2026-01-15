import os
import pytest
from app import app, mongo
from bson.objectid import ObjectId

@pytest.fixture
def client():
    # Enable testing mode
    app.config["TESTING"] = True

    # Read Mongo URI from environment variable set in Jenkins credentials
    mongo_uri = os.environ.get("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI environment variable not set. Please configure Jenkins credentials or set locally.")

    app.config["MONGO_URI"] = mongo_uri

    # Initialize PyMongo
    mongo.init_app(app)

    # Create Flask test client
    client = app.test_client()

    # Setup: clear test DB and insert initial test student
    with app.app_context():
        mongo.db.students.delete_many({})
        mongo.db.students.insert_one({
            "_id": ObjectId("66fddff25f4b5f6a0a123456"),
            "name": "Test Student",
            "email": "test@student.com",
            "course": "Flask"
        })

    yield client  # Provide client to tests

    # Teardown: drop the test database after all tests
    with app.app_context():
        db_name = mongo.db.name
        mongo.cx.drop_database(db_name)


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test Student" in response.data


def test_add_student(client):
    data = {"name": "New User", "email": "new@user.com", "course": "Python"}
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"New User" in response.data


def test_update_student(client):
    student_id = "66fddff25f4b5f6a0a123456"
    data = {"name": "Updated Name", "email": "updated@student.com", "course": "Updated Course"}
    response = client.post(f'/update/{student_id}', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated Name" in response.data


def test_delete_student(client):
    with app.app_context():
        student_id = mongo.db.students.insert_one({
            "name": "Temp User",
            "email": "temp@user.com",
            "course": "Temp Course"
        }).inserted_id

    response = client.get(f'/delete/{student_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Temp User" not in response.data
