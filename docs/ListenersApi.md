# swagger_client.ListenersApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_listener**](ListenersApi.md#create_account_listener) | **POST** /accounts/{account_id}/listeners | Add a listener object to your account that can be used to subscribe an event.
[**delete_account_listener**](ListenersApi.md#delete_account_listener) | **DELETE** /accounts/{account_id}/listeners/{listener_id} | Delete an individual event listener.
[**get_account_listener**](ListenersApi.md#get_account_listener) | **GET** /accounts/{account_id}/listeners/{listener_id} | Show details of an individual listener.
[**list_account_listeners**](ListenersApi.md#list_account_listeners) | **GET** /accounts/{account_id}/listeners | Get a list of listeners for an account.
[**replace_account_listener**](ListenersApi.md#replace_account_listener) | **PUT** /accounts/{account_id}/listeners/{listener_id} | Update the settings of an individual event listener.


# **create_account_listener**
> ListenerFull create_account_listener(account_id, data=data)

Add a listener object to your account that can be used to subscribe an event.

Add a listener object to your account that can be used to subscribe an event. See Account Listeners for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Post Listener API with the following definition: POST https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/listeners

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
api_instance = swagger_client.ListenersApi()
account_id = 56 # int | Account ID
data = swagger_client.CreateListenerParams() # CreateListenerParams | Account Listeners Data (optional)

try: 
    # Add a listener object to your account that can be used to subscribe an event.
    api_response = api_instance.create_account_listener(account_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenersApi->create_account_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **data** | [**CreateListenerParams**](CreateListenerParams.md)| Account Listeners Data | [optional] 

### Return type

[**ListenerFull**](ListenerFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_listener**
> DeleteEntry delete_account_listener(account_id, listener_id)

Delete an individual event listener.

Delete an individual event listener. See Account Listeners for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Delete Listener API with the following definition: DELETE https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/listeners/:listener_id

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
api_instance = swagger_client.ListenersApi()
account_id = 56 # int | Account ID
listener_id = 56 # int | Listener ID

try: 
    # Delete an individual event listener.
    api_response = api_instance.delete_account_listener(account_id, listener_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenersApi->delete_account_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **listener_id** | **int**| Listener ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_listener**
> ListenerFull get_account_listener(account_id, listener_id)

Show details of an individual listener.

Show details of an individual event listener. See Account Listeners for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Get Listener API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/listeners/:listener_id

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
api_instance = swagger_client.ListenersApi()
account_id = 56 # int | Account ID
listener_id = 56 # int | Listener ID

try: 
    # Show details of an individual listener.
    api_response = api_instance.get_account_listener(account_id, listener_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenersApi->get_account_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **listener_id** | **int**| Listener ID | 

### Return type

[**ListenerFull**](ListenerFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_listeners**
> ListListeners list_account_listeners(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)

Get a list of listeners for an account.

Get a list of listeners for an account. See Account Listeners for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level List Listeners API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/listeners

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
api_instance = swagger_client.ListenersApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of listeners for an account.
    api_response = api_instance.list_account_listeners(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenersApi->list_account_listeners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListListeners**](ListListeners.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_account_listener**
> ListenerFull replace_account_listener(account_id, listener_id, data=data)

Update the settings of an individual event listener.

Update the settings of an individual event listener. See Event Listeners for more detail. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Replace Listener API with the following definition: PUT https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/listeners/:listener_id

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
api_instance = swagger_client.ListenersApi()
account_id = 56 # int | Account ID
listener_id = 56 # int | Listener ID
data = swagger_client.CreateListenerParams() # CreateListenerParams | Account Listeners Data (optional)

try: 
    # Update the settings of an individual event listener.
    api_response = api_instance.replace_account_listener(account_id, listener_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListenersApi->replace_account_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **listener_id** | **int**| Listener ID | 
 **data** | [**CreateListenerParams**](CreateListenerParams.md)| Account Listeners Data | [optional] 

### Return type

[**ListenerFull**](ListenerFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

