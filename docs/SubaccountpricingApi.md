# swagger_client.SubaccountpricingApi

All URIs are relative to *https://api.phone.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_subaccount_pricing**](SubaccountpricingApi.md#create_account_subaccount_pricing) | **POST** /accounts/{account_id}/subaccounts/{subaccount_id}/pricing | Add a pricing plan to a subaccount.
[**delete_account_subaccount_pricing**](SubaccountpricingApi.md#delete_account_subaccount_pricing) | **DELETE** /accounts/{account_id}/subaccounts/{subaccount_id}/pricing/{pricing_id} | Delete a pricing plan from a subaccount.
[**get_account_subaccount_pricing**](SubaccountpricingApi.md#get_account_subaccount_pricing) | **GET** /accounts/{account_id}/subaccounts/{subaccount_id}/pricing/{pricing_id} | Get the details of a pricing plan for a subaccount.
[**list_account_subaccount_pricing**](SubaccountpricingApi.md#list_account_subaccount_pricing) | **GET** /accounts/{account_id}/subaccounts/{subaccount_id}/pricing | Get a list of pricing plans for a subaccount.


# **create_account_subaccount_pricing**
> PricingFull create_account_subaccount_pricing(account_id, subaccount_id, data)

Add a pricing plan to a subaccount.

Add a pricing plan to a subaccount. See Account Subaccount Pricing for more info on the properties.

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
api_instance = swagger_client.SubaccountpricingApi()
account_id = 56 # int | Account ID
subaccount_id = 56 # int | Subaccount ID
data = swagger_client.CreatePricingParams() # CreatePricingParams | Subaccount pricing data

try: 
    # Add a pricing plan to a subaccount.
    api_response = api_instance.create_account_subaccount_pricing(account_id, subaccount_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountpricingApi->create_account_subaccount_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **subaccount_id** | **int**| Subaccount ID | 
 **data** | [**CreatePricingParams**](CreatePricingParams.md)| Subaccount pricing data | 

### Return type

[**PricingFull**](PricingFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_subaccount_pricing**
> DeleteEntry delete_account_subaccount_pricing(account_id, subaccount_id, pricing_id)

Delete a pricing plan from a subaccount.

Delete a pricing plan from a subaccount. See Account Subaccount Pricing for more info on the properties.

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
api_instance = swagger_client.SubaccountpricingApi()
account_id = 56 # int | Account ID
subaccount_id = 56 # int | Subaccount ID
pricing_id = 56 # int | Pricing Object ID

try: 
    # Delete a pricing plan from a subaccount.
    api_response = api_instance.delete_account_subaccount_pricing(account_id, subaccount_id, pricing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountpricingApi->delete_account_subaccount_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **subaccount_id** | **int**| Subaccount ID | 
 **pricing_id** | **int**| Pricing Object ID | 

### Return type

[**DeleteEntry**](DeleteEntry.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_subaccount_pricing**
> PricingFull get_account_subaccount_pricing(account_id, subaccount_id, pricing_id)

Get the details of a pricing plan for a subaccount.

Get the details of a pricing plan for a subaccount. See Account Subaccount Pricing for more info on the properties.

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
api_instance = swagger_client.SubaccountpricingApi()
account_id = 56 # int | Account ID
subaccount_id = 56 # int | Subaccount ID
pricing_id = 56 # int | Pricing Object ID

try: 
    # Get the details of a pricing plan for a subaccount.
    api_response = api_instance.get_account_subaccount_pricing(account_id, subaccount_id, pricing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountpricingApi->get_account_subaccount_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **subaccount_id** | **int**| Subaccount ID | 
 **pricing_id** | **int**| Pricing Object ID | 

### Return type

[**PricingFull**](PricingFull.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_subaccount_pricing**
> ListPricings list_account_subaccount_pricing(account_id, subaccount_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)

Get a list of pricing plans for a subaccount.

Get a list of pricing plans for a subaccount. See Account Subaccount Pricing for more info on the properties.

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
api_instance = swagger_client.SubaccountpricingApi()
account_id = 56 # int | Account ID
subaccount_id = 56 # int | Subaccount ID
filters_id = ['filters_id_example'] # list[str] | ID filter (optional)
sort_id = 'sort_id_example' # str | ID sorting (optional)
limit = 56 # int | Max results (optional)
offset = 56 # int | Results to skip (optional)
fields = 'fields_example' # str | Field set (optional)

try: 
    # Get a list of pricing plans for a subaccount.
    api_response = api_instance.list_account_subaccount_pricing(account_id, subaccount_id, filters_id=filters_id, sort_id=sort_id, limit=limit, offset=offset, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountpricingApi->list_account_subaccount_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account ID | 
 **subaccount_id** | **int**| Subaccount ID | 
 **filters_id** | [**list[str]**](str.md)| ID filter | [optional] 
 **sort_id** | **str**| ID sorting | [optional] 
 **limit** | **int**| Max results | [optional] 
 **offset** | **int**| Results to skip | [optional] 
 **fields** | **str**| Field set | [optional] 

### Return type

[**ListPricings**](ListPricings.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

