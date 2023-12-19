# OpportunityToServiceTicketConversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_all_documents_flag** | **bool** |  | [optional] 
**include_all_notes_flag** | **bool** |  | [optional] 
**include_all_products_flag** | **bool** |  | [optional] 
**include_document_ids** | **List[int]** |  | [optional] 
**include_note_ids** | **List[int]** |  | [optional] 
**include_product_ids** | **List[int]** |  | [optional] 
**summary** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_to_service_ticket_conversion import OpportunityToServiceTicketConversion

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityToServiceTicketConversion from a JSON string
opportunity_to_service_ticket_conversion_instance = OpportunityToServiceTicketConversion.from_json(json)
# print the JSON string representation of the object
print OpportunityToServiceTicketConversion.to_json()

# convert the object into a dict
opportunity_to_service_ticket_conversion_dict = opportunity_to_service_ticket_conversion_instance.to_dict()
# create an instance of OpportunityToServiceTicketConversion from a dict
opportunity_to_service_ticket_conversion_form_dict = opportunity_to_service_ticket_conversion.from_dict(opportunity_to_service_ticket_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


