# OsGradeWeight


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**os_grade_weight** | **float** |  | [optional] 
**os_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.os_grade_weight import OsGradeWeight

# TODO update the JSON string below
json = "{}"
# create an instance of OsGradeWeight from a JSON string
os_grade_weight_instance = OsGradeWeight.from_json(json)
# print the JSON string representation of the object
print OsGradeWeight.to_json()

# convert the object into a dict
os_grade_weight_dict = os_grade_weight_instance.to_dict()
# create an instance of OsGradeWeight from a dict
os_grade_weight_form_dict = os_grade_weight.from_dict(os_grade_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


