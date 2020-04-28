#!/usr/bin/env python3
from WellKnownHandler.handler import WellKnownHandler

from WellKnownHandler.handler import TYPE_OIDC, TYPE_SCIM, TYPE_UMA_V2

# OIDC endpoints
from WellKnownHandler.handler import KEY_OIDC_AUTHORIZATION_ENDPOINT, KEY_OIDC_TOKEN_ENDPOINT, KEY_OIDC_USERINFO_ENDPOINT, KEY_OIDC_END_SESSION_ENDPOINT, KEY_OIDC_CLIENTINFO_ENDPOINT, KEY_OIDC_INTROSPECTION_ENDPOINT, KEY_OIDC_JWKS_ENDPOINT, KEY_OIDC_REGISTRATION_ENDPOINT, KEY_OIDC_OP_POLICY_ENDPOINT, KEY_OIDC_OP_TOS_ENDPOINT, KEY_OIDC_ID_GENERATION_ENDPOINT

# OIDC supported
from WellKnownHandler.handler import KEY_OIDC_SUPPORTED_RESPONSE_TYPES, KEY_OIDC_SUPPORTED_SCOPES, KEY_OIDC_SUPPORTED_GRANT_TYPES, KEY_OIDC_SUPPORTED_CLAIMS_PARAMETER, KEY_OIDC_SUPPORTED_REQUEST_PARAMETER, KEY_OIDC_SUPPORTED_REQUEST_URI_PARAMETER, KEY_OIDC_SUPPORTED_SUBJECT_TYPES, KEY_OIDC_SUPPORTED_USERINFO_SIGNING_ALG_VALUES, KEY_OIDC_SUPPORTED_ID_TOKEN_SIGNING_ALG_VALUES
from WellKnownHandler.handler import KEY_OIDC_SUPPORTED_USERINFO_ENCRYPTION_ALG_VALUES, KEY_OIDC_SUPPORTED_USERINFO_ENCRYPTION_ENC_VALUES, KEY_OIDC_SUPPORTED_ID_TOKEN_ENCRYPTION_ALG_VALUES, KEY_OIDC_SUPPORTED_ID_TOKEN_ENCRYPTION_ENC_VALUES, KEY_OIDC_SUPPORTED_REQUEST_OBJ_SIGNING_ALG_VALUES, KEY_OIDC_SUPPORTED_REQUEST_OBJ_ENCRYPTION_ALG_VALUES, KEY_OIDC_SUPPORTED_REQUEST_OBJ_ENCRYPTION_ENC_VALUES, KEY_OIDC_SUPPORTED_AUTH_METHODS_TOKEN_ENDPOINT, KEY_OIDC_SUPPORTED_TOKEN_ENDPOINT_AUTH_SIGNING_ALG_VALUES, KEY_OIDC_SUPPORTED_DISPLAY_VALUES, KEY_OIDC_SUPPORTED_CLAIM_TYPES, KEY_OIDC_SUPPORTED_CLAIMS, KEY_OIDC_SUPPORTED_CLAIMS_LOCALES, KEY_OIDC_SUPPORTED_ACR_VALUES, KEY_OIDC_SUPPORTED_UI_LOCALES, KEY_OIDC_SUPPORTED_FRONTCHANNEL_LOGOUT, KEY_OIDC_SUPPORTED_FRONTCHANNEL_LOGOUT_SESSION

# OIDC others
from WellKnownHandler.handler import KEY_OIDC_CHECK_SESSION_IFRAME, KEY_OIDC_AUTH_LEVEL_MAPPING, KEY_OIDC_SERVICE_DOCUMENTATION, KEY_OIDC_SCOPE_TO_CLAIMS_MAPPING, KEY_OIDC_REQUIRE_REQUEST_URI_REGISTRATION

# SCIM
from WellKnownHandler.handler import KEY_SCIM_VERSION, KEY_SCIM_SUPPORTED_AUTH, KEY_SCIM_USER_ENDPOINT, KEY_SCIM_GROUP_ENDPOINT, KEY_SCIM_BULK_ENDPOINT, KEY_SCIM_SERVICE_PROVIDER_ENDPOINT, KEY_SCIM_RESOURCE_TYPES_ENDPOINT, KEY_SCIM_FIDO_DEVICES_ENDPOINT, KEY_SCIM_SCHEMAS_ENDPOINT

# UMA endpoints
from WellKnownHandler.handler import KEY_UMA_V2_AUTHORIZATION_ENDPOINT, KEY_UMA_V2_TOKEN_ENDPOINT, KEY_UMA_V2_REGISTRATION_ENDPOINT, KEY_UMA_V2_JWKS_ENDPOINT, KEY_UMA_V2_INTROSPECTION_ENDPOINT, KEY_UMA_V2_CLAIMS_INTERACTION_ENDPOINT, KEY_UMA_V2_PERMISSION_ENDPOINT, KEY_UMA_V2_RESOURCE_REGISTRATION_ENDPOINT, KEY_UMA_V2_SCOPE_ENDPOINT

# UMA supported
from WellKnownHandler.handler import KEY_UMA_V2_SUPPORTED_RESPONSE_TYPES, KEY_UMA_V2_SUPPORTED_GRANT_TYPES, KEY_UMA_V2_SUPPORTED_AUTH_METHODS_TOKEN_ENDPOINT, KEY_UMA_V2_SUPPORTED_AUTH_SIGNING_ALG_VALUES_TOKEN_ENDPOINT, KEY_UMA_V2_SUPPORTED_UI_LOCALES, KEY_UMA_V2_SUPPORTED_CODE_CHALLENGE_METHODS, KEY_UMA_V2_SUPPORTED_UMA_PROFILES