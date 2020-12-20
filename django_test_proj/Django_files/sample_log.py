# CharField has max_length of 255 characters while TextField can hold
# more than 255 characters. Use TextField when you have a large string as input.

# ImageField takes everything FileField takes in terms of attributes, but ImageField also takes a width
# and height attribute if indicated.
# ImageField, unlike FileField, validates an upload, making sure it's an image.

# STATIC_ROOT and STATIC_URL are for static files - files that are used by your web application and
# don't change by its users, i.e. static images(you site logo, backgrounds, etc). If you are using files, '
#    'that are uploaded by users, images or not, MEDIA_ROOT and MEDIA_URL are used. When you define upload_to'
#    ' it is concatenated with MEDIA_ROOT in your settings. So i.e.:
#
# MEDIA_ROOT='/var/www/media/'
#
# and you define:
#
# image = models.ImageField(upload_to = "shop/static/shop")
#
# the image will be stored as /var/www/media/shop/static/shop/[image_name.jpg].
#
# MEDIA_URL is the part in URL that will correspond to MEDIA_ROOT on filesystem path.














#############################################################################
# upload a file in rest_framework 1.
# models.py
from django.db import models
from probably.users.models import User


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, to_field='id')
    datafile = models.FileField()


# serializers.py
from rest_framework import serializers
from probably.obtain.models import FileUpload


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = FileUpload
        read_only_fields = ('created', 'datafile', 'owner')


# views.py
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from probably.obtain.models import FileUpload
from probably.obtain.serializers import FileUploadSerializer


class FileUploadViewSet(ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        datafile=self.request.data.get('datafile'))

# tests.py


class FileUploadTests(APITestCase):

    def setUp(self):
        self.tearDown()
        u = User.objects.create_user('test', password='test',
                                     email='test@test.test')
        u.save()

    def tearDown(self):
        try:
            u = User.objects.get_by_natural_key('test')
            u.delete()

        except ObjectDoesNotExist:
            pass
        FileUpload.objects.all().delete()

    def _create_test_file(self, path):
        f = open(path, 'w')
        f.write('test123\n')
        f.close()
        f = open(path, 'rb')
        return {'datafile': f}

    def test_upload_file(self):
        url = reverse('fileupload-list')
        data = self._create_test_file('/tmp/test_upload')

        # assert authenticated user can upload file
        token = Token.objects.get(user__username='test')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('created', response.data)
        self.assertTrue(urlparse(
            response.data['datafile']).path.startswith(settings.MEDIA_URL))
        self.assertEqual(response.data['owner'],
                       User.objects.get_by_natural_key('test').id)
        self.assertIn('created', response.data)

        # assert unauthenticated user can not upload file
        client.logout()
        response = client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#####################################################################
#### Write/save  data files to mysql
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='pynative',
                             password='pynative@#29')
        cursor = connection.cursor(prepared=True)
        sql_insert_blob_query = """ INSERT INTO `python_employee`
                          (`id`, `name`, `photo`, `biodata`) VALUES (%s,%s,%s,%s)"""
        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)
        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print ("Image and file inserted successfully as a BLOB into python_employee table", result)
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
insertBLOB(1, "Eric", "D:\Python\Articles\my_SQL\images\eric_photo.png", "D:\Python\Articles\my_SQL\images\eric_bioData.txt")
insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png","D:\Python\Articles\my_SQL\images\scott_bioData.txt")

# output
# Inserting BLOB into python_employee table
# Image and file inserted successfully as a BLOB into python_employee table None
# MySQL connection is closed
# Inserting BLOB into python_employee table

### Read BLOB data from mysql

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='pynative',
                             password='pynative@#29')
        cursor = connection.cursor(prepared=True)
        sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""
        cursor.execute(sql_fetch_blob_query, (emp_id, ))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image =  row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to read BLOB data from MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


readBLOB(1, "D:\Python\Articles\my_SQL\query_output\eric_photo.png", "D:\Python\Articles\my_SQL\query_output\eric_bioData.txt")
readBLOB(2, "D:\Python\Articles\my_SQL\query_output\scott_photo.png", "D:\Python\Articles\my_SQL\query_output\scott_bioData.txt")

###output
# Reading BLOB data from python_employee table
# Id = 1
# Name = Eric
# Storing employee image and bio-data on disk
# MySQL connection is closed
# Reading BLOB data from python_employee table
# Id = 2
# Name = Scott
# Storing employee image and bio-data on disk
# MySQL connection is closed

##
#upload a file in rest_framework 2.
# models.py
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    bio  = models.TextField(blank=True)

    pic  = models.ImageField(uploaded_to='pics', balnk=True)

    updated_at = models.DatTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# serializers.py


from rest_framework import serializers
from .models import Profile

# create new objects and retrieve data


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'pic']
        read_only_fields = ['pic']

# handle file


class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['pic']

### views.py

from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from .models import Profile
from .serializers import ProfilePicSerializer
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializers_class = ProfileSerializer
    queryset = Profile.object.all()

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializers_class=ProfileSerializer,
        parser_classes=[parsers.MultiPartParser],
    )
    def pic(self, request, pk):
        obj = self.get_object()
        serializers = self.serializers_class(obj, data=request.data, partial=True)

        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data)
        return response.Response(serializers.errors, status.HTTP_400_BAD_REQUEST)

## urls.py
from django.urls import path

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path(r'api/v1/', include(router.urls)),
]

# You can now create a profile with curl by making a POST request to /api/v1/profiles/:
#
# curl -d '{"name": "Douglas Hofstadter"}' \
#      -H "Content-Type: application/json" \
#      -X POST http://127.0.0.1:8000/api/v1/profiles/
# And attach an image by making a PUT request to /api/v1/profiles/1/pic/:
#
# curl -F "pic=@pic.png" \
#      -X PUT http://127.0.0.1:8000/api/v1/profiles/1/pic/

## file upload 1.
# models.py
from django.db import models


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# serializers.py


from rest_framework import serializers
from .models import MyFile


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFile
        fields = ('file', 'description', 'uploaded_at')

# views.py
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from  rest_framework   import status
from .serializers import MyFileSerializer

class MyFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#urls.py


from django.conf.urls import url
from .views import MyFileView

urlpatterns = [
    url(r'^upload/$',MyFileView.as_view(), name='file-upload'),
]

#
json_response={
    "file": "/media/dude_I2FPPum.jpg",
    "description": "Big Lebowski",
    "uploaded_at": "2019-04-26T12:30:09.463345Z"
}



























