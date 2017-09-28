# swagger_client.SmsApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_sms**](SmsApi.md#create_account_sms) | **POST** /accounts/{account_id}/sms | Send a SMS to one or a group of recipients.
[**get_account_sms**](SmsApi.md#get_account_sms) | **GET** /accounts/{account_id}/sms/{sms_id} | This service shows the details of an individual SMS.
[**list_account_sms**](SmsApi.md#list_account_sms) | **GET** /accounts/{account_id}/sms | Get a list of SMS messages for an account.
[**patch_account_sms**](SmsApi.md#patch_account_sms) | **PATCH** /accounts/{account_id}/sms/{sms_id} | Update the is_new parameter in a sms record.


# **create_account_sms**
> SmsFull create_account_sms(account_id, data)

Send a SMS to one or a group of recipients.

Send a SMS to one or a group of recipients. For details on the input fields, see Intro to SMS. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Create SMS API with the following definition: POST https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms

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
api_instance = swagger_client.SmsApi()
account_id = 56 # int | Account ID
data = swagger_client.CreateSmsParams() # CreateSmsParams | SMS data

try: 
    # Send a SMS to one or a group of recipients.
    api_response = api_instance.create_account_sms(account_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsApi->create_account_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **data** | [**CreateSmsParams**](CreateSmsParams.md)| SMS data | 

### Return type

[**SmsFull**](SmsFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_sms**
> SmsFull get_account_sms(account_id, sms_id)

This service shows the details of an individual SMS.

This service shows the details of an individual SMS. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Get SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id

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
api_instance = swagger_client.SmsApi()
account_id = 56 # int | Account ID
sms_id = 'sms_id_example' # str | SMS ID

try: 
    # This service shows the details of an individual SMS.
    api_response = api_instance.get_account_sms(account_id, sms_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsApi->get_account_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **sms_id** | **str**| SMS ID | 

### Return type

[**SmsFull**](SmsFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_sms**
> ListSms list_account_sms(account_id, filters_id=filters_id, filters_from=filters_from, filters_to=filters_to, filters_direction=filters_direction, filters_extension=filters_extension, filters_created_at=filters_created_at, sort_id=sort_id, sort_created_at=sort_created_at, limit=limit, offset=offset, fields=fields)

Get a list of SMS messages for an account.

Get a list of SMS messages for an account. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level List SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms

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
api_instance = swagger_client.SmsApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
filters_from = 'filters_from_example' # str | Caller ID filter (optional)
filters_to = 'filters_to_example' # str | Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B (optional)
filters_direction = 'filters_direction_example' # str | Direction filter (optional)
filters_extension = ['filters_extension_example'] # list[str] | Extension filter (optional)
filters_created_at = 'filters_created_at_example' # str | Date string representing the UTC time that sms was created (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
sort_created_at = 'sort_created_at_example' # str | Sort by created time of message (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of SMS messages for an account.
    api_response = api_instance.list_account_sms(account_id, filters_id=filters_id, filters_from=filters_from, filters_to=filters_to, filters_direction=filters_direction, filters_extension=filters_extension, filters_created_at=filters_created_at, sort_id=sort_id, sort_created_at=sort_created_at, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsApi->list_account_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **filters_from** | **str**| Caller ID filter | [optional] 
 **filters_to** | **str**| Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B | [optional] 
 **filters_direction** | **str**| Direction filter | [optional] 
 **filters_extension** | [**list[str]**](str.md)| Extension filter | [optional] 
 **filters_created_at** | **str**| Date string representing the UTC time that sms was created | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **sort_created_at** | **str**| Sort by created time of message | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListSms**](ListSms.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_account_sms**
> SmsFull patch_account_sms(account_id, sms_id, data=data)

Update the is_new parameter in a sms record.

Update the is_new parameter in a sms record. See Account SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Patch SMS API with the following definition: PATCH https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id

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
api_instance = swagger_client.SmsApi()
account_id = 56 # int | Account ID
sms_id = 'sms_id_example' # str | SMS ID
data = swagger_client.PatchSmsParams() # PatchSmsParams | Sms data (optional)

try: 
    # Update the is_new parameter in a sms record.
    api_response = api_instance.patch_account_sms(account_id, sms_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmsApi->patch_account_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **sms_id** | **str**| SMS ID | 
 **data** | [**PatchSmsParams**](PatchSmsParams.md)| Sms data | [optional] 

### Return type

[**SmsFull**](SmsFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

