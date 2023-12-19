# Other1RevenueReference


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
from connectwise_psa.models.other1_revenue_reference import Other1RevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of Other1RevenueReference from a JSON string
other1_revenue_reference_instance = Other1RevenueReference.from_json(json)
# print the JSON string representation of the object
print Other1RevenueReference.to_json()

# convert the object into a dict
other1_revenue_reference_dict = other1_revenue_reference_instance.to_dict()
# create an instance of Other1RevenueReference from a dict
other1_revenue_reference_form_dict = other1_revenue_reference.from_dict(other1_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


