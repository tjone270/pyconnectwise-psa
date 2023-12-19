# ServiceSignoff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billing_methods_text** | **str** |  Max length: 2000; | [optional] 
**billing_methods_text_flag** | **bool** | On add/post, if billingMethodsText.Length &gt; 0, this is set to true. | [optional] 
**billing_terms_flag** | **bool** |  | [optional] 
**company_info_flag** | **bool** |  | [optional] 
**configurations_flag** | **bool** |  | [optional] 
**credit_card_fields_flag** | **bool** |  | [optional] 
**customer_signoff_fields_flag** | **bool** |  | [optional] 
**customer_signoff_text** | **str** |  Max length: 4000; | [optional] 
**customer_signoff_text_flag** | **bool** | On add/post, if customerSignoffText.Length &gt; 0, this is set to true. | [optional] 
**default_ff_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**discussion_flag** | **bool** |  | [optional] 
**expense_agreement_flag** | **bool** |  | [optional] 
**expense_amount_flag** | **bool** |  | [optional] 
**expense_bill_flag** | **bool** |  | [optional] 
**expense_date_flag** | **bool** |  | [optional] 
**expense_flag** | **bool** | On add/post, if any expense related flag is set to true, this is also set to true. | [optional] 
**expense_manual_entry** | **int** |  | [optional] 
**expense_manual_flag** | **bool** |  | [optional] 
**expense_member_flag** | **bool** |  | [optional] 
**expense_notes_flag** | **bool** |  | [optional] 
**expense_tax_flag** | **bool** |  | [optional] 
**expense_type_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**product_agreement_flag** | **bool** |  | [optional] 
**product_bill_flag** | **bool** |  | [optional] 
**product_description_flag** | **bool** |  | [optional] 
**product_extended_amount_flag** | **bool** |  | [optional] 
**product_flag** | **bool** | On add/post, if any product related flag is set to true, this is also set to true. | [optional] 
**product_manual_entry** | **int** |  | [optional] 
**product_manual_flag** | **bool** |  | [optional] 
**product_price_flag** | **bool** |  | [optional] 
**product_quantity_flag** | **bool** |  | [optional] 
**product_tax_flag** | **bool** |  | [optional] 
**resolution_flag** | **bool** |  | [optional] 
**summary_flag** | **bool** |  | [optional] 
**task** | **str** | On add/post, if this is set but no value is set for taskFlag, taskFlag is set to true. | [optional] 
**task_flag** | **bool** | On add/post, if this is set to true but no value is set for task, task is defaulted to ServiceTasks.All. | [optional] 
**technician_signoff_flag** | **bool** |  | [optional] 
**time_agreement_flag** | **bool** |  | [optional] 
**time_bill_flag** | **bool** |  | [optional] 
**time_date_flag** | **bool** |  | [optional] 
**time_extended_amount_flag** | **bool** |  | [optional] 
**time_flag** | **bool** | On add/post, if any time related flag is set to true, this is also set to true. | [optional] 
**time_hours_flag** | **bool** |  | [optional] 
**time_manual_entry** | **int** |  | [optional] 
**time_manual_flag** | **bool** |  | [optional] 
**time_member_flag** | **bool** |  | [optional] 
**time_notes_flag** | **bool** |  | [optional] 
**time_rate_flag** | **bool** |  | [optional] 
**time_start_end_flag** | **bool** |  | [optional] 
**time_tax_flag** | **bool** |  | [optional] 
**time_work_type_flag** | **bool** |  | [optional] 
**visible_logo_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_signoff import ServiceSignoff

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSignoff from a JSON string
service_signoff_instance = ServiceSignoff.from_json(json)
# print the JSON string representation of the object
print ServiceSignoff.to_json()

# convert the object into a dict
service_signoff_dict = service_signoff_instance.to_dict()
# create an instance of ServiceSignoff from a dict
service_signoff_form_dict = service_signoff.from_dict(service_signoff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


