import sender_stand_requests
import data

def test_get_order_info_by_track():
    track = sender_stand_requests.create_order(data.order_body).json()['track']
    response = sender_stand_requests.get_order_info_by_track(track)
    assert response.status_code == 200