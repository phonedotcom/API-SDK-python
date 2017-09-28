# swagger_client.VoicemailApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_voicemail**](VoicemailApi.md#get_account_voicemail) | **GET** /accounts/{account_id}/voicemail/{voicemail_id} | This service shows the details of an individual voicemail.
[**list_account_voicemail**](VoicemailApi.md#list_account_voicemail) | **GET** /accounts/{account_id}/voicemail | Get a list of voicemail messages for an account.
[**patch_account_voicemail**](VoicemailApi.md#patch_account_voicemail) | **PATCH** /accounts/{account_id}/voicemail/{voicemail_id} | Update the is_new parameter in a voicemail record.


# **get_account_voicemail**
> VoicemailFull get_account_voicemail(account_id, voicemail_id)

This service shows the details of an individual voicemail.

This service shows the details of an individual voicemail. See Intro to Voicemail for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Get Voicemail API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/voicemail/:voicemail_id

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
api_instance = swagger_client.VoicemailApi()
account_id = 56 # int | Account ID
voicemail_id = 'voicemail_id_example' # str | Voicemail ID

try: 
    # This service shows the details of an individual voicemail.
    api_response = api_instance.get_account_voicemail(account_id, voicemail_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->get_account_voicemail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **voicemail_id** | **str**| Voicemail ID | 

### Return type

[**VoicemailFull**](VoicemailFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_voicemail**
> ListVoicemail list_account_voicemail(account_id, filters_id=filters_id, filters_from=filters_from, filters_to=filters_to, filters_is_new=filters_is_new, filters_created_at=filters_created_at, filters_extension=filters_extension, sort_id=sort_id, sort_created_at=sort_created_at, limit=limit, offset=offset, fields=fields)

Get a list of voicemail messages for an account.

Get a list of voicemail messages for an account. See Intro to Voicemail for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the List Voicemail API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/voicemail

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
api_instance = swagger_client.VoicemailApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
filters_from = 'filters_from_example' # str | Caller ID filter (optional)
filters_to = 'filters_to_example' # str | Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B (optional)
filters_is_new = true # bool |  (optional)
filters_created_at = 'filters_created_at_example' # str | Date string representing the UTC time that sms was created (optional)
filters_extension = ['filters_extension_example'] # list[str] | Extension filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
sort_created_at = 'sort_created_at_example' # str | Sort by the UTC time that voicemail was created (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of voicemail messages for an account.
    api_response = api_instance.list_account_voicemail(account_id, filters_id=filters_id, filters_from=filters_from, filters_to=filters_to, filters_is_new=filters_is_new, filters_created_at=filters_created_at, filters_extension=filters_extension, sort_id=sort_id, sort_created_at=sort_created_at, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->list_account_voicemail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **filters_from** | **str**| Caller ID filter | [optional] 
 **filters_to** | **str**| Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B | [optional] 
 **filters_is_new** | **bool**|  | [optional] 
 **filters_created_at** | **str**| Date string representing the UTC time that sms was created | [optional] 
 **filters_extension** | [**list[str]**](str.md)| Extension filter | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **sort_created_at** | **str**| Sort by the UTC time that voicemail was created | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListVoicemail**](ListVoicemail.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_account_voicemail**
> VoicemailFull patch_account_voicemail(account_id, voicemail_id, data=data)

Update the is_new parameter in a voicemail record.

Update the is_new parameter in a voicemail record. See Account Voicemail for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Patch Voicemail API with the following definition: PATCH https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/voicemail/:voicemail_id

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
api_instance = swagger_client.VoicemailApi()
account_id = 56 # int | Account ID
voicemail_id = 'voicemail_id_example' # str | Voicemail ID
data = swagger_client.PatchVoicemailParams() # PatchVoicemailParams | Payment data (optional)

try: 
    # Update the is_new parameter in a voicemail record.
    api_response = api_instance.patch_account_voicemail(account_id, voicemail_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoicemailApi->patch_account_voicemail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **voicemail_id** | **str**| Voicemail ID | 
 **data** | [**PatchVoicemailParams**](PatchVoicemailParams.md)| Payment data | [optional] 

### Return type

[**VoicemailFull**](VoicemailFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

