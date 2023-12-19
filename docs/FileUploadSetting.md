# FileUploadSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**global_file_size_limit** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**restrict_file_types_flag** | **bool** |  | 

## Example

```python
from connectwise_psa.models.file_upload_setting import FileUploadSetting

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadSetting from a JSON string
file_upload_setting_instance = FileUploadSetting.from_json(json)
# print the JSON string representation of the object
print FileUploadSetting.to_json()

# convert the object into a dict
file_upload_setting_dict = file_upload_setting_instance.to_dict()
# create an instance of FileUploadSetting from a dict
file_upload_setting_form_dict = file_upload_setting.from_dict(file_upload_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


