# CompanyPickerItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**company_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**company_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**company_status** | [**CompanyStatusReference**](CompanyStatusReference.md) |  | [optional] 
**company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**vendor_picker_flag** | **bool** | Gets or sets if true, this record was created by the vendor picker component. Otherwise, the record was created by the company picker component. | [optional] 

## Example

```python
from connectwise_psa.models.company_picker_item import CompanyPickerItem

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyPickerItem from a JSON string
company_picker_item_instance = CompanyPickerItem.from_json(json)
# print the JSON string representation of the object
print CompanyPickerItem.to_json()

# convert the object into a dict
company_picker_item_dict = company_picker_item_instance.to_dict()
# create an instance of CompanyPickerItem from a dict
company_picker_item_form_dict = company_picker_item.from_dict(company_picker_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


