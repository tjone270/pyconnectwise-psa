# DocumentSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**doc_path** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**is_public_flag** | **bool** |  | [optional] 
**template_output_path** | **str** |  Max length: 200; | [optional] 
**template_path** | **str** |  Max length: 200; | [optional] 
**upload_as_link_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.document_setup import DocumentSetup

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSetup from a JSON string
document_setup_instance = DocumentSetup.from_json(json)
# print the JSON string representation of the object
print DocumentSetup.to_json()

# convert the object into a dict
document_setup_dict = document_setup_instance.to_dict()
# create an instance of DocumentSetup from a dict
document_setup_form_dict = document_setup.from_dict(document_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


