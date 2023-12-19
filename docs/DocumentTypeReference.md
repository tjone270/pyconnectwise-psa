# DocumentTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.document_type_reference import DocumentTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTypeReference from a JSON string
document_type_reference_instance = DocumentTypeReference.from_json(json)
# print the JSON string representation of the object
print DocumentTypeReference.to_json()

# convert the object into a dict
document_type_reference_dict = document_type_reference_instance.to_dict()
# create an instance of DocumentTypeReference from a dict
document_type_reference_form_dict = document_type_reference.from_dict(document_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


