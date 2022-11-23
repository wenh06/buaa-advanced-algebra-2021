"""
"""

import os
import time
import re
import email
from email.header import decode_header
import imaplib
import getpass
import warnings

import pandas as pd


_EMAIL = "wenh06@buaa.edu.cn"
_SERVER = "mail.buaa.edu.cn"
_PORT = 993  # 接收端口
_SUBJECT_PATTERN = "^(?P<id>[\\d]{8})(?:[\\s]*[\\-_][\\s]*)?(?P<name>[\u4e00-\u9FFF]{0,10})(?:[\\s]*[\\-_][\\s]*)?第(?P<no>[\\d一二三四五六七八九十]{1,2})次作业"
# _BASE64_UTF8_PATTERN = "^=\?(?:utf|UTF)\-8\?(?:b|B)\?(?P<base64_string>.*)\?=$"

_zh2num = {k: v for k, v in zip("一二三四五六七八九十", range(1, 11))}
for k in "一二三四五六七八九":
    _zh2num[f"十{k}"] = 10 + _zh2num[k]

_PWD = os.path.abspath(os.path.curdir)
_STATS_FILE = os.path.join(_PWD, "统计.csv")
_COLS = [
    "学号",
    "姓名",
] + [f"第{i}次作业" for i in range(1, 20)]


def collect() -> None:
    """ """
    start = time.time()
    # connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(_SERVER, _PORT)
    mail.login(_EMAIL, getpass.getpass())

    # we choose the inbox but you can select others
    mail.select("inbox")
    # we"ll search using the ALL criteria to retrieve
    # every message inside the inbox
    # it will return with its status and a list of ids
    status, data = mail.search(None, "ALL")

    mail_ids = []
    # then we go through the list splitting its blocks
    # of bytes and appending to the mail_ids list
    for block in data:
        # the split function called without parameter
        # transforms the text or bytes into a list using
        # as separator the white spaces:
        # b"1 2 3".split() => [b"1", b"2", b"3"]
        mail_ids += block.split()
    mail_ids = mail_ids[::-1]

    if os.path.exists(_STATS_FILE):
        df_stats = pd.read_csv(_STATS_FILE)
    else:
        df_stats = pd.DataFrame(columns=_COLS)

    newly_collected = 0
    new_attachment = 0
    for i in mail_ids:
        # fetch the email message by ID
        res, msg = mail.fetch(i, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])

                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    try:
                        From = From.decode(encoding)
                    except Exception:
                        pass
                try:
                    From_email = re.findall(
                        "\\<(?P<email>[\\w\\d\\_\\-]+@[\\w\\d\\.\\_\\-]+)\\>",
                        msg.get("From"),
                    )[0]
                except Exception:
                    From_email = ""

                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it"s a bytes, decode to str
                    try:
                        subject = subject.decode(encoding)
                    except Exception:
                        pass
                if isinstance(subject, str):
                    subject = re.sub("高代|高等代数", "", subject)
                if not isinstance(subject, str) or not re.search(
                    _SUBJECT_PATTERN, subject
                ):
                    continue
                subject_content = list(re.finditer(_SUBJECT_PATTERN, subject))[
                    0
                ].groupdict()
                student_id = int(subject_content["id"])
                student_name = subject_content["name"]
                assignment_no = subject_content["no"]
                assignment_no = _zh2num.get(assignment_no, assignment_no)

                if student_name == "" and From != "" and isChinese(From, strict=True):
                    student_name = From

                df_assignment = df_stats[
                    (df_stats["学号"] == student_id)
                    & (~df_stats[f"第{assignment_no}次作业"].isna())
                ]

                if not df_assignment.empty:
                    print(
                        f"{student_name}({student_id}) 第{assignment_no}次作业 already collected."
                    )
                    print("Continue.")
                    print("=" * 100)
                    continue

                print("Subject:", subject)
                print("From:", From)
                print("Email address:", From_email)

                folder_name = os.path.join(
                    _PWD, "attachments", f"{student_id}-{student_name}"
                )
                save_folder_name = os.path.join(folder_name, f"第{assignment_no}次作业")
                os.makedirs(save_folder_name, exist_ok=True)

                if student_id not in df_stats.学号.values.tolist():
                    df_stats = df_stats.append(
                        {
                            "学号": student_id,
                            "姓名": student_name,
                            f"第{assignment_no}次作业": -1,
                        },
                        ignore_index=True,
                    )
                else:
                    df_stats.loc[
                        df_stats["学号"] == student_id, f"第{assignment_no}次作业"
                    ] = -1
                newly_collected += 1

                if not msg.is_multipart():
                    continue

                msg_content_type = msg.get_content_type()

                if msg_content_type in [
                    "multipart/mixed",
                    "multipart/related",
                ]:  # with attachments or inline image
                    print("with attachments or inline images")
                    for part in msg.get_payload():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        content_transfer_encoding = part.get(
                            "Content-Transfer-Encoding"
                        )
                        if (
                            content_type == "text/plain"
                            and "attachment" not in content_disposition
                        ):
                            try:
                                body = part.get_payload(decode=True).decode()
                            except Exception:
                                body = ""
                            # print text/plain emails and skip attachments
                            print(body)
                        elif (
                            "attachment" in content_disposition
                            or content_type.startswith("image")
                        ):
                            # download attachment
                            filename, encoding = decode_header(part.get_filename())[0]
                            if encoding:
                                filename = filename.decode(encoding)
                            if filename:
                                filename = re.sub("[\\s]+", "-", filename)
                                filepath = os.path.join(save_folder_name, filename)
                                # download attachment or inline image and save it
                                # TODO: compress before saving
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                    new_attachment += 1
                            else:
                                warnings.warn(
                                    f"{student_name}({student_id}) 第{assignment_no}次作业未找到附件或内嵌图片"
                                )
                else:
                    warnings.warn(
                        f"{student_name}({student_id}) 第{assignment_no}次作业未找到附件或内嵌图片"
                    )
                print("=" * 100)
    df_stats.to_csv(_STATS_FILE, index=False)
    print(f"collection used {time.time()-start:.2f} seconds")
    print(f"新收取作业{newly_collected}份，附件{new_attachment}份")


def isChinese(text: str, strict: bool = False) -> bool:
    """ """
    pattern = "[\u4e00-\u9FFF]"
    if not re.search(pattern, text):  # contains Chinese
        return False
    if not strict:
        pattern = "^[\u4e00-\u9FFF0-9a-zA-Z]+$"  # allow for Chinese along with numbers and English characters
    else:
        pattern = "^[\u4e00-\u9FFF]+$"  # only Chinese
    if not re.search(pattern, text):
        return False
    return True


if __name__ == "__main__":
    collect()
