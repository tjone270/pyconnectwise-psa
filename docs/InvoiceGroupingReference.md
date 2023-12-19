# InvoiceGroupingReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**group_parent_child_additions_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**show_price_flag** | **bool** |  | [optional] 
**show_sub_items_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_grouping_reference import InvoiceGroupingReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGroupingReference from a JSON string
invoice_grouping_reference_instance = InvoiceGroupingReference.from_json(json)
# print the JSON string representation of the object
print InvoiceGroupingReference.to_json()

# convert the object into a dict
invoice_grouping_reference_dict = invoice_grouping_reference_instance.to_dict()
# create an instance of InvoiceGroupingReference from a dict
invoice_grouping_reference_form_dict = invoice_grouping_reference.from_dict(invoice_grouping_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


