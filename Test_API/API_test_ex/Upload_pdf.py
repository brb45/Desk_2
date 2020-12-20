from base64 import b64encode
from json import dumps
import requests

ENCODING = 'utf-8'
FILE_NAME = 'en-ligne1.pdf'
JSON_NAME = 'output.json'

# first: reading the binary stuff
# note the 'rb' flag
# result: bytes
with open(FILE_NAME, 'rb') as open_file:
    byte_content = open_file.read()

# second: base64 encode read data
# result: bytes (again)
base64_bytes = b64encode(byte_content)

# third: decode these bytes to text
# result: string (in utf-8)
base64_string = base64_bytes.decode(ENCODING)

# optional: doing stuff with the data
# result here: some dict
raw_data = {
    "@type": "File",
    "title": "My file",
    "file": {
        "encoding": "base64",
        "data": base64_string,
        "filename": "test.pdf",
        "content-type": "application/pdf"
    }
}

# now: encoding the data to json
# result: string
json_data = dumps(raw_data, indent=2)

# finally: writing the json string to disk
# note the 'w' flag, no 'b' needed as we deal with text here
with open(JSON_NAME, 'w') as another_open_file:
    another_open_file.write(json_data)

# The script looks good. Use json_data as "body" of your HTTP-POST request
# (use "POST" rather than "GET" as "GET" requests typically have a size limitation).

requests.post('http://nohost/plone/folder',\
              headers={ 'Accept': 'application/json', 'Content-Type': 'application/json', }, \
              json=raw_data, auth=('admin', 'secret'))
"""
curl -H "X-PrettyPrint: 1" 
    -F 'json={ "body":{ 
    "messageSegments":[ { "type":"Text", "text":"Please accept this receipt." } ] }, 
    "capabilities":{ "content":{ "description":"Receipt for expenses", "title":"receipt.pdf" } }, 
    "feedElementType":"FeedItem", "subjectId":"005RR000000DmOb" };
    type=application/json' 
    
    
    -F "feedElementFileUpload=@receipt.pdf;type=application/octet-stream"
 -X POST https://instance_name/services/data/v35.0/chatter/feed-elements 
-H 'Authorization: OAuth 00DRR0000000N0g!...' --insecure
"""

"""
POST /services/data/v35.0/chatter/feed-elements HTTP/1.1
Authorization: OAuth 00DRR0000000N0g!...
User-Agent: Jakarta Commons-HttpClient/3.0.1
Host: instance_name
Content-Length: 845
Content-Type: multipart/form-data; boundary=a7V4kRcFA8E79pivMuV2tukQ85cmNKeoEgJgq
Accept: application/json

--a7V4kRcFA8E79pivMuV2tukQ85cmNKeoEgJgq
Content-Disposition: form-data; name="json"
Content-Type: application/json; charset=UTF-8

{
   "body":{
      "messageSegments":[
         {
            "type":"Text",
            "text":"Please accept this receipt."
         }
      ]
   },
   "capabilities":{
      "content":{
         "description":"Receipt for expenses",
         "title":"receipt.pdf"
      }
   },
   "feedElementType":"FeedItem",
   "subjectId":"005RR000000DmOb"
}

--a7V4kRcFA8E79pivMuV2tukQ85cmNKeoEgJgq
Content-Disposition: form-data; name="feedElementFileUpload"; filename="receipt.pdf"
Content-Type: application/octet-stream; charset=ISO-8859-1

...contents of receipt.pdf...

--a7V4kRcFA8E79pivMuV2tukQ85cmNKeoEgJgq--
"""