# BoardStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**closed_status** | **bool** |  | [optional] 
**custom_status_indicator_name** | **str** |  Max length: 30; | [optional] 
**customer_portal_description** | **str** |  Max length: 500; | [optional] 
**customer_portal_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**display_on_board** | **bool** |  | [optional] 
**email_template** | [**ServiceEmailTemplateReference**](ServiceEmailTemplateReference.md) |  | [optional] 
**escalation_status** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**round_robin_catchall** | **bool** |  | [optional] 
**save_time_as_note** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**status_indicator** | [**StatusIndicatorReference**](StatusIndicatorReference.md) |  | [optional] 
**time_entry_not_allowed** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_status import BoardStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BoardStatus from a JSON string
board_status_instance = BoardStatus.from_json(json)
# print the JSON string representation of the object
print BoardStatus.to_json()

# convert the object into a dict
board_status_dict = board_status_instance.to_dict()
# create an instance of BoardStatus from a dict
board_status_form_dict = board_status.from_dict(board_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


