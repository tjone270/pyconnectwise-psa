# ProjectStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_status_reference import ProjectStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusReference from a JSON string
project_status_reference_instance = ProjectStatusReference.from_json(json)
# print the JSON string representation of the object
print ProjectStatusReference.to_json()

# convert the object into a dict
project_status_reference_dict = project_status_reference_instance.to_dict()
# create an instance of ProjectStatusReference from a dict
project_status_reference_form_dict = project_status_reference.from_dict(project_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


