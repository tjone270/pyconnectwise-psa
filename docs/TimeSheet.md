# TimeSheet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_end** | **str** |  | [optional] 
**date_start** | **str** |  | [optional] 
**deadline** | **str** |  | [optional] 
**hours** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**period** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_sheet import TimeSheet

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSheet from a JSON string
time_sheet_instance = TimeSheet.from_json(json)
# print the JSON string representation of the object
print TimeSheet.to_json()

# convert the object into a dict
time_sheet_dict = time_sheet_instance.to_dict()
# create an instance of TimeSheet from a dict
time_sheet_form_dict = time_sheet.from_dict(time_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


