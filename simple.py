def pam_sm_authenticate(pamh, flags, argv):
    pwd_msg = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "password:"))
    if pwd_msg.resp == "pw":
        return pamh.PAM_SUCCESS
    else:
        return pamh.PAM_AUTH_ERR

