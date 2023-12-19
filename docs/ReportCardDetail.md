# ReportCardDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**kpi** | [**KPIReference**](KPIReference.md) |  | [optional] 
**report_card** | [**ReportCardReference**](ReportCardReference.md) |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.report_card_detail import ReportCardDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCardDetail from a JSON string
report_card_detail_instance = ReportCardDetail.from_json(json)
# print the JSON string representation of the object
print ReportCardDetail.to_json()

# convert the object into a dict
report_card_detail_dict = report_card_detail_instance.to_dict()
# create an instance of ReportCardDetail from a dict
report_card_detail_form_dict = report_card_detail.from_dict(report_card_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


