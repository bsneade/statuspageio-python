# Subscriber

Get an incident subscriber
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscriber Identifier | [optional] 
**skip_confirmation_notification** | **bool** | If this is true, do not notify the user with changes to their subscription. | [optional] 
**mode** | **str** | The communication mode of the subscriber. | [optional] 
**email** | **str** | The email address to use to contact the subscriber. Used for Email and Webhook subscribers. | [optional] 
**endpoint** | **str** | The URL where a webhook subscriber elects to receive updates. | [optional] 
**phone_number** | **str** | The phone number used to contact an SMS subscriber | [optional] 
**phone_country** | **str** | The two-character country code representing the country of which the phone_number is a part. | [optional] 
**display_phone_number** | **str** | A formatted version of the phone_number and phone_country pair, nicely formatted for display. | [optional] 
**quarantined_at** | **datetime** | The timestamp when the subscriber was quarantined due to an issue reaching them. | [optional] 
**purge_at** | **datetime** | The timestamp when a quarantined subscriber will be purged (unsubscribed). | [optional] 
**components** | **str** | The components for which the subscriber has elected to receive updates. | [optional] 
**page_access_user_id** | **str** | The Page Access user this subscriber belongs to (only for audience-specific pages). | [optional] 
**created_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


