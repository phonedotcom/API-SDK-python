# swagger_client.PaymentmethodsApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_payment_method**](PaymentmethodsApi.md#create_account_payment_method) | **POST** /accounts/{account_id}/payment-methods | Create an individual payment method.
[**delete_account_payment_method**](PaymentmethodsApi.md#delete_account_payment_method) | **DELETE** /accounts/{account_id}/payment-methods/{pm_id} | Delete an individual payment method.
[**get_account_payment_method**](PaymentmethodsApi.md#get_account_payment_method) | **GET** /accounts/{account_id}/payment-methods/{pm_id} | Show details of an individual payment method.
[**list_account_payment_methods**](PaymentmethodsApi.md#list_account_payment_methods) | **GET** /accounts/{account_id}/payment-methods | Get a list of payment methods for an account.
[**patch_account_payment_method**](PaymentmethodsApi.md#patch_account_payment_method) | **PATCH** /accounts/{account_id}/payment-methods/{pm_id} | Replace the status of an individual payment method.


# **create_account_payment_method**
> PaymentFull create_account_payment_method(account_id, data)

Create an individual payment method.

Create an individual payment method. See Account Payment Methods for more info on the properties.

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
api_instance = swagger_client.PaymentmethodsApi()
account_id = 56 # int | Account ID
data = swagger_client.CreatePaymentParams() # CreatePaymentParams | Payment data

try: 
    # Create an individual payment method.
    api_response = api_instance.create_account_payment_method(account_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentmethodsApi->create_account_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **data** | [**CreatePaymentParams**](CreatePaymentParams.md)| Payment data | 

### Return type

[**PaymentFull**](PaymentFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_payment_method**
> DeleteEntry delete_account_payment_method(account_id, pm_id)

Delete an individual payment method.

Delete an individual payment method. See Account Payment Methods for more info on the properties.

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
api_instance = swagger_client.PaymentmethodsApi()
account_id = 56 # int | Account ID
pm_id = 56 # int | Payment Method ID

try: 
    # Delete an individual payment method.
    api_response = api_instance.delete_account_payment_method(account_id, pm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentmethodsApi->delete_account_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **pm_id** | **int**| Payment Method ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_payment_method**
> PaymentFull get_account_payment_method(account_id, pm_id)

Show details of an individual payment method.

Show details of an individual payment method. See Account Payment Methods for more info on the properties.

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
api_instance = swagger_client.PaymentmethodsApi()
account_id = 56 # int | Account ID
pm_id = 56 # int | Payment Method ID

try: 
    # Show details of an individual payment method.
    api_response = api_instance.get_account_payment_method(account_id, pm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentmethodsApi->get_account_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **pm_id** | **int**| Payment Method ID | 

### Return type

[**PaymentFull**](PaymentFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_payment_methods**
> ListPaymentMethods list_account_payment_methods(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)

Get a list of payment methods for an account.

Get a list of payment methods for an account. See Account Payment Methods for more info on the properties.

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
api_instance = swagger_client.PaymentmethodsApi()
account_id = 56 # int | Account ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of payment methods for an account.
    api_response = api_instance.list_account_payment_methods(account_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentmethodsApi->list_account_payment_methods: %s\n" % e)
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

[**ListPaymentMethods**](ListPaymentMethods.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_account_payment_method**
> PaymentFull patch_account_payment_method(account_id, pm_id, data=data)

Replace the status of an individual payment method.

Replace the status of an individual payment method. See Account Payment Methods for more info on the properties.

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
api_instance = swagger_client.PaymentmethodsApi()
account_id = 56 # int | Account ID
pm_id = 56 # int | Payment Method ID
data = swagger_client.PatchPaymentParams() # PatchPaymentParams | Payment data (optional)

try: 
    # Replace the status of an individual payment method.
    api_response = api_instance.patch_account_payment_method(account_id, pm_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentmethodsApi->patch_account_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **pm_id** | **int**| Payment Method ID | 
 **data** | [**PatchPaymentParams**](PatchPaymentParams.md)| Payment data | [optional] 

### Return type

[**PaymentFull**](PaymentFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

