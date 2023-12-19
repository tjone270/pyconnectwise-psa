# ProductRecurring


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_cycle_id** | **int** |  | [optional] 
**cycle_type** | **str** |  | [optional] 
**cycles** | **int** |  | [optional] 
**end_date** | **str** | The Recurring End Date is calculated based on the             start date, number of cycles, and cycle type. | [optional] 
**recurring_cost** | **float** |  | [optional] 
**recurring_revenue** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_recurring import ProductRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRecurring from a JSON string
product_recurring_instance = ProductRecurring.from_json(json)
# print the JSON string representation of the object
print ProductRecurring.to_json()

# convert the object into a dict
product_recurring_dict = product_recurring_instance.to_dict()
# create an instance of ProductRecurring from a dict
product_recurring_form_dict = product_recurring.from_dict(product_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


