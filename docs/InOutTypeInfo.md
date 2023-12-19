# InOutTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.in_out_type_info import InOutTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InOutTypeInfo from a JSON string
in_out_type_info_instance = InOutTypeInfo.from_json(json)
# print the JSON string representation of the object
print InOutTypeInfo.to_json()

# convert the object into a dict
in_out_type_info_dict = in_out_type_info_instance.to_dict()
# create an instance of InOutTypeInfo from a dict
in_out_type_info_form_dict = in_out_type_info.from_dict(in_out_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


