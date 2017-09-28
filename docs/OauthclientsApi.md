# swagger_client.OauthclientsApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_oauth_client**](OauthclientsApi.md#delete_account_oauth_client) | **DELETE** /accounts/{account_id}/oauth/clients/{client_id} | Delete an individual OAuth client.
[**get_account_oauth_client**](OauthclientsApi.md#get_account_oauth_client) | **GET** /accounts/{account_id}/oauth/clients/{client_id} | Show details of an individual OAuth client.
[**list_account_oauth_clients**](OauthclientsApi.md#list_account_oauth_clients) | **GET** /accounts/{account_id}/oauth/clients | Get a list of OAuth clients for an account.


# **delete_account_oauth_client**
> DeleteEntry delete_account_oauth_client(account_id, client_id)

Delete an individual OAuth client.

Delete an individual OAuth client. See Account OAuth Clients for more info on the properties.

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
api_instance = swagger_client.OauthclientsApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID

try: 
    # Delete an individual OAuth client.
    api_response = api_instance.delete_account_oauth_client(account_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->delete_account_oauth_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_oauth_client**
> OauthClientFull get_account_oauth_client(account_id, client_id)

Show details of an individual OAuth client.

Show details of an individual OAuth client. See Account OAuth Clients for more info on the properties.

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
api_instance = swagger_client.OauthclientsApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID

try: 
    # Show details of an individual OAuth client.
    api_response = api_instance.get_account_oauth_client(account_id, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->get_account_oauth_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 

### Return type

[**OauthClientFull**](OauthClientFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_oauth_clients**
> ListOauthClients list_account_oauth_clients(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)

Get a list of OAuth clients for an account.

Get a list of OAuth clients for an account. See Account OAuth Clients for more info on the properties.

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
api_instance = swagger_client.OauthclientsApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of OAuth clients for an account.
    api_response = api_instance.list_account_oauth_clients(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->list_account_oauth_clients: %s\n" % e)
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

[**ListOauthClients**](ListOauthClients.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

