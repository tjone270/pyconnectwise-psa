# PortalConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_type_ids** | **List[int]** |  | [optional] 
**board_ids** | **List[int]** |  | [optional] 
**button_color** | **str** |  Max length: 7; | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**config_type_ids** | **List[int]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**display_vendor_flag** | **bool** |  | [optional] 
**header_color** | **str** |  Max length: 7; | [optional] 
**id** | **int** | Gets or sets and Sets             An existing Portal Configuration id is required when copying a Portal Configuration. | [optional] 
**language** | **str** |  | [optional] 
**location_ids** | **List[int]** |  | [optional] 
**login_background_color** | **str** |  Max length: 7; | [optional] 
**menu_color** | **str** |  Max length: 7; | [optional] 
**name** | **str** |  Max length: 150; | 
**portal_background_color** | **str** |  Max length: 7; | [optional] 
**portal_image_copy_success_flag** | **bool** |  | [optional] 
**url** | **str** |  Max length: 1000; | [optional] 
**welcome_text** | **str** |  Max length: 4000; | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration import PortalConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfiguration from a JSON string
portal_configuration_instance = PortalConfiguration.from_json(json)
# print the JSON string representation of the object
print PortalConfiguration.to_json()

# convert the object into a dict
portal_configuration_dict = portal_configuration_instance.to_dict()
# create an instance of PortalConfiguration from a dict
portal_configuration_form_dict = portal_configuration.from_dict(portal_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


