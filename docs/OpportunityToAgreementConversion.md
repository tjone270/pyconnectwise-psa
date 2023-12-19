# OpportunityToAgreementConversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_id** | **int** |  | [optional] 
**bill_cycle_id** | **int** |  | [optional] 
**bill_one_time_flag** | **bool** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**end_date** | **str** |  | [optional] 
**include_all_documents_flag** | **bool** |  | [optional] 
**include_all_notes_flag** | **bool** |  | [optional] 
**include_all_products_flag** | **bool** |  | [optional] 
**include_document_ids** | **List[int]** |  | [optional] 
**include_note_ids** | **List[int]** |  | [optional] 
**include_product_ids** | **List[int]** |  | [optional] 
**location_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**no_ending_date_flag** | **bool** |  | [optional] 
**start_date** | **str** |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_to_agreement_conversion import OpportunityToAgreementConversion

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityToAgreementConversion from a JSON string
opportunity_to_agreement_conversion_instance = OpportunityToAgreementConversion.from_json(json)
# print the JSON string representation of the object
print OpportunityToAgreementConversion.to_json()

# convert the object into a dict
opportunity_to_agreement_conversion_dict = opportunity_to_agreement_conversion_instance.to_dict()
# create an instance of OpportunityToAgreementConversion from a dict
opportunity_to_agreement_conversion_form_dict = opportunity_to_agreement_conversion.from_dict(opportunity_to_agreement_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


