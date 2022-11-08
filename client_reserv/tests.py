import django

django.setup()
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from client_reserv.models import Reservation
from client_reserv.serializers import ReservationSerializer
from django.test import TestCase
from django.urls import reverse

client = APIClient()


class GetAllReservationsTest(TestCase):
    """
    Get all reservations
    """

    def setUp(self):
        Reservation.objects.create(Name='Viny', Email='viny@gmail.com', TimeSlot='2022-11-25T12:00:00-09:30Z')
        Reservation.objects.create(Name='Ted', Email='ted@gmail.com', TimeSlot='2022-11-25T12:00:00-10:30Z')
        Reservation.objects.create(Name='John', Email='john@gmail.com', TimeSlot='2022-11-25T12:00:00-11:30Z')

    def test_get_all_reservations(self):
        # get API response
        response = client.get('client_reserv/reservation')
        # get data from db
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
