# ProjectTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_type_reference import ProjectTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTypeReference from a JSON string
project_type_reference_instance = ProjectTypeReference.from_json(json)
# print the JSON string representation of the object
print ProjectTypeReference.to_json()

# convert the object into a dict
project_type_reference_dict = project_type_reference_instance.to_dict()
# create an instance of ProjectTypeReference from a dict
project_type_reference_form_dict = project_type_reference.from_dict(project_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


