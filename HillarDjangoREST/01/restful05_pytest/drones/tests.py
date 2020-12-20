# patch_response = self.client.patch(url, data, format='json')
# response = self.client.post(url, data, format='json')
# response = self.client.get(url, format='json')
from django.test import TestCase

# Create your tests here.
from django.utils.http import urlencode
# from django.core.urlresolvers import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DroneCategory
from . import views


from .models import Pilot
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class DroneCategoryTests(APITestCase):
    def post_drone_category(self, name):
        url = reverse(views.DroneCategoryList.name)
        print("DroneCategoryList.name url is {}\n".format(url))
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_drone_category(self):
        """
        Ensure we can create a new DroneCategory and then retrieve it
        """
        print("\n*************************************************")
        print(" \n1.__ test_post_and_get_drone_category __")
        print("\n*************************************************")
        new_drone_category_name = 'Hexacopter'
        response = self.post_drone_category(new_drone_category_name)
        print("post response is {}".format(response))
        # post response is < Response status_code = 201, "application/json" >
        print("\nPK is {0}\n".format(DroneCategory.objects.get().pk))
        print(f"object is {DroneCategory.objects.get()}\n")
        # object is Hexacopter

        print(f"response.data is {response.data}\n")
        # response.data is {'url': 'http://testserver/drone-categories/1',
                        #   'pk': 1, 'name': 'Hexacopter', 'drones': []}
        print(f"response.data['name'] is {response.data['name']}\n")
        assert response.status_code == status.HTTP_201_CREATED
        assert DroneCategory.objects.count() == 1
        assert DroneCategory.objects.get().name == new_drone_category_name


    def test_post_existing_drone_category_name(self):
        """
        Ensure we cannot create a DroneCategory with an existing name
        """
        print("\n*************************************************")
        print(" \n2.__ test_post_existing_drone_category_name __\n")
        print("*************************************************")
        url = reverse(views.DroneCategoryList.name)
        new_drone_category_name = 'Duplicated Copter'
        # data = {'name': new_drone_category_name}
        response1 = self.post_drone_category(new_drone_category_name)
        assert response1.status_code == status.HTTP_201_CREATED
        response2 = self.post_drone_category(new_drone_category_name)
        print(f"type(response2)  is {response2}")
        print("response2 is {}\n".format(response2))
        # type(response2) is < Response status_code = 400, "application/json" >
        # response2 is < Response status_code = 400, "application/json" >

        print(f"response2.status_code is {response2.status_code}") # 400
        # <class 'int'>
        print(f"type(response2.status_code) is {type(response2.status_code)}")

        print(f"status.HTTP_400_BAD_REQUEST is {status.HTTP_400_BAD_REQUEST}")
        # status.HTTP_400_BAD_REQUEST is 400

        print(f"type(response2.data) is {type(response2.data)}")
        # type(response2.data) is < class 'rest_framework.utils.serializer_helpers.ReturnDict' >
        print(f"response2.data is {response2.data}\n")
        assert response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_drone_category_by_name(self):
        """
        Ensure we can filter a drone category by name
        """
        print("\n*************************************************")
        print(" \n3._ test_filter_drone_category_by_name _")
        print("\n*************************************************")
        print(" \n\n")
        drone_category_name1 = 'Hexacopter'
        self.post_drone_category(drone_category_name1)
        drone_caregory_name2 = 'Octocopter'
        self.post_drone_category(drone_caregory_name2)

        filter_by_name = {'name': drone_category_name1}
        url = '{0}?{1}'.format(
            reverse(views.DroneCategoryList.name),
            urlencode(filter_by_name))
        print("\nurl is {}\n".format(url))

        # ***
        response = self.client.get(url, format='json')
        print("\nresponse is {}\n".format(response))
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive only one element in the response
        assert response.data['count'] == 1

        assert response.data['results'][0]['name'] == drone_category_name1
        print(f"Type of response.data: {type(response.data)}")
        # Type of response.data: < class 'collections.OrderedDict' >
        print("response.data: {}".format(response.data))

