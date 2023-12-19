# Office365EmailSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**authorized_flag** | **bool** |  | [optional] 
**client_id** | **str** |  Max length: 36; | [optional] 
**client_secret** | **str** |  Max length: 4000; | [optional] 
**email_connector** | [**EmailConnectorReference**](EmailConnectorReference.md) |  | [optional] 
**failed_folder** | **str** |  Max length: 40; | 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**inbox_folder** | **str** |  Max length: 40; | 
**name** | **str** |  Max length: 200; | 
**processed_folder** | **str** |  Max length: 40; | 
**source** | **int** |  | [optional] 
**tenant_id** | **str** |  Max length: 36; | [optional] 
**username** | **str** |  Max length: 100; | [optional] 

## Example

```python
from connectwise_psa.models.office365_email_setup import Office365EmailSetup

# TODO update the JSON string below
json = "{}"
# create an instance of Office365EmailSetup from a JSON string
office365_email_setup_instance = Office365EmailSetup.from_json(json)
# print the JSON string representation of the object
print Office365EmailSetup.to_json()

# convert the object into a dict
office365_email_setup_dict = office365_email_setup_instance.to_dict()
# create an instance of Office365EmailSetup from a dict
office365_email_setup_form_dict = office365_email_setup.from_dict(office365_email_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


