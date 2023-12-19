# InOutTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.in_out_type_reference import InOutTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of InOutTypeReference from a JSON string
in_out_type_reference_instance = InOutTypeReference.from_json(json)
# print the JSON string representation of the object
print InOutTypeReference.to_json()

# convert the object into a dict
in_out_type_reference_dict = in_out_type_reference_instance.to_dict()
# create an instance of InOutTypeReference from a dict
in_out_type_reference_form_dict = in_out_type_reference.from_dict(in_out_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


