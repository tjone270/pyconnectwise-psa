# ContactDepartmentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_department_info import ContactDepartmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDepartmentInfo from a JSON string
contact_department_info_instance = ContactDepartmentInfo.from_json(json)
# print the JSON string representation of the object
print ContactDepartmentInfo.to_json()

# convert the object into a dict
contact_department_info_dict = contact_department_info_instance.to_dict()
# create an instance of ContactDepartmentInfo from a dict
contact_department_info_form_dict = contact_department_info.from_dict(contact_department_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


