# ProjectContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_contact import ProjectContact

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectContact from a JSON string
project_contact_instance = ProjectContact.from_json(json)
# print the JSON string representation of the object
print ProjectContact.to_json()

# convert the object into a dict
project_contact_dict = project_contact_instance.to_dict()
# create an instance of ProjectContact from a dict
project_contact_form_dict = project_contact.from_dict(project_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


