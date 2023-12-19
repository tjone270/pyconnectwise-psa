# ContactDepartmentReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_department_reference import ContactDepartmentReference

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDepartmentReference from a JSON string
contact_department_reference_instance = ContactDepartmentReference.from_json(json)
# print the JSON string representation of the object
print ContactDepartmentReference.to_json()

# convert the object into a dict
contact_department_reference_dict = contact_department_reference_instance.to_dict()
# create an instance of ContactDepartmentReference from a dict
contact_department_reference_form_dict = contact_department_reference.from_dict(contact_department_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


