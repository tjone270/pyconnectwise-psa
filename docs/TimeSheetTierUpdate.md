# TimeSheetTierUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_sheet_tier_update import TimeSheetTierUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSheetTierUpdate from a JSON string
time_sheet_tier_update_instance = TimeSheetTierUpdate.from_json(json)
# print the JSON string representation of the object
print TimeSheetTierUpdate.to_json()

# convert the object into a dict
time_sheet_tier_update_dict = time_sheet_tier_update_instance.to_dict()
# create an instance of TimeSheetTierUpdate from a dict
time_sheet_tier_update_form_dict = time_sheet_tier_update.from_dict(time_sheet_tier_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


