# Code


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board_id** | **int** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**description** | **str** |  | 
**id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.code import Code

# TODO update the JSON string below
json = "{}"
# create an instance of Code from a JSON string
code_instance = Code.from_json(json)
# print the JSON string representation of the object
print Code.to_json()

# convert the object into a dict
code_dict = code_instance.to_dict()
# create an instance of Code from a dict
code_form_dict = code.from_dict(code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


