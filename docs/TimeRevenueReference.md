# TimeRevenueReference


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
from connectwise_psa.models.time_revenue_reference import TimeRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRevenueReference from a JSON string
time_revenue_reference_instance = TimeRevenueReference.from_json(json)
# print the JSON string representation of the object
print TimeRevenueReference.to_json()

# convert the object into a dict
time_revenue_reference_dict = time_revenue_reference_instance.to_dict()
# create an instance of TimeRevenueReference from a dict
time_revenue_reference_form_dict = time_revenue_reference.from_dict(time_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


