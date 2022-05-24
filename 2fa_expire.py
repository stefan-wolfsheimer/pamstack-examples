import datetime
import json

def pam_sm_authenticate(pamh, flags, argv):
    pwd_msg = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, "password:"))
    if pwd_msg.resp != "pw":
        return pamh.PAM_AUTH_ERR        
    else:
        dtg = datetime.datetime.now() + datetime.timedelta(seconds=10)
        msg={"prompt": "second factor:",
             "key": "2ndfactor",
             "password": True,
             "context": "iinit",
             "expire": dtg.strftime("%Y-%m-%d %H:%M:%S")}
        
        snd_msg = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_ON, json.dumps(msg)))
        if snd_msg.resp == "1234":
            return pamh.PAM_SUCCESS
        else:
            return pamh.PAM_AUTH_ERR
