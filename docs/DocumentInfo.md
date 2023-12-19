# DocumentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**created_on_date** | **str** |  | [optional] 
**document_type** | [**DocumentTypeReference**](DocumentTypeReference.md) |  | [optional] 
**file_name** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**html_template_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**image_flag** | **bool** |  | [optional] 
**link_flag** | **bool** |  | [optional] 
**owner** | **str** |  | [optional] 
**public_flag** | **bool** |  | [optional] 
**read_only_flag** | **bool** |  | [optional] 
**server_file_name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**url_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.document_info import DocumentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInfo from a JSON string
document_info_instance = DocumentInfo.from_json(json)
# print the JSON string representation of the object
print DocumentInfo.to_json()

# convert the object into a dict
document_info_dict = document_info_instance.to_dict()
# create an instance of DocumentInfo from a dict
document_info_form_dict = document_info.from_dict(document_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


