# ConvertToProject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**record_type** | **str** |  | [optional] 
**wbs_code** | **str** |  | 

## Example

```python
from connectwise_psa.models.convert_to_project import ConvertToProject

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToProject from a JSON string
convert_to_project_instance = ConvertToProject.from_json(json)
# print the JSON string representation of the object
print ConvertToProject.to_json()

# convert the object into a dict
convert_to_project_dict = convert_to_project_instance.to_dict()
# create an instance of ConvertToProject from a dict
convert_to_project_form_dict = convert_to_project.from_dict(convert_to_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


