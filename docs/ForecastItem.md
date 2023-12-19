# ForecastItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_cycle** | [**BillingCycleReference**](BillingCycleReference.md) |  | [optional] 
**catalog_item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**cycle_basis** | **str** |  | [optional] 
**cycles** | **int** |  | [optional] 
**forecast_description** | **str** |  Max length: 50; | [optional] 
**forecast_type** | **str** |  | 
**id** | **int** |  | [optional] 
**include_flag** | **bool** |  | [optional] 
**link_flag** | **bool** |  | [optional] 
**margin** | **float** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**percentage** | **int** |  | [optional] 
**product_class** | **str** |  | [optional] 
**product_description** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**quote_werks_doc_name** | **str** |  Max length: 255; | [optional] 
**quote_werks_doc_no** | **str** |  Max length: 20; | [optional] 
**quote_werks_quantity** | **int** |  | [optional] 
**recurring_cost** | **float** |  | [optional] 
**recurring_date_end** | **datetime** |  | [optional] 
**recurring_date_start** | **datetime** |  | [optional] 
**recurring_flag** | **bool** |  | [optional] 
**recurring_revenue** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 
**sequence_number** | **float** |  | [optional] 
**status** | [**OpportunityStatusReference**](OpportunityStatusReference.md) |  | [optional] 
**sub_number** | **int** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.forecast_item import ForecastItem

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastItem from a JSON string
forecast_item_instance = ForecastItem.from_json(json)
# print the JSON string representation of the object
print ForecastItem.to_json()

# convert the object into a dict
forecast_item_dict = forecast_item_instance.to_dict()
# create an instance of ForecastItem from a dict
forecast_item_form_dict = forecast_item.from_dict(forecast_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


