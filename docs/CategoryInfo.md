# CategoryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.category_info import CategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryInfo from a JSON string
category_info_instance = CategoryInfo.from_json(json)
# print the JSON string representation of the object
print CategoryInfo.to_json()

# convert the object into a dict
category_info_dict = category_info_instance.to_dict()
# create an instance of CategoryInfo from a dict
category_info_form_dict = category_info.from_dict(category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


