# OpenRevenueReference


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
from connectwise_psa.models.open_revenue_reference import OpenRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of OpenRevenueReference from a JSON string
open_revenue_reference_instance = OpenRevenueReference.from_json(json)
# print the JSON string representation of the object
print OpenRevenueReference.to_json()

# convert the object into a dict
open_revenue_reference_dict = open_revenue_reference_instance.to_dict()
# create an instance of OpenRevenueReference from a dict
open_revenue_reference_form_dict = open_revenue_reference.from_dict(open_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


