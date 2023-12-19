# ContactDepartment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.contact_department import ContactDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDepartment from a JSON string
contact_department_instance = ContactDepartment.from_json(json)
# print the JSON string representation of the object
print ContactDepartment.to_json()

# convert the object into a dict
contact_department_dict = contact_department_instance.to_dict()
# create an instance of ContactDepartment from a dict
contact_department_form_dict = contact_department.from_dict(contact_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


