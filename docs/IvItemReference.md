# IvItemReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**serialized_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.iv_item_reference import IvItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of IvItemReference from a JSON string
iv_item_reference_instance = IvItemReference.from_json(json)
# print the JSON string representation of the object
print IvItemReference.to_json()

# convert the object into a dict
iv_item_reference_dict = iv_item_reference_instance.to_dict()
# create an instance of IvItemReference from a dict
iv_item_reference_form_dict = iv_item_reference.from_dict(iv_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


