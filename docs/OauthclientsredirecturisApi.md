# swagger_client.OauthclientsredirecturisApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_oauth_clients_redirect_uri**](OauthclientsredirecturisApi.md#create_account_oauth_clients_redirect_uri) | **POST** /accounts/{account_id}/oauth/clients/{client_id}/redirect-uris | Create an OAuth Client Redirect URI record.
[**delete_account_oauth_clients_redirect_uri**](OauthclientsredirecturisApi.md#delete_account_oauth_clients_redirect_uri) | **DELETE** /accounts/{account_id}/oauth/clients/{client_id}/redirect-uris/{uri_id} | Delete an OAuth Client Redirect URI record.
[**get_account_oauth_clients_redirect_uri**](OauthclientsredirecturisApi.md#get_account_oauth_clients_redirect_uri) | **GET** /accounts/{account_id}/oauth/clients/{client_id}/redirect-uris/{uri_id} | Get details of an OAuth Client Redirect URI record.
[**list_account_oauth_clients_redirect_uris**](OauthclientsredirecturisApi.md#list_account_oauth_clients_redirect_uris) | **GET** /accounts/{account_id}/oauth/clients/{client_id}/redirect-uris | Get a list of OAuth Client Redirect URIs for an account.


# **create_account_oauth_clients_redirect_uri**
> OauthClientRedirectUriFull create_account_oauth_clients_redirect_uri(account_id, client_id, data=data)

Create an OAuth Client Redirect URI record.

Create an OAuth Client Redirect URI record.

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
api_instance = swagger_client.OauthclientsredirecturisApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID
data = swagger_client.CreateRedirectUriParams() # CreateRedirectUriParams | Redirect Uri data (optional)

try: 
    # Create an OAuth Client Redirect URI record.
    api_response = api_instance.create_account_oauth_clients_redirect_uri(account_id, client_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsredirecturisApi->create_account_oauth_clients_redirect_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 
 **data** | [**CreateRedirectUriParams**](CreateRedirectUriParams.md)| Redirect Uri data | [optional] 

### Return type

[**OauthClientRedirectUriFull**](OauthClientRedirectUriFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_oauth_clients_redirect_uri**
> DeleteEntry delete_account_oauth_clients_redirect_uri(account_id, client_id, uri_id)

Delete an OAuth Client Redirect URI record.

Delete an OAuth Client Redirect URI record.

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
api_instance = swagger_client.OauthclientsredirecturisApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID
uri_id = 56 # int | Redirect URI ID

try: 
    # Delete an OAuth Client Redirect URI record.
    api_response = api_instance.delete_account_oauth_clients_redirect_uri(account_id, client_id, uri_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsredirecturisApi->delete_account_oauth_clients_redirect_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 
 **uri_id** | **int**| Redirect URI ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_oauth_clients_redirect_uri**
> OauthClientRedirectUriFull get_account_oauth_clients_redirect_uri(account_id, client_id, uri_id)

Get details of an OAuth Client Redirect URI record.

Get details of an OAuth Client Redirect URI record.

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
api_instance = swagger_client.OauthclientsredirecturisApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID
uri_id = 56 # int | Redirect URI ID

try: 
    # Get details of an OAuth Client Redirect URI record.
    api_response = api_instance.get_account_oauth_clients_redirect_uri(account_id, client_id, uri_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsredirecturisApi->get_account_oauth_clients_redirect_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 
 **uri_id** | **int**| Redirect URI ID | 

### Return type

[**OauthClientRedirectUriFull**](OauthClientRedirectUriFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_oauth_clients_redirect_uris**
> ListOauthClientsRedirectUris list_account_oauth_clients_redirect_uris(account_id, client_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)

Get a list of OAuth Client Redirect URIs for an account.

Get a list of OAuth Client Redirect URIs for an account.

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
api_instance = swagger_client.OauthclientsredirecturisApi()
account_id = 56 # int | Account ID
client_id = 56 # int | Client ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of OAuth Client Redirect URIs for an account.
    api_response = api_instance.list_account_oauth_clients_redirect_uris(account_id, client_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsredirecturisApi->list_account_oauth_clients_redirect_uris: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **client_id** | **int**| Client ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListOauthClientsRedirectUris**](ListOauthClientsRedirectUris.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

