# KPIReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.kpi_reference import KPIReference

# TODO update the JSON string below
json = "{}"
# create an instance of KPIReference from a JSON string
kpi_reference_instance = KPIReference.from_json(json)
# print the JSON string representation of the object
print KPIReference.to_json()

# convert the object into a dict
kpi_reference_dict = kpi_reference_instance.to_dict()
# create an instance of KPIReference from a dict
kpi_reference_form_dict = kpi_reference.from_dict(kpi_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


