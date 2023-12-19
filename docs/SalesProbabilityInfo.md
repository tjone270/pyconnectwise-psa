# SalesProbabilityInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**probability** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_probability_info import SalesProbabilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SalesProbabilityInfo from a JSON string
sales_probability_info_instance = SalesProbabilityInfo.from_json(json)
# print the JSON string representation of the object
print SalesProbabilityInfo.to_json()

# convert the object into a dict
sales_probability_info_dict = sales_probability_info_instance.to_dict()
# create an instance of SalesProbabilityInfo from a dict
sales_probability_info_form_dict = sales_probability_info.from_dict(sales_probability_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


