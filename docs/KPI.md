# KPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**KPICategoryReference**](KPICategoryReference.md) |  | [optional] 
**date_filter** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.kpi import KPI

# TODO update the JSON string below
json = "{}"
# create an instance of KPI from a JSON string
kpi_instance = KPI.from_json(json)
# print the JSON string representation of the object
print KPI.to_json()

# convert the object into a dict
kpi_dict = kpi_instance.to_dict()
# create an instance of KPI from a dict
kpi_form_dict = kpi.from_dict(kpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


