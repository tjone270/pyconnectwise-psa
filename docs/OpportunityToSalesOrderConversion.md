# OpportunityToSalesOrderConversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_documents_flag** | **bool** |  | [optional] 
**include_all_notes_flag** | **bool** |  | [optional] 
**include_all_products_flag** | **bool** |  | [optional] 
**include_document_ids** | **List[int]** |  | [optional] 
**include_note_ids** | **List[int]** |  | [optional] 
**include_product_ids** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**sales_order_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_to_sales_order_conversion import OpportunityToSalesOrderConversion

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityToSalesOrderConversion from a JSON string
opportunity_to_sales_order_conversion_instance = OpportunityToSalesOrderConversion.from_json(json)
# print the JSON string representation of the object
print OpportunityToSalesOrderConversion.to_json()

# convert the object into a dict
opportunity_to_sales_order_conversion_dict = opportunity_to_sales_order_conversion_instance.to_dict()
# create an instance of OpportunityToSalesOrderConversion from a dict
opportunity_to_sales_order_conversion_form_dict = opportunity_to_sales_order_conversion.from_dict(opportunity_to_sales_order_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


