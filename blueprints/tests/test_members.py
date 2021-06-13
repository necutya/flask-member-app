import json
from datetime import datetime


def test_index(app, client):
    """
    Test get request
    """
    res = client.get('/')
    assert res.status_code == 200


def test_create_member(app, client):
    """
    Test creating a new member
    """
    res = client.post('/', data={'name': 'Artem', 'email': 'test@test.com'})
    assert res.status_code == 200
    expected = {
        'status': 'success',
        'message': 'Member has been added successfully.',
        'user_data': {
            'name': 'Artem',
            'email': 'test@test.com',
            'registration_date': datetime.now().strftime('%d-%m-%Y'),
            'index': 1,
        }}
    assert expected == json.loads(res.get_data(as_text=True))


def test_create_member_with_duplicated_email(app, client):
    """
        Test creating a new member with existing email
    """
    res = client.post('/', data={'name': 'Errorich', 'email': 'test@test.com'})
    assert res.status_code == 403
    expected = {
        'status': 'fail',
        'message': 'Please, check correctness of your data.',
        'errors': {
            'email': ['Member with this email has been already registered. Please, use another one.']
        }}
    assert expected == json.loads(res.get_data(as_text=True))


def test_create_member_validators(app, client):
    """
        Test creating a new member with invalid data
    """
    res = client.post('/', data={'name': 'ТакНельзя', 'email': 'Хз'})
    assert res.status_code == 403
    expected = {
        'status': 'fail',
        'message': 'Please, check correctness of your data.',
        'errors': {
            'name': ['Name can contain only English letters, dots and spaces.'],
            'email': ['Field must be between 4 and 35 characters long.', 'Invalid email address.']
        }
    }
    assert expected == json.loads(res.get_data(as_text=True))
