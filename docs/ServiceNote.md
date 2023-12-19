# ServiceNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**customer_updated_flag** | **bool** |  | [optional] 
**date_created** | **str** |  | [optional] 
**detail_description_flag** | **bool** |  | [optional] 
**external_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_analysis_flag** | **bool** |  | [optional] 
**internal_flag** | **bool** |  | [optional] 
**issue_flag** | **bool** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**process_notifications** | **bool** |  | [optional] 
**resolution_flag** | **bool** |  | [optional] 
**sentiment_score** | **float** |  | [optional] 
**text** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_note import ServiceNote

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceNote from a JSON string
service_note_instance = ServiceNote.from_json(json)
# print the JSON string representation of the object
print ServiceNote.to_json()

# convert the object into a dict
service_note_dict = service_note_instance.to_dict()
# create an instance of ServiceNote from a dict
service_note_form_dict = service_note.from_dict(service_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


