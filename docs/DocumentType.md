# DocumentType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**file_extension** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**mime_type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.document_type import DocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentType from a JSON string
document_type_instance = DocumentType.from_json(json)
# print the JSON string representation of the object
print DocumentType.to_json()

# convert the object into a dict
document_type_dict = document_type_instance.to_dict()
# create an instance of DocumentType from a dict
document_type_form_dict = document_type.from_dict(document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


