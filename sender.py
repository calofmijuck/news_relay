import thecampy
from credentials import USER_ID, USER_PW
from soldier_info import SOLDIER_NAME, SOLDIER_BIRTHDAY, SOLDIER_START_DATE

soldier = thecampy.Soldier(SOLDIER_NAME, SOLDIER_BIRTHDAY, SOLDIER_START_DATE)


def send(subject, content):
    content += '\n[FINISH]'
    msg_num = 0
    char_count = 0
    enter_count = 0
    buffer = []
    for i, char in enumerate(content):
        buffer.append(char)
        char_count += 1
        if char == '\n':
            enter_count += 1

        if char_count > 1495 or enter_count > 22 or i == len(content) - 1:
            _send(subject + f" - {msg_num}", ''.join(buffer))

            char_count = 0
            enter_count = 0
            buffer = []

            msg_num += 1


def _send(subject, content):
    try:
        msg = thecampy.Message(subject, content)
        tc = thecampy.client()
        tc.login(USER_ID, USER_PW)

        add_result = tc.add_soldier(soldier)
        get_result = tc.get_soldier(soldier)
        send_result = tc.send_message(soldier, msg)
        return True
    except Exception as p:
        return False
