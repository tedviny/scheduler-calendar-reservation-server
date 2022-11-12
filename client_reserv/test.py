import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from client_reserv.models import Reservation


client = Client()


class TestGetAllReservations(TestCase):
    """
    Test module to get all reservations created
    """
    def setUp(self):
        Reservation.objects.create(
            Name='Alice', Email='alice@gmail.com', TimeSlot='2015-03-25T12:00:00-06:30Z'
        )
        Reservation.objects.create(
            Name='Bob', Email='bob@gmail.com', TimeSlot='2015-03-26T12:00:00-06:30Z'
        )
        Reservation.objects.create(
            Name='John', Email='john@gmail.com', TimeSlot='2015-03-27T12:00:00-06:30Z'
        )

    def test_get_all_reservations(self):
        # get API response
        response = client.get(reverse('reservation'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewReservationTest(TestCase):
    """
    Test Module to add new reservations
    """
    def setUp(self) -> None:
        # add correct user
        self.valid_payload = {
            "Name": "Alice",
            "Email": "alice@gmail.com",
            "TimeSlot": "2015-03-26T12:00:00-06:30Z"
        }
        # add incorrect user
        self.invalid_payload = {
            "Name": "Bob",
            "Email": "alice@gmail.com",
            "TimeSlot": ""
        }

    def test_create_valid_reservation(self):
        response = client.post(reverse('reservation'), data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_invalid_reservation(self):
        response = client.post(reverse('reservation'), data=json.dumps(self.invalid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
