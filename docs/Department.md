# Department


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 15; | 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.department import Department

# TODO update the JSON string below
json = "{}"
# create an instance of Department from a JSON string
department_instance = Department.from_json(json)
# print the JSON string representation of the object
print Department.to_json()

# convert the object into a dict
department_dict = department_instance.to_dict()
# create an instance of Department from a dict
department_form_dict = department.from_dict(department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


