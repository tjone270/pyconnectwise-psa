# ProductDemand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** |  | [optional] 
**product_rec_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_demand import ProductDemand

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDemand from a JSON string
product_demand_instance = ProductDemand.from_json(json)
# print the JSON string representation of the object
print ProductDemand.to_json()

# convert the object into a dict
product_demand_dict = product_demand_instance.to_dict()
# create an instance of ProductDemand from a dict
product_demand_form_dict = product_demand.from_dict(product_demand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


