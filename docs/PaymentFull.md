# PaymentFull

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment Method ID | [optional] 
**voip_id** | **int** | API Account ID | [optional] 
**status** | **str** | &#39;primary&#39; &#x3D; primary card used for billing; &#39;onfile&#39; &#x3D; card on file; &#39;hidden&#39; &#x3D; deleted card; | [optional] 
**nickname** | **str** | Name of Card | [optional] 
**type** | **str** | &#39;cc&#39; for credit card | [optional] 
**created_at** | **int** | Time payment record is created | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) | Detail of contact person | [optional] 
**decline_count** | **int** | Number of times the payment method was declined | [optional] 
**next_charge_date** | **int** | Next billing date | [optional] 
**updated_at** | **int** | Last time the payment method was updated | [optional] 
**cc_token** | **str** | Encrypted credit card token to be used for billing | [optional] 
**cc_number** | **str** | Credit card number partially masked with xxxxxxxx | [optional] 
**cc_exp** | **str** | Credit card expiration date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


