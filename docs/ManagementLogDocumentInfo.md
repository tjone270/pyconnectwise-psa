# ManagementLogDocumentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size** | **str** |  | [optional] 
**full_path_file_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.management_log_document_info import ManagementLogDocumentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementLogDocumentInfo from a JSON string
management_log_document_info_instance = ManagementLogDocumentInfo.from_json(json)
# print the JSON string representation of the object
print ManagementLogDocumentInfo.to_json()

# convert the object into a dict
management_log_document_info_dict = management_log_document_info_instance.to_dict()
# create an instance of ManagementLogDocumentInfo from a dict
management_log_document_info_form_dict = management_log_document_info.from_dict(management_log_document_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


