# SalesProbability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**probability** | **int** |  | 

## Example

```python
from connectwise_psa.models.sales_probability import SalesProbability

# TODO update the JSON string below
json = "{}"
# create an instance of SalesProbability from a JSON string
sales_probability_instance = SalesProbability.from_json(json)
# print the JSON string representation of the object
print SalesProbability.to_json()

# convert the object into a dict
sales_probability_dict = sales_probability_instance.to_dict()
# create an instance of SalesProbability from a dict
sales_probability_form_dict = sales_probability.from_dict(sales_probability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


