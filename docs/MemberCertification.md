# MemberCertification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**certification** | [**CertificationReference**](CertificationReference.md) |  | 
**certification_number** | **str** |  Max length: 50; | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**date_expires** | **datetime** |  | [optional] 
**date_received** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**percent_complete** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_certification import MemberCertification

# TODO update the JSON string below
json = "{}"
# create an instance of MemberCertification from a JSON string
member_certification_instance = MemberCertification.from_json(json)
# print the JSON string representation of the object
print MemberCertification.to_json()

# convert the object into a dict
member_certification_dict = member_certification_instance.to_dict()
# create an instance of MemberCertification from a dict
member_certification_form_dict = member_certification.from_dict(member_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


