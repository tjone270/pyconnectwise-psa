# ServiceTemplateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_template_info import ServiceTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemplateInfo from a JSON string
service_template_info_instance = ServiceTemplateInfo.from_json(json)
# print the JSON string representation of the object
print ServiceTemplateInfo.to_json()

# convert the object into a dict
service_template_info_dict = service_template_info_instance.to_dict()
# create an instance of ServiceTemplateInfo from a dict
service_template_info_form_dict = service_template_info.from_dict(service_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


