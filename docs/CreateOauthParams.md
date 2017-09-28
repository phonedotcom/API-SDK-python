# CreateOauthParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | authorization_code, client_credentials, password or refresh_token | [optional] 
**client_id** | **str** | Client ID | [optional] 
**client_secret** | **str** | Client Secret Key | [optional] 
**code** | **str** | Authorization Code created via the /oauth/authorization API | [optional] 
**redirect_uri** | **str** | The redirect URI where user enters authentication information | [optional] 
**scope** | **str** | account-owner, extension-user and/or methods:ALL, separated by space (%20) | [optional] 
**username** | **str** | User name | [optional] 
**password** | **str** | Password | [optional] 
**refresh_token** | **str** | Refresh token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


