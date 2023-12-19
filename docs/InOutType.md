# InOutType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  Max length: 30; | 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.in_out_type import InOutType

# TODO update the JSON string below
json = "{}"
# create an instance of InOutType from a JSON string
in_out_type_instance = InOutType.from_json(json)
# print the JSON string representation of the object
print InOutType.to_json()

# convert the object into a dict
in_out_type_dict = in_out_type_instance.to_dict()
# create an instance of InOutType from a dict
in_out_type_form_dict = in_out_type.from_dict(in_out_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


