def pam_sm_authenticate(pamh, flags, argv):
    pwd_msg = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "password:"))
    if pwd_msg.resp != "pw":
        return pamh.PAM_AUTH_ERR        
    else:
        snd_msg = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_ON, "second factor:"))        
        if snd_msg.resp == "1234":
            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_AUTH_ERR
