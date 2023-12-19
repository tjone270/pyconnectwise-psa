# AllowedFileType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**file_type** | **str** |  | 
**id** | **int** |  | [optional] 
**size_limit** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.allowed_file_type import AllowedFileType

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedFileType from a JSON string
allowed_file_type_instance = AllowedFileType.from_json(json)
# print the JSON string representation of the object
print AllowedFileType.to_json()

# convert the object into a dict
allowed_file_type_dict = allowed_file_type_instance.to_dict()
# create an instance of AllowedFileType from a dict
allowed_file_type_form_dict = allowed_file_type.from_dict(allowed_file_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


