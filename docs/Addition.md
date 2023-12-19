# Addition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**agreement_status** | **str** |  | [optional] 
**bill_customer** | **str** |  | 
**billed_quantity** | **float** |  | [optional] 
**cancelled_date** | **datetime** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**description** | **str** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**ext_cost** | **float** |  | [optional] 
**ext_price** | **float** |  | [optional] 
**extended_prorate_cost** | **float** |  | [optional] 
**extended_prorate_price** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_description** | **str** |  Max length: 6000; | [optional] 
**invoice_grouping** | [**InvoiceGroupingReference**](InvoiceGroupingReference.md) |  | [optional] 
**less_included** | **float** |  | [optional] 
**margin** | **float** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**prorate_cost** | **float** |  | [optional] 
**prorate_current_period_flag** | **bool** |  | [optional] 
**prorate_price** | **float** |  | [optional] 
**purchase_item_flag** | **bool** |  | [optional] 
**quantity** | **float** |  | [optional] 
**sequence_number** | **float** |  | [optional] 
**serial_number** | **str** |  Max length: 50; | [optional] 
**special_order_flag** | **bool** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**uom** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.addition import Addition

# TODO update the JSON string below
json = "{}"
# create an instance of Addition from a JSON string
addition_instance = Addition.from_json(json)
# print the JSON string representation of the object
print Addition.to_json()

# convert the object into a dict
addition_dict = addition_instance.to_dict()
# create an instance of Addition from a dict
addition_form_dict = addition.from_dict(addition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


