# Commission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**agreements_flag** | **bool** |  | [optional] 
**billing_method** | **str** |  | [optional] 
**commission_basis** | **str** |  | [optional] 
**commission_percent** | **float** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**date_end** | **datetime** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_option** | **str** |  | [optional] 
**item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**my_opportunities_flag** | **bool** |  | [optional] 
**number_of_months** | **int** |  | [optional] 
**product_category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | [optional] 
**product_sub_category** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 
**products_flag** | **bool** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**project_board** | [**ProjectBoardReference**](ProjectBoardReference.md) |  | [optional] 
**project_type** | [**ProjectTypeReference**](ProjectTypeReference.md) |  | [optional] 
**service_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**services_flag** | **bool** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**territory** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.commission import Commission

# TODO update the JSON string below
json = "{}"
# create an instance of Commission from a JSON string
commission_instance = Commission.from_json(json)
# print the JSON string representation of the object
print Commission.to_json()

# convert the object into a dict
commission_dict = commission_instance.to_dict()
# create an instance of Commission from a dict
commission_form_dict = commission.from_dict(commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


