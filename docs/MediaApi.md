# swagger_client.MediaApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_media_files**](MediaApi.md#create_account_media_files) | **POST** /accounts/{account_id}/media/files | Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
[**create_account_media_tts**](MediaApi.md#create_account_media_tts) | **POST** /accounts/{account_id}/media/tts | Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
[**delete_account_media**](MediaApi.md#delete_account_media) | **DELETE** /accounts/{account_id}/media/{media_id} | Delete an individual media record
[**get_account_media**](MediaApi.md#get_account_media) | **GET** /accounts/{account_id}/media/{media_id} | Show details of an individual media recording (Greeting or Hold Music)
[**list_account_media**](MediaApi.md#list_account_media) | **GET** /accounts/{account_id}/media | Get a list of media recordings for an account.
[**replace_account_media_files**](MediaApi.md#replace_account_media_files) | **PUT** /accounts/{account_id}/media/files/{media_id} | Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB.
[**replace_account_media_tts**](MediaApi.md#replace_account_media_tts) | **PUT** /accounts/{account_id}/media/tts/{media_id} | Update a media object to your account.


# **create_account_media_files**
> MediaFull create_account_media_files(account_id, json=json, file=file)

Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)

See Account Media for more info on the properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
json = 'json_example' # str | Media extra parameters (optional)
file = '/path/to/file.txt' # file | Media file (optional)

try: 
    # Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
    api_response = api_instance.create_account_media_files(account_id, json=json, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->create_account_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **json** | **str**| Media extra parameters | [optional] 
 **file** | **file**| Media file | [optional] 

### Return type

[**MediaFull**](MediaFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_media_tts**
> MediaFull create_account_media_tts(account_id, data=data)

Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)

See Account Media for more info on the properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
data = swagger_client.CreateMediaParams() # CreateMediaParams | Media data (optional)

try: 
    # Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
    api_response = api_instance.create_account_media_tts(account_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->create_account_media_tts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **data** | [**CreateMediaParams**](CreateMediaParams.md)| Media data | [optional] 

### Return type

[**MediaFull**](MediaFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_media**
> DeleteEntry delete_account_media(account_id, media_id)

Delete an individual media record

See Account Media for more info on the properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
media_id = 56 # int | Media ID

try: 
    # Delete an individual media record
    api_response = api_instance.delete_account_media(account_id, media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->delete_account_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **media_id** | **int**| Media ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_media**
> MediaFull get_account_media(account_id, media_id)

Show details of an individual media recording (Greeting or Hold Music)

Get individual media recording

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
media_id = 56 # int | Media ID

try: 
    # Show details of an individual media recording (Greeting or Hold Music)
    api_response = api_instance.get_account_media(account_id, media_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_account_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **media_id** | **int**| Media ID | 

### Return type

[**MediaFull**](MediaFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_media**
> ListMedia list_account_media(account_id, filters_id=filters_id, filters_name=filters_name, sort_id=sort_id, sort_name=sort_name, limit=limit, offset=offset, fields=fields)

Get a list of media recordings for an account.

Get a list of media recordings for an account. See Account Media for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level List Media API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/media

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
filters_name = ['filters_name_example'] # list[str] | Name filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
sort_name = 'sort_name_example' # str | Name sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of media recordings for an account.
    api_response = api_instance.list_account_media(account_id, filters_id=filters_id, filters_name=filters_name, sort_id=sort_id, sort_name=sort_name, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->list_account_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **filters_name** | [**list[str]**](str.md)| Name filter | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **sort_name** | **str**| Name sorting | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListMedia**](ListMedia.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_account_media_files**
> MediaFull replace_account_media_files(account_id, media_id, json=json, file=file)

Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB.

See Account Media for more info on the properties.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
media_id = 56 # int | Media ID
json = 'json_example' # str | Media extra parameters (optional)
file = '/path/to/file.txt' # file | Media file (optional)

try: 
    # Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB.
    api_response = api_instance.replace_account_media_files(account_id, media_id, json=json, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->replace_account_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **media_id** | **int**| Media ID | 
 **json** | **str**| Media extra parameters | [optional] 
 **file** | **file**| Media file | [optional] 

### Return type

[**MediaFull**](MediaFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_account_media_tts**
> MediaFull replace_account_media_tts(account_id, media_id, data=data)

Update a media object to your account.

Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB. See Account Media for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Replace Media API with the following definition: PUT https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/media/:media_id

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MediaApi()
account_id = 56 # int | Account ID
media_id = 56 # int | Media ID
data = swagger_client.CreateMediaParams() # CreateMediaParams | Media data (optional)

try: 
    # Update a media object to your account.
    api_response = api_instance.replace_account_media_tts(account_id, media_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->replace_account_media_tts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **media_id** | **int**| Media ID | 
 **data** | [**CreateMediaParams**](CreateMediaParams.md)| Media data | [optional] 

### Return type

[**MediaFull**](MediaFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

