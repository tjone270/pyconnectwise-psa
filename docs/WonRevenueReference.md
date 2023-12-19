# WonRevenueReference


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
from connectwise_psa.models.won_revenue_reference import WonRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of WonRevenueReference from a JSON string
won_revenue_reference_instance = WonRevenueReference.from_json(json)
# print the JSON string representation of the object
print WonRevenueReference.to_json()

# convert the object into a dict
won_revenue_reference_dict = won_revenue_reference_instance.to_dict()
# create an instance of WonRevenueReference from a dict
won_revenue_reference_form_dict = won_revenue_reference.from_dict(won_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


