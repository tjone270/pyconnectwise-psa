# Order


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_closed_flag** | **bool** |  | [optional] 
**bill_shipped_flag** | **bool** |  | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**bottom_comment_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**config_ids** | **List[int]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**document_ids** | **List[int]** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_ids** | **List[int]** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**order_date** | **datetime** |  | [optional] 
**phone** | **str** |  | [optional] 
**phone_ext** | **str** |  | [optional] 
**po_number** | **str** |  Max length: 50; | [optional] 
**product_ids** | **List[int]** |  | [optional] 
**restrict_downpayment_flag** | **bool** |  | [optional] 
**sales_rep** | [**MemberReference**](MemberReference.md) |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**status** | [**OrderStatusReference**](OrderStatusReference.md) |  | [optional] 
**sub_total** | **float** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_total** | **float** |  | [optional] 
**top_comment_flag** | **bool** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print Order.to_json()

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_form_dict = order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


