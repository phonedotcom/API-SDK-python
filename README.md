# swagger_client
This is a Phone.com api Swagger definition

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account ID

try:
    # Retrieve details of an individual account
    api_response = api_instance.get_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.phone.com/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /accounts/{account_id} | Retrieve details of an individual account
*AccountsApi* | [**list_accounts**](docs/AccountsApi.md#list_accounts) | **GET** /accounts | Get a list of accounts visible to the authenticated user or client
*ApplicationsApi* | [**get_account_application**](docs/ApplicationsApi.md#get_account_application) | **GET** /accounts/{account_id}/applications/{application_id} | Show details of an individual application
*ApplicationsApi* | [**list_account_applications**](docs/ApplicationsApi.md#list_account_applications) | **GET** /accounts/{account_id}/applications | Get a list of applications you have defined
*AvailablenumbersApi* | [**list_available_phone_numbers**](docs/AvailablenumbersApi.md#list_available_phone_numbers) | **GET** /phone-numbers/available | 
*CalleridsApi* | [**get_caller_ids**](docs/CalleridsApi.md#get_caller_ids) | **GET** /accounts/{account_id}/extensions/{extension_id}/caller-ids | Show the Caller ID options a given extension can use
*CalllogsApi* | [**get_account_call_logs**](docs/CalllogsApi.md#get_account_call_logs) | **GET** /accounts/{account_id}/call-logs/{call_id} | Show details of an individual Call Log entry
*CalllogsApi* | [**list_account_call_logs**](docs/CalllogsApi.md#list_account_call_logs) | **GET** /accounts/{account_id}/call-logs | Get a list of call details associated with your account
*CallsApi* | [**create_account_call**](docs/CallsApi.md#create_account_call) | **POST** /accounts/{account_id}/calls | Make a phone call
*ContactsApi* | [**create_account_extension_contact**](docs/ContactsApi.md#create_account_extension_contact) | **POST** /accounts/{account_id}/extensions/{extension_id}/contacts | Add a new address book contact for an extension
*ContactsApi* | [**delete_account_extension_contact**](docs/ContactsApi.md#delete_account_extension_contact) | **DELETE** /accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id} | 
*ContactsApi* | [**get_account_extension_contact**](docs/ContactsApi.md#get_account_extension_contact) | **GET** /accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id} | Retrieve the details of an address book contact
*ContactsApi* | [**list_account_extension_contacts**](docs/ContactsApi.md#list_account_extension_contacts) | **GET** /accounts/{account_id}/extensions/{extension_id}/contacts | Show a list of address book contacts
*ContactsApi* | [**replace_account_extension_contact**](docs/ContactsApi.md#replace_account_extension_contact) | **PUT** /accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id} | 
*DefaultApi* | [**ping**](docs/DefaultApi.md#ping) | **GET** /ping | The default API command
*DevicesApi* | [**create_account_device**](docs/DevicesApi.md#create_account_device) | **POST** /accounts/{account_id}/devices | Register a generic VoIP device
*DevicesApi* | [**get_account_device**](docs/DevicesApi.md#get_account_device) | **GET** /accounts/{account_id}/devices/{device_id} | Show details of an individual VoIP device
*DevicesApi* | [**list_account_devices**](docs/DevicesApi.md#list_account_devices) | **GET** /accounts/{account_id}/devices | Get a list of VoIP devices associated with your account
*DevicesApi* | [**replace_account_device**](docs/DevicesApi.md#replace_account_device) | **PUT** /accounts/{account_id}/devices/{device_id} | Update the settings for an individual VoIP device
*ExpressservicecodesApi* | [**get_account_express_srv_code**](docs/ExpressservicecodesApi.md#get_account_express_srv_code) | **GET** /accounts/{account_id}/express-service-codes/{code_id} | Show details of an account Express Service Code
*ExpressservicecodesApi* | [**list_account_express_srv_codes**](docs/ExpressservicecodesApi.md#list_account_express_srv_codes) | **GET** /accounts/{account_id}/express-service-codes | Get the Express Service Code associated with your account in list format
*ExtensionsApi* | [**create_account_extension**](docs/ExtensionsApi.md#create_account_extension) | **POST** /accounts/{account_id}/extensions | Create an individual extension
*ExtensionsApi* | [**get_account_extension**](docs/ExtensionsApi.md#get_account_extension) | **GET** /accounts/{account_id}/extensions/{extension_id} | Show details of an individual extension
*ExtensionsApi* | [**list_account_extensions**](docs/ExtensionsApi.md#list_account_extensions) | **GET** /accounts/{account_id}/extensions | Get a list of extensions visible to the authenticated user or client
*ExtensionsApi* | [**replace_account_extension**](docs/ExtensionsApi.md#replace_account_extension) | **PUT** /accounts/{account_id}/extensions/{extension_id} | Replace an individual extension
*GroupsApi* | [**create_account_extension_contact_group**](docs/GroupsApi.md#create_account_extension_contact_group) | **POST** /accounts/{account_id}/extensions/{extension_id}/contact-groups | 
*GroupsApi* | [**delete_account_extension_contact_group**](docs/GroupsApi.md#delete_account_extension_contact_group) | **DELETE** /accounts/{account_id}/extensions/{extension_id}/contact-groups/{group_id} | Delete an addressbook group
*GroupsApi* | [**get_account_extension_contact_group**](docs/GroupsApi.md#get_account_extension_contact_group) | **GET** /accounts/{account_id}/extensions/{extension_id}/contact-groups/{group_id} | 
*GroupsApi* | [**list_account_extension_contact_groups**](docs/GroupsApi.md#list_account_extension_contact_groups) | **GET** /accounts/{account_id}/extensions/{extension_id}/contact-groups | Show a list of contact groups belonging to an extension
*GroupsApi* | [**replace_account_extension_contact_group**](docs/GroupsApi.md#replace_account_extension_contact_group) | **PUT** /accounts/{account_id}/extensions/{extension_id}/contact-groups/{group_id} | 
*MediaApi* | [**create_account_media_files**](docs/MediaApi.md#create_account_media_files) | **POST** /accounts/{account_id}/media/files | Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
*MediaApi* | [**create_account_media_tts**](docs/MediaApi.md#create_account_media_tts) | **POST** /accounts/{account_id}/media/tts | Add a media object to your account that can be used as a greeting or hold music. Users may create a media by using the built-in Text-to-speech (TTS) facility or upload a file of their choice. (Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB)
*MediaApi* | [**delete_account_media**](docs/MediaApi.md#delete_account_media) | **DELETE** /accounts/{account_id}/media/{media_id} | Delete an individual media record
*MediaApi* | [**get_account_media**](docs/MediaApi.md#get_account_media) | **GET** /accounts/{account_id}/media/{media_id} | Show details of an individual media recording (Greeting or Hold Music)
*MediaApi* | [**list_account_media**](docs/MediaApi.md#list_account_media) | **GET** /accounts/{account_id}/media | Get a list of media recordings for an account
*MediaApi* | [**replace_account_media_files**](docs/MediaApi.md#replace_account_media_files) | **PUT** /accounts/{account_id}/media/files/{media_id} | Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB.
*MediaApi* | [**replace_account_media_tts**](docs/MediaApi.md#replace_account_media_tts) | **PUT** /accounts/{account_id}/media/tts/{media_id} | Update a media object to your account. Note: The maximum size for media files or JSON objects included with a POST or PUT request is 10 MB.
*MenusApi* | [**create_account_menu**](docs/MenusApi.md#create_account_menu) | **POST** /accounts/{account_id}/menus | Create an individual menu
*MenusApi* | [**delete_account_menu**](docs/MenusApi.md#delete_account_menu) | **DELETE** /accounts/{account_id}/menus/{menu_id} | Delete an individual menu
*MenusApi* | [**get_account_menu**](docs/MenusApi.md#get_account_menu) | **GET** /accounts/{account_id}/menus/{menu_id} | Show details of an individual menu
*MenusApi* | [**list_account_menus**](docs/MenusApi.md#list_account_menus) | **GET** /accounts/{account_id}/menus | Get a list of menus for an account
*MenusApi* | [**replace_account_menu**](docs/MenusApi.md#replace_account_menu) | **PUT** /accounts/{account_id}/menus/{menu_id} | Replace an individual menu
*NumberregionsApi* | [**list_available_phone_number_regions**](docs/NumberregionsApi.md#list_available_phone_number_regions) | **GET** /phone-numbers/available/regions | 
*PhonenumbersApi* | [**create_account_phone_number**](docs/PhonenumbersApi.md#create_account_phone_number) | **POST** /accounts/{account_id}/phone-numbers | Add a phone number to an account
*PhonenumbersApi* | [**get_account_phone_number**](docs/PhonenumbersApi.md#get_account_phone_number) | **GET** /accounts/{account_id}/phone-numbers/{number_id} | Show details of an individual phone number
*PhonenumbersApi* | [**list_account_phone_numbers**](docs/PhonenumbersApi.md#list_account_phone_numbers) | **GET** /accounts/{account_id}/phone-numbers | Get a list of phone numbers registered to an account
*PhonenumbersApi* | [**replace_account_phone_number**](docs/PhonenumbersApi.md#replace_account_phone_number) | **PUT** /accounts/{account_id}/phone-numbers/{number_id} | Update the settings for an existing phone number on your account
*QueuesApi* | [**create_account_queue**](docs/QueuesApi.md#create_account_queue) | **POST** /accounts/{account_id}/queues | Create a queue
*QueuesApi* | [**delete_account_queue**](docs/QueuesApi.md#delete_account_queue) | **DELETE** /accounts/{account_id}/queues/{queue_id} | Delete a queue
*QueuesApi* | [**get_account_queue**](docs/QueuesApi.md#get_account_queue) | **GET** /accounts/{account_id}/queues/{queue_id} | Show details of an individual queue
*QueuesApi* | [**list_account_queues**](docs/QueuesApi.md#list_account_queues) | **GET** /accounts/{account_id}/queues | Get a list of queues for an account
*QueuesApi* | [**replace_account_queue**](docs/QueuesApi.md#replace_account_queue) | **PUT** /accounts/{account_id}/queues/{queue_id} | Replace a queue
*RoutesApi* | [**create_route**](docs/RoutesApi.md#create_route) | **POST** /accounts/{account_id}/routes | Add a new address book contact for an extension
*RoutesApi* | [**delete_account_route**](docs/RoutesApi.md#delete_account_route) | **DELETE** /accounts/{account_id}/routes/{route_id} | 
*RoutesApi* | [**get_account_route**](docs/RoutesApi.md#get_account_route) | **GET** /accounts/{account_id}/routes/{route_id} | Show details of an individual route
*RoutesApi* | [**list_account_routes**](docs/RoutesApi.md#list_account_routes) | **GET** /accounts/{account_id}/routes | Get a list of routes for an account
*RoutesApi* | [**replace_account_route**](docs/RoutesApi.md#replace_account_route) | **PUT** /accounts/{account_id}/routes/{route_id} | 
*SchedulesApi* | [**get_account_schedule**](docs/SchedulesApi.md#get_account_schedule) | **GET** /accounts/{account_id}/schedules/{schedule_id} | Show details of an individual schedule
*SchedulesApi* | [**list_account_schedules**](docs/SchedulesApi.md#list_account_schedules) | **GET** /accounts/{account_id}/schedules | Get a list of schedules for an account
*SmsApi* | [**create_account_sms**](docs/SmsApi.md#create_account_sms) | **POST** /accounts/{account_id}/sms | Send a SMS to one or a group of recipients
*SmsApi* | [**get_account_sms**](docs/SmsApi.md#get_account_sms) | **GET** /accounts/{account_id}/sms/{sms_id} | Show details of an individual SMS
*SmsApi* | [**list_account_sms**](docs/SmsApi.md#list_account_sms) | **GET** /accounts/{account_id}/sms | Get a list of SMS messages for an account
*SubaccountsApi* | [**create_account_subaccount**](docs/SubaccountsApi.md#create_account_subaccount) | **POST** /accounts/{account_id}/subaccounts | Add a subaccount for the authenticated user or client
*SubaccountsApi* | [**list_account_subaccounts**](docs/SubaccountsApi.md#list_account_subaccounts) | **GET** /accounts/{account_id}/subaccounts | Get a list of subaccounts for the authenticated user or client
*TrunksApi* | [**create_account_trunk**](docs/TrunksApi.md#create_account_trunk) | **POST** /accounts/{account_id}/trunks | Add a trunk record with SIP information
*TrunksApi* | [**delete_account_trunk**](docs/TrunksApi.md#delete_account_trunk) | **DELETE** /accounts/{account_id}/trunks/{trunk_id} | Delete a trunk from account
*TrunksApi* | [**get_account_trunk**](docs/TrunksApi.md#get_account_trunk) | **GET** /accounts/{account_id}/trunks/{trunk_id} | Show details of an individual trunk
*TrunksApi* | [**list_account_trunks**](docs/TrunksApi.md#list_account_trunks) | **GET** /accounts/{account_id}/trunks | Get a list of trunks for an account
*TrunksApi* | [**replace_account_trunk**](docs/TrunksApi.md#replace_account_trunk) | **PUT** /accounts/{account_id}/trunks/{trunk_id} | Replace parameters in a trunk


## Documentation For Models

 - [AccountFull](docs/AccountFull.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [Address](docs/Address.md)
 - [AddressListContacts](docs/AddressListContacts.md)
 - [ApplicationFull](docs/ApplicationFull.md)
 - [ApplicationSummary](docs/ApplicationSummary.md)
 - [AvailableNumbersFull](docs/AvailableNumbersFull.md)
 - [CallDetails](docs/CallDetails.md)
 - [CallFull](docs/CallFull.md)
 - [CallLogFull](docs/CallLogFull.md)
 - [CallNotifications](docs/CallNotifications.md)
 - [CallerIdFull](docs/CallerIdFull.md)
 - [CallerIdPhoneNumber](docs/CallerIdPhoneNumber.md)
 - [ContactAccount](docs/ContactAccount.md)
 - [ContactFull](docs/ContactFull.md)
 - [ContactSubaccount](docs/ContactSubaccount.md)
 - [ContactSummary](docs/ContactSummary.md)
 - [CreateCallParams](docs/CreateCallParams.md)
 - [CreateContactParams](docs/CreateContactParams.md)
 - [CreateDeviceParams](docs/CreateDeviceParams.md)
 - [CreateExtensionParams](docs/CreateExtensionParams.md)
 - [CreateGroupParams](docs/CreateGroupParams.md)
 - [CreateMediaParams](docs/CreateMediaParams.md)
 - [CreateMenuParams](docs/CreateMenuParams.md)
 - [CreatePhoneNumberParams](docs/CreatePhoneNumberParams.md)
 - [CreateQueueParams](docs/CreateQueueParams.md)
 - [CreateRouteParams](docs/CreateRouteParams.md)
 - [CreateSmsParams](docs/CreateSmsParams.md)
 - [CreateSubaccountParams](docs/CreateSubaccountParams.md)
 - [CreateTrunkParams](docs/CreateTrunkParams.md)
 - [DeleteContact](docs/DeleteContact.md)
 - [DeleteGroup](docs/DeleteGroup.md)
 - [DeleteMedia](docs/DeleteMedia.md)
 - [DeleteMenu](docs/DeleteMenu.md)
 - [DeleteQueue](docs/DeleteQueue.md)
 - [DeleteRoute](docs/DeleteRoute.md)
 - [DeleteTrunk](docs/DeleteTrunk.md)
 - [DeviceFull](docs/DeviceFull.md)
 - [DeviceMembership](docs/DeviceMembership.md)
 - [DeviceSummary](docs/DeviceSummary.md)
 - [Email](docs/Email.md)
 - [ExpressServiceCodeFull](docs/ExpressServiceCodeFull.md)
 - [ExtensionFull](docs/ExtensionFull.md)
 - [ExtensionSummary](docs/ExtensionSummary.md)
 - [FilterCallLogs](docs/FilterCallLogs.md)
 - [FilterIdArray](docs/FilterIdArray.md)
 - [FilterIdDirectionFrom](docs/FilterIdDirectionFrom.md)
 - [FilterIdExtensionNameArray](docs/FilterIdExtensionNameArray.md)
 - [FilterIdGroupIdUpdatedAtArray](docs/FilterIdGroupIdUpdatedAtArray.md)
 - [FilterIdNameArray](docs/FilterIdNameArray.md)
 - [FilterIdNamePhoneNumberArray](docs/FilterIdNamePhoneNumberArray.md)
 - [FilterListAvailableNumbers](docs/FilterListAvailableNumbers.md)
 - [FilterListPhoneNumbersRegions](docs/FilterListPhoneNumbersRegions.md)
 - [FilterNameNumberArray](docs/FilterNameNumberArray.md)
 - [Greeting](docs/Greeting.md)
 - [GroupFull](docs/GroupFull.md)
 - [GroupListContacts](docs/GroupListContacts.md)
 - [GroupSummary](docs/GroupSummary.md)
 - [HoldMusic](docs/HoldMusic.md)
 - [Line](docs/Line.md)
 - [ListAccounts](docs/ListAccounts.md)
 - [ListApplications](docs/ListApplications.md)
 - [ListAvailableNumbers](docs/ListAvailableNumbers.md)
 - [ListCallLogs](docs/ListCallLogs.md)
 - [ListCallerIds](docs/ListCallerIds.md)
 - [ListContacts](docs/ListContacts.md)
 - [ListDevices](docs/ListDevices.md)
 - [ListExpressServiceCodes](docs/ListExpressServiceCodes.md)
 - [ListExtensions](docs/ListExtensions.md)
 - [ListGroups](docs/ListGroups.md)
 - [ListMedia](docs/ListMedia.md)
 - [ListMenus](docs/ListMenus.md)
 - [ListPhoneNumbers](docs/ListPhoneNumbers.md)
 - [ListPhoneNumbersRegions](docs/ListPhoneNumbersRegions.md)
 - [ListQueues](docs/ListQueues.md)
 - [ListRoutes](docs/ListRoutes.md)
 - [ListSchedules](docs/ListSchedules.md)
 - [ListSms](docs/ListSms.md)
 - [ListTrunks](docs/ListTrunks.md)
 - [MediaFull](docs/MediaFull.md)
 - [MediaSummary](docs/MediaSummary.md)
 - [Member](docs/Member.md)
 - [MenuFull](docs/MenuFull.md)
 - [MenuSummary](docs/MenuSummary.md)
 - [Notification](docs/Notification.md)
 - [Option](docs/Option.md)
 - [PhoneNumberContact](docs/PhoneNumberContact.md)
 - [PhoneNumberFull](docs/PhoneNumberFull.md)
 - [PhoneNumbersRegionFull](docs/PhoneNumbersRegionFull.md)
 - [PingResponse](docs/PingResponse.md)
 - [QueueFull](docs/QueueFull.md)
 - [QueueSummary](docs/QueueSummary.md)
 - [Recipient](docs/Recipient.md)
 - [ReplaceExtensionParams](docs/ReplaceExtensionParams.md)
 - [ReplaceMenuParams](docs/ReplaceMenuParams.md)
 - [ReplacePhoneNumberParams](docs/ReplacePhoneNumberParams.md)
 - [RouteFull](docs/RouteFull.md)
 - [RouteSummary](docs/RouteSummary.md)
 - [RuleSet](docs/RuleSet.md)
 - [RuleSetAction](docs/RuleSetAction.md)
 - [RuleSetFilter](docs/RuleSetFilter.md)
 - [RuleSetForwardItem](docs/RuleSetForwardItem.md)
 - [ScheduleFull](docs/ScheduleFull.md)
 - [ScheduleSummary](docs/ScheduleSummary.md)
 - [SipAuthentication](docs/SipAuthentication.md)
 - [SmsForwarding](docs/SmsForwarding.md)
 - [SmsFull](docs/SmsFull.md)
 - [SortCallLogs](docs/SortCallLogs.md)
 - [SortId](docs/SortId.md)
 - [SortIdCreatedAt](docs/SortIdCreatedAt.md)
 - [SortIdExtensionName](docs/SortIdExtensionName.md)
 - [SortIdName](docs/SortIdName.md)
 - [SortIdNamePhoneNumber](docs/SortIdNamePhoneNumber.md)
 - [SortIdUpdatedAt](docs/SortIdUpdatedAt.md)
 - [SortListAvailableNumbers](docs/SortListAvailableNumbers.md)
 - [SortListPhoneNumbersRegions](docs/SortListPhoneNumbersRegions.md)
 - [SortNameNumber](docs/SortNameNumber.md)
 - [TrunkFull](docs/TrunkFull.md)
 - [TrunkSummary](docs/TrunkSummary.md)
 - [Voicemail](docs/Voicemail.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

apisupport@phone.com

