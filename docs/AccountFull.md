# AccountFull

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Account ID. Sometimes referred to as \&quot;Voip ID\&quot; or \&quot;voip_id\&quot;. | [optional] 
**name** | **str** | Name on the account. Read-only. | [optional] 
**username** | **str** | Account user name | [optional] 
**password** | **str** | Account password. For security reason, this is masked as \&quot;**\&quot; | [optional] 
**master_account** | [**AccountSummary**](AccountSummary.md) | If this account is a subaccount, this property shows the master account that it belongs to. Otherwise it is NULL. Read-only. Output is an Account Summary Object. | [optional] 
**contact** | [**ContactAccount**](ContactAccount.md) | Contact Object. See below for details. | [optional] 
**billing_contact** | [**ContactAccount**](ContactAccount.md) | Contact Object for billing purposes. See below for details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


