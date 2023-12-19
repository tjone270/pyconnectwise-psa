# KPICategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.kpi_category import KPICategory

# TODO update the JSON string below
json = "{}"
# create an instance of KPICategory from a JSON string
kpi_category_instance = KPICategory.from_json(json)
# print the JSON string representation of the object
print KPICategory.to_json()

# convert the object into a dict
kpi_category_dict = kpi_category_instance.to_dict()
# create an instance of KPICategory from a dict
kpi_category_form_dict = kpi_category.from_dict(kpi_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


