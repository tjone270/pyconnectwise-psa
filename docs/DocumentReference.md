# DocumentReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.document_reference import DocumentReference

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentReference from a JSON string
document_reference_instance = DocumentReference.from_json(json)
# print the JSON string representation of the object
print DocumentReference.to_json()

# convert the object into a dict
document_reference_dict = document_reference_instance.to_dict()
# create an instance of DocumentReference from a dict
document_reference_form_dict = document_reference.from_dict(document_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


