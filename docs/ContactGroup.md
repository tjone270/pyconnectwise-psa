# ContactGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company_group_unsubscribed_email_message** | **str** |  | [optional] 
**company_unsubcribed_email_message** | **str** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**contact_group_unsubscribed_email_message** | **str** |  | [optional] 
**contact_unsubscribed_email_message** | **str** |  | [optional] 
**description** | **str** |  Max length: 50; | [optional] 
**group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_group import ContactGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ContactGroup from a JSON string
contact_group_instance = ContactGroup.from_json(json)
# print the JSON string representation of the object
print ContactGroup.to_json()

# convert the object into a dict
contact_group_dict = contact_group_instance.to_dict()
# create an instance of ContactGroup from a dict
contact_group_form_dict = contact_group.from_dict(contact_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