# response.data: 
# OrderedDict([('count', 1), ('next', None), ('previous', None), 
#('results',[OrderedDict([('url', 'http://testserver/drone-categories/1'), ('pk', 1), ('name', 'Hexacopter'), ('drones', [])])
# ])
# ])

    def test_get_drone_categories_collection(self):
        """
        Ensure we can retrieve the drone categories collection
        """
        print("\n*************************************************")
        print(" \n4. ______ test_get_drone_categories_collection _")
        print("\n*************************************************")
        new_drone_category_name = 'Super Copter'
        self.post_drone_category(new_drone_category_name)
        url = reverse(views.DroneCategoryList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        # Make sure we receive only one element in the response
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_drone_category_name

    def test_update_patch_drone_category(self):
        """
        Ensure we can update a single field for a drone category
        """
        print("\n*************************************************")
        print(" \n5.______ test_patch_drone_category ______\n")
        print("\n*************************************************")
        drone_category_name = 'Category Initial Name'
        response = self.post_drone_category(drone_category_name)
        url = reverse(
            views.DroneCategoryDetail.name,
            None,
            {response.data['pk']})
        print("url is {}\n".format(url))
        updated_drone_category_name = 'Updated Name'
        data = {'name': updated_drone_category_name}
        patch_response = self.client.patch(url, data, format='json')

        print("patch_response is {}\n".format(patch_response))
        print("type(patch_response) is {}\n".format(type(patch_response)))


# patch_response is < Response status_code = 200, "application/json" >
# type(patch_response) is < class 'rest_framework.response.Response' >
# patch_response.data is 
# {'url': 'http://testserver/drone-categories/1',
#     'pk': 1, 'name': 'Updated Name', 'drones': []}

        print("patch_response.data is {}\n".format(patch_response.data))
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_drone_category_name

    def test_get_drone_category(self):
        """
        Ensure we can get a single drone category by id
        """
        print(" \n______ test_get_drone_category ______\n")
        drone_category_name = 'Easy to retrieve'
        response = self.post_drone_category(drone_category_name)
        url = reverse(
            views.DroneCategoryDetail.name,
            None,
            {response.data['pk']})
        get_response = self.client.get(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == drone_category_name

#______________________________________________________________
# ************************************************************
class PilotTests(APITestCase):
    def post_pilot(self, name, gender, races_count):
        url = reverse(views.PilotList.name)
        print("url is {}\n".format(url))
        data = {
            'name': name,
            'gender': gender,
            'races_count': races_count,
        }
        response = self.client.post(url, data, format='json')
        return response

    def create_user_and_set_token_credentials(self):
        user = User.objects.create_user(
            'user01', 'user01@example.com', 'user01P4ssw0rD')
        token = Token.objects.create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {0}'.format(token.key))

    def test_post_and_get_pilot(self):
        """
        Ensure we can create a new Pilot and then retrieve it
        Ensure we cannot retrieve the persisted pilot without a token
        """
        print("\n*************************************************")
        print(" \n6.______ test_post_and_get_pilot ______\n")
        print("\n*************************************************")
        self.create_user_and_set_token_credentials()
        new_pilot_name = 'Gaston'
        new_pilot_gender = Pilot.MALE
        new_pilot_races_count = 5
        response = self.post_pilot(
            new_pilot_name,
            new_pilot_gender,
            new_pilot_races_count)
        print("\nPK {0}\n".format(Pilot.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Pilot.objects.count() == 1
        saved_pilot = Pilot.objects.get()
        assert saved_pilot.name == new_pilot_name
        assert saved_pilot.gender == new_pilot_gender
        assert saved_pilot.races_count == new_pilot_races_count
        url = reverse(
            views.PilotDetail.name,
            None,
            {saved_pilot.pk})
        authorized_get_response = self.client.get(url, format='json')
        assert authorized_get_response.status_code ==status.HTTP_200_OK

        assert authorized_get_response.data['name'] == new_pilot_name
        # Clean up credentials
        self.client.credentials()
        unauthorized_get_response = self.client.get(url, format='json')
        assert unauthorized_get_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_try_to_post_pilot_without_token(self):
        """
        Ensure we cannot create a pilot without a token
        """
        new_pilot_name = 'Unauthorized Pilot'
        new_pilot_gender = Pilot.MALE
        new_pilot_races_count = 5
        response = self.post_pilot(
            new_pilot_name,
            new_pilot_gender,
            new_pilot_races_count)
        print("response is {}\n".format(response))
        print("Pilot.objects.count() is {}\n".format(Pilot.objects.count()))
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Pilot.objects.count() == 0





