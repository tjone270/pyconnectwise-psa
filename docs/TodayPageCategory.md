# TodayPageCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 30; | 
**sort_order** | **int** |  | 

## Example

```python
from connectwise_psa.models.today_page_category import TodayPageCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TodayPageCategory from a JSON string
today_page_category_instance = TodayPageCategory.from_json(json)
# print the JSON string representation of the object
print TodayPageCategory.to_json()

# convert the object into a dict
today_page_category_dict = today_page_category_instance.to_dict()
# create an instance of TodayPageCategory from a dict
today_page_category_form_dict = today_page_category.from_dict(today_page_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


