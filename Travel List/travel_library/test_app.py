import pytest
from travel_library import create_app


# Configure the test client and create a fixture for it
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# Test function: testing the index page
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


# Test function: testing the add page
def test_add_trip(client):
    response = client.get('/add')
    assert response.status_code == 200

    # Test the form submission
    data = {'attraction': 'Bay Bridge',
            'city': 'San Francisco',
            'country': 'USA'}
    response = client.post('/add', data=data, follow_redirects=True)
    assert response.status_code == 200


# Test function: testing the search function
def test_search(client):
    response = client.post("/search", data={"query": "Golden Gate Bridge"})
    assert response.status_code == 302
    assert "/trip/" in response.location

    response = client.post("/search", data={"query": "Non-existent Trip"})
    assert response.status_code == 302
    assert "/add" in response.location


# Test function: testing the trip page
def test_trip(client):
    _id = 'a26f988651ac44f98eedb8e5c85bd7ff'
    response = client.get(f'/trip/{_id}')
    assert response.status_code == 200


# Test function: testing the edit_trip page
def test_edit_trip(client):
    _id = 'a26f988651ac44f98eedb8e5c85bd7ff'
    response = client.get(f'/edit/{_id}')
    assert response.status_code == 200


# Test function: testing the delete_trip page
def test_delete_trip(client):
    _id = 'a26f988651ac44f98eedb8e5c85bd7ff'
    response = client.get(f'/delete/{_id}')
    assert response.status_code == 200


# Test function: testing the delete_comment page
def test_delete_comment(client):
    _id = 'a26f988651ac44f98eedb8e5c85bd7ff'
    comment_index = 0
    response = client.post(f'/trip/{_id}/delete_comment/{comment_index}')
    assert response.status_code == 302


# Test function: testing the rate_trip page
def test_rate_trip(client):
    _id = 'a26f988651ac44f98eedb8e5c85bd7ff'
    rating = 5
    response = client.get(f'/trips/{_id}/rate?rating={rating}')
    assert response.status_code == 302
