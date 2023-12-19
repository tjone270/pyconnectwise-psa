# OnPremiseSearchSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**password** | **str** |  | 

## Example

```python
from connectwise_psa.models.on_premise_search_setting import OnPremiseSearchSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremiseSearchSetting from a JSON string
on_premise_search_setting_instance = OnPremiseSearchSetting.from_json(json)
# print the JSON string representation of the object
print OnPremiseSearchSetting.to_json()

# convert the object into a dict
on_premise_search_setting_dict = on_premise_search_setting_instance.to_dict()
# create an instance of OnPremiseSearchSetting from a dict
on_premise_search_setting_form_dict = on_premise_search_setting.from_dict(on_premise_search_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


