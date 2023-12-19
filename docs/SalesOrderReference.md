# SalesOrderReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_order_reference import SalesOrderReference

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderReference from a JSON string
sales_order_reference_instance = SalesOrderReference.from_json(json)
# print the JSON string representation of the object
print SalesOrderReference.to_json()

# convert the object into a dict
sales_order_reference_dict = sales_order_reference_instance.to_dict()
# create an instance of SalesOrderReference from a dict
sales_order_reference_form_dict = sales_order_reference.from_dict(sales_order_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


