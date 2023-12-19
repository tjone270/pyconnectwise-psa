# ServiceRevenueReference


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
from connectwise_psa.models.service_revenue_reference import ServiceRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceRevenueReference from a JSON string
service_revenue_reference_instance = ServiceRevenueReference.from_json(json)
# print the JSON string representation of the object
print ServiceRevenueReference.to_json()

# convert the object into a dict
service_revenue_reference_dict = service_revenue_reference_instance.to_dict()
# create an instance of ServiceRevenueReference from a dict
service_revenue_reference_form_dict = service_revenue_reference.from_dict(service_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


