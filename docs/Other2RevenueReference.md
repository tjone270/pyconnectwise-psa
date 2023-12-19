# Other2RevenueReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cost** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**margin** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.other2_revenue_reference import Other2RevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of Other2RevenueReference from a JSON string
other2_revenue_reference_instance = Other2RevenueReference.from_json(json)
# print the JSON string representation of the object
print Other2RevenueReference.to_json()

# convert the object into a dict
other2_revenue_reference_dict = other2_revenue_reference_instance.to_dict()
# create an instance of Other2RevenueReference from a dict
other2_revenue_reference_form_dict = other2_revenue_reference.from_dict(other2_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


