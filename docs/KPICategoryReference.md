# KPICategoryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.kpi_category_reference import KPICategoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of KPICategoryReference from a JSON string
kpi_category_reference_instance = KPICategoryReference.from_json(json)
# print the JSON string representation of the object
print KPICategoryReference.to_json()

# convert the object into a dict
kpi_category_reference_dict = kpi_category_reference_instance.to_dict()
# create an instance of KPICategoryReference from a dict
kpi_category_reference_form_dict = kpi_category_reference.from_dict(kpi_category_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


